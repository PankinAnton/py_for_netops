# -*- coding: utf-8 -*-
"""
Task 9.2

Create generate_trunk_config function that generates configuration
for access ports.

The function expects arguments:

- intf_vlan_mapping: expects a dictionary with interface-VLAN mapping:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: expects trunk port configuration template as command list
  (trunk_mode_template list)

The function should return a list of commands with configuration based on
the specified ports and trunk_mode_template.

Check the operation of the function using the example of the trunk_config
dictionary and a list of commands trunk_mode_template.
If the previous check was successful, check the function again
on the trunk_config_2 dictionary and make sure that the final list contains
the correct numbers interfaces and vlans.


An example of a final list (each string is written on a new line for readability):
[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]


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

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}

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
    return lines

print(generate_trunk_config(trunk_config, trunk_mode_template))
print(generate_trunk_config(trunk_config_2, trunk_mode_template))

