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
        rP = self.addHost('P', cls=LinuxRouter, ip='10.0.0.1/24')
        rQ = self.addHost('Q', cls=LinuxRouter, ip='10.1.0.1/24')
        rR = self.addHost('R', cls=LinuxRouter, ip='10.2.0.1/24')
        rS = self.addHost('S', cls=LinuxRouter, ip='10.3.0.1/24')
        rT = self.addHost('T', cls=LinuxRouter, ip='10.4.0.1/24')
        rU = self.addHost('U', cls=LinuxRouter, ip='10.5.0.1/24')
        rV = self.addHost('V', cls=LinuxRouter, ip='10.6.0.1/24')

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        # Add host-switch links in the same subnet.  We need this because now
        # we want to connect our routers to their respective switches. We must also
        # name the interfaces, here r1-eth1 and so on, and make sure to assign an
        # IP address facing the LAN.
        self.addLink(s1, rP, intfName2='s1-rP-eth', params2={'ip': '10.0.0.1/24'})
        self.addLink(s2, rQ, intfName2='s2-rQ-eth', params2={'ip': '10.1.0.1/24'})
        self.addLink(s3, rR, intfName2="s3-rR-eth", params2={'ip': '10.2.0.1/24'})
        self.addLink(rS, rS, intfName2="rS-eth", params2={'ip': '10.3.0.1/24'})
        self.addLink(rT, rT, intfName2="rT-eth", params2={'ip': '10.4.0.1/24'})
        self.addLink(s4, rU, intfName2="s4-rU-eth", params2={'ip': '10.5.0.1/24'})
        self.addLink(s5, rV, intfName2="s5-rV-eth", params2={'ip': '10.6.0.1/24'})

        # Add links between routers to form the triangle
        self.addLink(rP, rQ, intfName1='rP-rQ-eth', params1={'ip': '10.100.0.1/24'},
                             intfName2='rQ-rP-eth', params2={'ip': '10.100.0.2/24'})
        self.addLink(rR, rP, intfName1='rR-rP-eth', params1={'ip': '10.101.0.1/24'},
                             intfName2='rP-rR-eth', params2={'ip': '10.101.0.2/24'})
        self.addLink(rS, rQ, intfName1='rS-rQ-eth', params1={'ip': '10.102.0.1/24'},
                             intfName2='rQ-rS-eth', params2={'ip': '10.102.0.2/24'})
        self.addLink(rS, rR, intfName1='rS-rR-eth', params1={'ip': '10.103.0.1/24'},
                             intfName2='rR-rS-eth', params2={'ip': '10.103.0.2/24'})
        self.addLink(rT, rQ, intfName1='rT-rQ-eth', params1={'ip': '10.104.0.1/24'},
                             intfName2='rQ-rT-eth', params2={'ip': '10.104.0.2/24'})
        self.addLink(rU, rS, intfName1='rU-rS-eth', params1={'ip': '10.105.0.1/24'},
                             intfName2='rS-rU-eth', params2={'ip': '10.105.0.2/24'})
        self.addLink(rU, rR, intfName1='rU-rR-eth', params1={'ip': '10.106.0.1/24'},
                             intfName2='rR-rU-eth', params2={'ip': '10.106.0.2/24'})
        self.addLink(rU, rV, intfName1='rU-rV-eth', params1={'ip': '10.107.0.1/24'},
                             intfName2='rV-rU-eth', params2={'ip': '10.107.0.2/24'})
        self.addLink(rV, rS, intfName1='rV-rS-eth', params1={'ip': '10.108.0.1/24'},
                             intfName2='rS-rV-eth', params2={'ip': '10.108.0.2/24'})
        self.addLink(rV, rT, intfName1='rV-rT-eth', params1={'ip': '10.109.0.1/24'},
                             intfName2='rT-rV-eth', params2={'ip': '10.109.0.2/24'})
        self.addLink(rV, rQ, intfName1='rV-rQ-eth', params1={'ip': '10.110.0.1/24'},
                             intfName2='rQ-rV-eth', params2={'ip': '10.110.0.2/24'})

        # Add hosts and their connections to switches
        h1 = self.addHost('h1', ip='10.0.0.251/24', defaultRoute='via 10.0.0.1')
        h2 = self.addHost('h2', ip='10.0.0.250/24', defaultRoute='via 10.0.0.1')
        h3 = self.addHost('h3', ip='10.1.0.252/24', defaultRoute='via 10.1.0.1')
        h4 = self.addHost('h4', ip='10.2.0.249/24', defaultRoute='via 10.2.0.1')
        h5 = self.addHost('h5', ip='10.5.0.248/24', defaultRoute='via 10.5.0.1')
        h6 = self.addHost('h6', ip='10.5.0.247/24', defaultRoute='via 10.5.0.1')
        h7 = self.addHost('h7', ip='10.6.0.246/24', defaultRoute='via 10.6.0.1')

        # Add host-switch links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s3)
        self.addLink(h5, s4)
        self.addLink(h6, s4)
        self.addLink(h7, s5)


