# -*- coding: utf-8 -*-
"""
Task 9.3a

Make a copy of the code from the task 9.3.

Add this functionality: add support for configuration when the port is in VLAN 1
and the access port setting looks like this:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

In this case, information should be added to the dictionary that the port in VLAN 1
Dictionary example:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw2.txt file.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

def get_int_vlan_map(config_filenam):
    access_ports = {}
    trunk_ports = {}
    with open(config_filenam) as f:
        interface = None
        is_access_mode = False
        vlan_assigned = False
        for line in f:
            line = line.strip()
            if line.startswith('interface'):
                if is_access_mode and not vlan_assigned:
                    access_ports[interface] = 1
                interface = line.split()[-1]
                is_access_mode = False
                vlan_assigned = False
            elif "switchport mode access" in line:
                is_access_mode = True
            elif 'switchport access vlan' in line:
                Vlan = int(line.split()[-1])
                access_ports[interface] = Vlan
                vlan_assigned = True
            elif 'switchport trunk allowed vlan' in line:
                vlans = line.split()[-1]
                vlan_list = [int(vlan) for vlan in vlans.split(',')]
                trunk_ports[interface] = vlan_list
            if is_access_mode and not vlan_assigned:
                access_ports[interface] = 1

    return access_ports, trunk_ports

access, trunk = get_int_vlan_map('/Users/antonpankin/Documents/GitHub/py_for_netops/exercises/09_functions/config_sw2.txt')
print("Access Ports:", access)
print("Trunk Ports:", trunk)
