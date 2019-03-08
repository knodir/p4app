#!/usr/bin/env python

import sys
import socket
import struct

UDP_PORT = 1234
OP_FOO   = 0
OP_BAR   = 1

#hdr = struct.Struct('!B B 4s') # op_type idx [val]
hdr = struct.Struct('!B B') # op_type [val]

if len(sys.argv) < 4:
    print "Usage: %s HOST FOO|BAR [VALUE]" % sys.argv[0]
    sys.exit(1)

host = sys.argv[1]
foo_or_bar = sys.argv[2].lower()[:1]
val = int(sys.argv[3])

addr = (host, UDP_PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if foo_or_bar == 'f': # foo
    req = hdr.pack(OP_FOO, val)
else: # bar
    req = hdr.pack(OP_BAR, val)

s.sendto(req, addr)
res, addr2 = s.recvfrom(1024)

op_type, val2 = hdr.unpack(res)

print val2