def run():
    # first, instantiate our topology. Recall that everything is hardcoded in this
    # topology
    topo = NetworkTopo()

    # Then create the network object from this topology
    net = Mininet(topo=topo)

    # start the network before configuring the router
    net.start()

    # info(net['P'].cmd("ip route show"))
    # info(net['Q'].cmd("ip route show"))
    # info(net['R'].cmd("ip route show"))

    # Configure routers
    route_commands = [
        ("P", "ip route add 10.1.0.0/24 via 10.100.0.2 dev rP-rQ-eth"),  # P to Q
        ("P", "ip route add 10.2.0.0/24 via 10.101.0.1 dev rP-rR-eth"),  # P to R
        ("P", "ip route add 10.3.0.0/24 via 10.101.0.1 dev rP-rR-eth"),  # P to S via R
        ("P", "ip route add 10.103.0.0/24 via 10.101.0.1 dev rP-rR-eth"),  # P to S via R
        ("P", "ip route add 10.4.0.0/24 via 10.100.0.2 dev rP-rQ-eth"),  # P to T via Q
        ("P", "ip route add 10.104.0.0/24 via 10.100.0.2 dev rP-rQ-eth"),  # P to T via Q
        ("P", "ip route add 10.5.0.0/24 via 10.101.0.1 dev rP-rR-eth"),  # P to U via R
        ("P", "ip route add 10.106.0.0/24 via 10.101.0.1 dev rP-rR-eth"),  # P to U via R
        ("P", "ip route add 10.6.0.0/24 via 10.100.0.2 dev rP-rQ-eth"),  # P to V via Q
        ("P", "ip route add 10.110.0.0/24 via 10.100.0.2 dev rP-rQ-eth"),  # P to V via Q

        ("Q", "ip route add 10.0.0.0/24 via 10.100.0.1 dev rQ-rP-eth"),  # Q to P
        ("Q", "ip route add 10.3.0.0/24 via 10.102.0.1 dev rQ-rS-eth"),  # Q to S
        ("Q", "ip route add 10.4.0.0/24 via 10.104.0.1 dev rQ-rT-eth"),  # Q to T
        ("Q", "ip route add 10.6.0.0/24 via 10.110.0.1 dev rQ-rV-eth"),  # Q to V
        ("Q", "ip route add 10.2.0.0/24 via 10.100.0.1 dev rQ-rP-eth"),  # Q to R via P
        ("Q", "ip route add 10.101.0.0/24 via 10.100.0.1 dev rQ-rP-eth"),  # Q to R via P
        ("Q", "ip route add 10.5.0.0/24 via 10.102.0.1 dev rQ-rS-eth"),  # Q to U via S
        ("Q", "ip route add 10.105.0.0/24 via 10.102.0.1 dev rQ-rS-eth"),  # Q to U via S
        # ("Q", "ip route add 10.0.0.0/24 via 10.102.0.1 dev rQ-rS-eth"),  # Q to P via R
        # ("Q", "ip route add 10.101.0.0/24 via 10.102.0.1 dev rQ-rS-eth"),  # Q to P via R

        ("R", "ip route add 10.0.0.0/24 via 10.101.0.2 dev rR-rP-eth"),  # R to P
        ("R", "ip route add 10.3.0.0/24 via 10.103.0.1 dev rR-rS-eth"),  # R to S
        ("R", "ip route add 10.5.0.0/24 via 10.106.0.1 dev rR-rU-eth"),  # R to U
        ("R", "ip route add 10.1.0.0/24 via 10.101.0.2 dev rR-rP-eth"),  # R to Q via P
        ("R", "ip route add 10.100.0.0/24 via 10.101.0.2 dev rR-rP-eth"),  # R to Q via P
        ("R", "ip route add 10.4.0.0/24 via 10.101.0.2 dev rR-rP-eth"),  # R to T via Q
        ("R", "ip route add 10.104.0.0/24 via 10.101.0.2 dev rR-rP-eth"),  # R to T via Q
        ("R", "ip route add 10.6.0.0/24 via 10.106.0.1 dev rR-rU-eth"),  # R to V via U
        ("R", "ip route add 10.107.0.0/24 via 10.106.0.1 dev rR-rU-eth"),  # R to V via U

        ("S", "ip route add 10.1.0.0/24 via 10.102.0.2 dev rS-rQ-eth"),  # S to Q
        ("S", "ip route add 10.2.0.0/24 via 10.103.0.2 dev rS-rR-eth"),  # S to R
        ("S", "ip route add 10.5.0.0/24 via 10.105.0.1 dev rS-rU-eth"),  # S to U
        ("S", "ip route add 10.6.0.0/24 via 10.108.0.1 dev rS-rV-eth"),  # S to V
        ("S", "ip route add 10.0.0.0/24 via 10.103.0.2 dev rS-rR-eth"),  # S to P via R
        ("S", "ip route add 10.101.0.0/24 via 10.103.0.2 dev rS-rR-eth"),  # S to P via R
        ("S", "ip route add 10.4.0.0/24 via 10.102.0.2 dev rS-rQ-eth"),  # S to T via Q
        ("S", "ip route add 10.104.0.0/24 via 10.102.0.2 dev rS-rQ-eth"),  # S to T via Q

        ("T", "ip route add 10.1.0.0/24 via 10.104.0.2 dev rT-rQ-eth"),  # T to Q
        ("T", "ip route add 10.6.0.0/24 via 10.109.0.1 dev rT-rV-eth"),  # T to V
        ("T", "ip route add 10.3.0.0/24 via 10.104.0.2 dev rT-rQ-eth"),  # T to S via Q
        ("T", "ip route add 10.102.0.0/24 via 10.104.0.2 dev rT-rQ-eth"),  # T to S via Q
        ("T", "ip route add 10.0.0.0/24 via 10.104.0.2 dev rT-rQ-eth"),  # T to P via Q
        ("T", "ip route add 10.100.0.0/24 via 10.104.0.2 dev rT-rQ-eth"),  # T to P via Q
        ("T", "ip route add 10.2.0.0/24 via 10.104.0.2 dev rT-rQ-eth"),  # T to R via P
        ("T", "ip route add 10.101.0.0/24 via 10.104.0.2 dev rT-rQ-eth"),  # T to R via P
        ("T", "ip route add 10.5.0.0/24 via 10.109.0.1 dev rT-rV-eth"),  # T to U via V
        ("T", "ip route add 10.107.0.0/24 via 10.109.0.1 dev rT-rV-eth"),  # T to U via V

        ("U", "ip route add 10.3.0.0/24 via 10.105.0.2 dev rU-rS-eth"),  # U to S
        ("U", "ip route add 10.2.0.0/24 via 10.106.0.2 dev rU-rR-eth"),  # U to R
        ("U", "ip route add 10.6.0.0/24 via 10.107.0.2 dev rU-rV-eth"),  # U to V
        ("U", "ip route add 10.0.0.0/24 via 10.106.0.2 dev rU-rR-eth"),  # U to P via R
        ("U", "ip route add 10.101.0.0/24 via 10.106.0.2 dev rU-rR-eth"),  # U to P via R
        ("U", "ip route add 10.1.0.0/24 via 10.105.0.2 dev rU-rS-eth"),  # U to Q via S
        ("U", "ip route add 10.102.0.0/24 via 10.105.0.2 dev rU-rS-eth"),  # U to Q via S
        ("U", "ip route add 10.4.0.0/24 via 10.107.0.2 dev rU-rV-eth"),  # U to T via V
        ("U", "ip route add 10.109.0.0/24 via 10.107.0.2 dev rU-rV-eth"),  # U to T via V

        ("V", "ip route add 10.5.0.0/24 via 10.107.0.1 dev rV-rU-eth"),  # V to U
        ("V", "ip route add 10.4.0.0/24 via 10.109.0.2 dev rV-rT-eth"),  # V to T
        ("V", "ip route add 10.3.0.0/24 via 10.108.0.2 dev rV-rS-eth"),  # V to S
        ("V", "ip route add 10.1.0.0/24 via 10.110.0.2 dev rV-rQ-eth"),  # V to Q
        ("V", "ip route add 10.2.0.0/24 via 10.107.0.1 dev rV-rU-eth"),  # V to R via U
        ("V", "ip route add 10.106.0.0/24 via 10.107.0.1 dev rV-rU-eth"),  # V to R via U
        ("V", "ip route add 10.0.0.0/24 via 10.110.0.2 dev rV-rQ-eth"),  # V to P via Q
        ("V", "ip route add 10.100.0.0/24 via 10.110.0.2 dev rV-rQ-eth"),  # V to P via Q
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