# -*- coding: utf-8 -*-
"""
Task 6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address.
An IP address is considered correct if it:
    - consists of 4 numbers (not letters or other symbols)
    - numbers are separated by a dot
    - every number in the range from 0 to 255

If the IP address is incorrect, print the message: 'Invalid IP address'

The message "Invalid IP address" should be printed only once,
even if several points above are not met.

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
            print("Invalid IP")
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
        print("Invalid IP")
        break


