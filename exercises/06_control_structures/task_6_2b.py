# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

The message "Invalid IP address" should be printed only once,
even if several chacks are not passed.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip_local_b = [255, 255, 255, 255]
ip_unassigned = [0, 0, 0, 0]


while True:
    ip = input("Enter an IP address in the format 10.0.1.1: ")
    ip_correct = False
    ip_s = ip.split('.')
    if len(ip_s) == 4:
        ip_correct = True
        for i in ip_s:
            if not i.isdigit():
                ip_correct = False
                break
            oct = int(i)
            if oct < 0 and oct > 255:
                ip_correct = False
                break
        if ip_correct == False:
            ip = input("Invalid IP. Enter an IP address in the format 10.0.1.1: ")
        else:
            if ip_s[0] in range(1, 223):
                print ('unicast')
            elif ip_s[0] in range(224, 239):
                print ('multicast')
            elif ip_s == ip_local_b:
                print ('local broadcast')
            elif ip_s == ip_unassigned:
                print ('unassigned')
            else:
                print ('unused')
            break
    else:
        ip = input("Invalid IP. Enter an IP address in the format 10.0.1.1: ")