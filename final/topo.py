import argparse

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node, OVSSwitch
from mininet.log import setLogLevel, info
from mininet.cli import CLI

global parsed_args


class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


class NetworkTopo(Topo):
    def build(self, **_opts):
        num_intermediates = parsed_args.hosts

        # Initialize client
        client = self.addHost('h1')
        prev_switch = self.addSwitch('s1')
        self.addLink(client, prev_switch)

        # Initialize intermediate nodes
        for i in range(num_intermediates):
            host = self.addHost(f'h{i + 2}')
            switch = self.addSwitch(f's{i + 2}')
            self.addLink(host, switch)
            self.addLink(prev_switch, switch)
            prev_switch = switch

        # Initialize server
        server = self.addHost(f'h{num_intermediates + 2}')
        switch = self.addSwitch(f's{num_intermediates + 2}')
        self.addLink(server, switch)
        self.addLink(prev_switch, switch)


def parse_args():
    # Parse the command line
    parser = argparse.ArgumentParser()

    # Add optional arguments
    parser.add_argument("-n", "--hosts", type=int, default=3,
                        help="Number of intermediate hosts (default: 3)")
    args = parser.parse_args()

    return args


def run():
    global parsed_args
    parsed_args = parse_args()
    num_intermediates = parsed_args.hosts

    topo = NetworkTopo()
    net = Mininet(topo=topo)
    net.start()

    # Public key exchange and message traversal
    net[f'h{num_intermediates + 2}'].cmd(f'python3 server.py -a 10.0.0.{num_intermediates + 2} > server_output.txt &')

    for i in range(num_intermediates):
        net[f'h{i + 2}'].cmd(f'python3 intermediate.py -a 10.0.0.{i + 2} > h{i + 2}_output.txt &')

    net['h1'].cmd(f'python3 client.py -n {num_intermediates} > client_output.txt &')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
