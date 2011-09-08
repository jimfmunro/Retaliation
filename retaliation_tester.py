# retaliation_tester.py
# useful for debugging your retaliation.py settings and making sure things work
#
# Simple UDP sender code via: http://wiki.python.org/moin/UdpCommunication
# 
# This works against both Hudson and Jenkins, same stuff.

import socket

UDP_IP="localhost"
UDP_PORT=22222
MESSAGE = '{"name":"JobName","url":"JobUrl","build":{"number":1,"phase":"FINISHED","status":"FAILED","url":"job/project/5","fullUrl":"http://ci.jenkins.org/job/project/5"}}'

print "Sending to UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print "Sample Hudson Notification: ", MESSAGE

sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
sock.sendto( MESSAGE, (UDP_IP, UDP_PORT) )
