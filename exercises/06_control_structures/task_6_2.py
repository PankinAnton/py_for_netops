# -*- coding: utf-8 -*-
"""
Task 6.2

Prompt the user to enter an IP address in the format 10.0.1.1
Depending on the type of address (described below), print to the stdout:
    'unicast' - if the first byte is in the range 1-223
    'multicast' - if the first byte is in the range 224-239
    'local broadcast' - if the IP address is 255.255.255.255
    'unassigned' - if the IP address is 0.0.0.0
    'unused' - in all other cases

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip = input("Enter an IP address in the format 10.0.1.1: ")
ip_s = ip.split('.')
ip_b = []
for i in ip_s:
    ip_b.append(int(i))
ip_local_b = [255, 255, 255, 255]
ip_unassigned = [0, 0, 0, 0]

if ip_b[0] in range(1, 223):
    print ('unicast')
elif ip_b[0] in range(224, 239):
    print ('multicast')
elif ip_b == ip_local_b:
    print ('local broadcast')
elif ip_b == ip_unassigned:
    print ('unassigned')
else:
    print ('unused')

