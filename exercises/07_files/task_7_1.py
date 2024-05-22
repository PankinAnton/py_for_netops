# -*- coding: utf-8 -*-
"""
Task 7.1

Process the lines from the ospf.txt file and print information for each line
in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

result = {}
route_template = {
"Prefix                "
"AD/Metric             "
"Next-Hop              "
"Last update           "
"Outbound Interface    "
}

with open('exercises\\07_files\ospf.txt', 'r') as f:
    for ospf_route in f:
        ospf_route = ospf_route.replace(",", " ").replace("[", "").replace("]", "")
        ospf_route = ospf_route.split()
        print_format = "\n{:25} {}" * 5
        print(print_format.format(
        "Prefix",                ospf_route[0],
        "AD/Metric",             ospf_route[1],
        "Next-Hop",              ospf_route[3],
        "Last update",           ospf_route[4],
        "Outbound Interface",    ospf_route[5]))
