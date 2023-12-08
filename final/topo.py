#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node, OVSSwitch
from mininet.log import setLogLevel, info
from mininet.cli import CLI


class LinuxRouter(Node):
    "A Node with IP forwarding enabled."

    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


class NetworkTopo(Topo):
    def build(self, **_opts):
        r1 = self.addHost('r1', cls=LinuxRouter, ip='10.0.0.10/24')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(s1, r1, intfName2='r1-eth1', params2={'ip': '10.0.0.10/24'})
        self.addLink(s2, r1, intfName2='r1-eth2', params2={'ip': '10.0.0.10/24'})

        h1 = self.addHost('h1', ip='10.0.0.1/24', defaultRoute='via 10.0.0.10')
        h2 = self.addHost('h2', ip='10.0.0.2/24', defaultRoute='via 10.0.0.10')

        self.addLink(h1, s1)
        self.addLink(h2, s2)


def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo)
    net.start()

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()