# -*- coding: utf-8 -*-
"""
Task 9.2a

Make a copy of the code from the task 9.2.

Change the function so that it returns a dictionary instead of a list of commands:
- keys: interface names, like 'FastEthernet0/1'
- values: the list of commands that you need execute on this interface

Check the operation of the function using the example of the trunk_config
dictionary and the trunk_mode_template template.

An example of a final dict (each string is written on a new line for readability):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}
interfaces = {}
def generate_trunk_config(intf_vlan_mapping, trunk_template, psecurity=None):
    lines = []
    for int, vlan in intf_vlan_mapping.items():
        lines.append(f"interface {int}")
        for command in trunk_template:
            if command.endswith("vlan"):
                vlans_list = ','.join([str(vlan) for vlan in vlan])
                lines.append(f"{command} {vlans_list}")
            else:
                lines.append(command)
        if psecurity:
            for pscommand in psecurity:
                lines.append(pscommand)
        interfaces[int] = lines
    return interfaces

print(generate_trunk_config(trunk_config, trunk_mode_template))