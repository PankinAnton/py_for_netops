# -*- coding: utf-8 -*-
"""
Task 4.6

Process the ospf_route string and print the information to the stdout as follows:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route = ospf_route.replace(",", " ").replace("[", "").replace("]", "")
ospf_route = ospf_route.split()
print_format = "\n{:25} {}" * 5
print(print_format.format(
"Prefix",                ospf_route[0],
"AD/Metric",             ospf_route[1],
"Next-Hop",              ospf_route[3],
"Last update",           ospf_route[4],
"Outbound Interface",    ospf_route[5]))