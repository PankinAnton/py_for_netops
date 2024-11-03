# -*- coding: utf-8 -*-
"""
Task 9.3

Create a get_int_vlan_map function that handles the switch configuration
file and returns a tuple of two dictionaries:

* a dictionary of ports in access mode, where the keys are port numbers,
  and the access VLAN values (numbers):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* a dictionary of ports in trunk mode, where the keys are port numbers,
  and the values are the list of allowed VLANs (list of numbers):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw1.txt file.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
def get_int_vlan_map(config_filenam):
    access_ports = {}
    trunk_ports = {}
    with open(config_filenam) as f:
        interface = None
        for line in f:
            line = line.strip()
            if line.startswith('interface'):
                interface = line.split()[-1]
            elif 'switchport access vlan' in line:
                Vlan = int(line.split()[-1])
                access_ports[interface] = Vlan
            elif 'switchport trunk allowed vlan' in line:
                vlans = line.split()[-1]
                vlan_list = [int(vlan) for vlan in vlans.split(',')]
                trunk_ports[interface] = vlan_list

    return access_ports, trunk_ports

access, trunk = get_int_vlan_map('/Users/antonpankin/Documents/GitHub/py_for_netops/exercises/09_functions/config_sw1.txt')
print("Access Ports:", access)
print("Trunk Ports:", trunk)