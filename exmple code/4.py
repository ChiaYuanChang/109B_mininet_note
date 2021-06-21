from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link,TCLink
 
if '__main__' == __name__:
  net = Mininet(link=TCLink)
  h1 = net.addHost('h1')
  h2 = net.addHost('h2')
  r1 = net.addHost('r1')
  r2 = net.addHost('r2')
  Link(h1, r1)
  Link(h2, r2)
  Link(r1, r2)
  net.build()
  h1.cmd("ifconfig h1-eth0 0")
  h1.cmd("ip addr add 192.168.1.1/24 brd + dev h1-eth0")
  h1.cmd("ip route add default via 192.168.1.254")

  h2.cmd("ifconfig h2-eth0 0")
  h2.cmd("ip addr add 192.168.2.1/24 brd + dev h2-eth0")
  h2.cmd("ip route add default via 192.168.2.254")

  r1.cmd("ifconfig r1-eth0 0")
  r1.cmd("ifconfig r1-eth1 0")
  r1.cmd("ip addr add 192.168.1.254/24 brd + dev r1-eth0")#catch
  r1.cmd("ip addr add 192.168.87.1/24 brd + dev r1-eth1")
  r1.cmd("ip addr add 192.168.87.8/24 brd + dev r1-eth2")
  r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")#open routing
  r1.cmd("ip route add 192.168.2.0/24 via 192.168.87.2")

  r2.cmd("ifconfig r2-eth0 0")
  r2.cmd("ifconfig r2-eth1 0")
  r2.cmd("ip addr add 192.168.2.254/24 brd + dev r2-eth0")#catch
  r2.cmd("ip addr add 192.168.87.2/24 brd + dev r2-eth1")
  r2.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")#open routing
  r2.cmd("ip route add 192.168.1.0/24 via 192.168.87.1")

  CLI(net)
  net.stop()