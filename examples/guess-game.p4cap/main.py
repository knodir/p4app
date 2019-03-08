import random

from p4app import P4Mininet
from mininet.topo import SingleSwitchTopo

topo = SingleSwitchTopo(2)
net = P4Mininet(program='registers.p4', topo=topo)
net.start()

h1 = net.get('h1')
h2 = net.get('h2')

n = random.randint(1, 9)

out = h1.cmd('./send.py 10.0.0.2 foo %d' % n)
print('wrote number %d to switch dataplane' % n)
print('Pretend that you do not know that and try to guess it. Start.')
assert int(out) == n

guess = int(raw_input("Enter an integer from 1 to 9: "))

while n != "guess":
    str_to_send = './send.py 10.0.0.2 bar %d' % guess
    print('str_to_send = %s' % str_to_send)
    out = h1.cmd(str_to_send)
    # print('out = %s' % out)
    outcome = int(out.strip())
    print('outcome = %s' % outcome)
    if outcome == 0:
        print('Congrats!')
        break
    elif outcome == 1:
        print('Hidden number is smaller')
    else:
        print('Hidden number is larger')
    
    guess = int(raw_input("Enter an integer from 1 to 9: "))

print('Game Over!')

from mininet.cli import CLI
CLI(net)

print "OK"
