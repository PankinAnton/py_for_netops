# -*- coding: utf-8 -*-
"""
Task 7.3b

Make a copy of the code from the task 7.3a.

Add this functionality:
- Ask the user to enter the VLAN number.
- Print information only for the specified VLAN.

Output example:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
uvlan = input("Enter VLAN number:")
result = {}

with open('exercises\\07_files\\CAM_table.txt') as f:
    for line in f:
        line = line.split()
        if line and line[0][1].isdigit() and line[0] == uvlan:
            Vlan, address, types, port, *other=line
            result = '{:10}{:20}{:}'.format(Vlan, address, port)
            print(result)
