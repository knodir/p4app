import random

from p4app import P4Mininet
from mininet.topo import SingleSwitchTopo

topo = SingleSwitchTopo(2)
net = P4Mininet(program='registers.p4', topo=topo)
net.start()

h1 = net.get('h1')
h2 = net.get('h2')

out = h1.cmd('./send.py 10.0.0.2 foo fooo')
print('sent a packet with payload *fooo* and received this: %s' % out)
assert out.strip() == "fooo"

out = h1.cmd('./send.py 10.0.0.2 bar barr')
print('sent a packet with payload *barr* and received this: %s' % out)
assert out.strip() == "fooo"

from mininet.cli import CLI
CLI(net)

print "OK"
