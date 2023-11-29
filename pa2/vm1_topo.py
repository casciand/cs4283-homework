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
        # Add routers
        r1 = self.addHost('r1', cls=LinuxRouter, ip='10.0.0.1/24')
        r2 = self.addHost('r2', cls=LinuxRouter, ip='10.1.0.1/24')
        r3 = self.addHost('r3', cls=LinuxRouter, ip='10.2.0.1/24')

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add host-switch links in the same subnet.  We need this because now
        # we want to connect our routers to their respective switches. We must also
        # name the interfaces, here r1-eth1 and so on, and make sure to assign an
        # IP address facing the LAN.
        self.addLink(s1, r1, intfName2='r1-eth1', params2={'ip': '10.0.0.1/24'})
        self.addLink(s2, r2, intfName2='r2-eth2', params2={'ip': '10.1.0.1/24'})
        self.addLink(s3, r3, intfName2="r3-eth3", params2={'ip': '10.2.0.1/24'})

        # Add links between routers to form the triangle
        self.addLink(r1, r2, intfName1='r1-eth2', intfName2='r2-eth1', params1={'ip': '10.100.0.1/24'},
                     params2={'ip': '10.100.0.2/24'})
        self.addLink(r2, r3, intfName1='r2-eth3', intfName2='r3-eth2', params1={'ip': '10.101.0.1/24'},
                     params2={'ip': '10.101.0.2/24'})
        self.addLink(r3, r1, intfName1='r3-eth1', intfName2='r1-eth3', params1={'ip': '10.102.0.1/24'},
                     params2={'ip': '10.102.0.2/24'})

        # Add hosts and their connections to switches
        d1 = self.addHost('d1', ip='10.0.0.251/24', defaultRoute='via 10.0.0.1')
        d2 = self.addHost('d2', ip='10.1.0.252/24', defaultRoute='via 10.1.0.1')

        # Add host-switch links
        self.addLink(d1, s1)
        self.addLink(d2, s2)


def run():
    # first, instantiate our topology. Recall that everything is hardcoded in this
    # topology
    topo = NetworkTopo()

    # Then create the network object from this topology
    net = Mininet(topo=topo)

    # start the network before configuring the router
    net.start()

    info(net['r1'].cmd("ip route show"))
    info(net['r2'].cmd("ip route show"))
    info(net['r3'].cmd("ip route show"))

    # Configure routers
    route_commands = [
        ("r1", "ip route add 10.1.0.0/24 via 10.100.0.2 dev r1-eth2"),
        ("r1", "ip route add 10.2.0.1/32 via 10.102.0.1 dev r1-eth3"),
        ("r2", "ip route add 10.0.0.0/24 via 10.100.0.1 dev r2-eth1"),
        ("r2", "ip route add 10.2.0.1/32 via 10.101.0.2 dev r2-eth3"),
        ("r3", "ip route add 10.0.0.0/24 via 10.102.0.2 dev r3-eth1"),
        ("r3", "ip route add 10.1.0.0/24 via 10.101.0.1 dev r3-eth2"),
        ('r3', 'ip route add 10.2.0.0/24 via 10.103.0.2 dev r3-nat-eth')
    ]

    for (router, cmd) in route_commands:
        print(f"Executing on {router}: {cmd}")
        result = net[router].cmd(cmd)
        if "Error" in result:
            print(f"Error executing {cmd} on {router}: {result}")

    CLI(net)  # this gives us mininet prompt
    net.stop()  # this cleans up the network


if __name__ == '__main__':
    setLogLevel('info')
    run()