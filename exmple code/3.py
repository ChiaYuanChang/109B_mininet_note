from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link,TCLink

if '__main__' == __name__:
    net = Mininet(link=TCLink)
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    r = net.addHost('r')
    Link(h1, r)
    Link(h2, r)
    net.build()
    h1.cmd("ifconfig h1-eth0 0")
    h1.cmd("ip addr add 192.168.1.1/24 brd + dev h1-eth0")
    h1.cmd("ip route add default via 192.168.1.254")
    h2.cmd("ifconfig h2-eth0 0")
    h2.cmd("ip addr add 192.168.2.1/24 brd + dev h2-eth0")
    h2.cmd("ip route add default via 192.168.2.254")
    r.cmd("ifconfig r-eth0 0")
    r.cmd("ifconfig r-eth1 0")
    r.cmd("ip addr add 192.168.1.254/24 brd + dev r-eth0")
    r.cmd("ip addr add 192.168.2.254/24 brd + dev r-eth1")
    r.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    CLI(net)
    net.stop()