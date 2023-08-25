# -*- coding: utf-8 -*-
"""
Task 5.1d

Modify the script from task 5.1c so that, when requesting a parameter,
the user could enter the parameter name in any case.

An example of script execution:
$ python task_5_1d.py
Enter device name: r1
Enter parameter name (ios, model, vendor, location, ip): IOS
15.4


Restriction: You cannot modify the london_co dictionary.

All tasks must be completed using only the topics covered. That is, this task can be
solved without using the if condition.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}
user_input_name = input("Enter device name:")
user_input_dev = london_co[user_input_name]
dev_keys = ', '.join(user_input_dev.keys())
user_input_param = input("Enter parameter name (" + (dev_keys)+"):").lower()
user_input_param_check = user_input_dev.get(user_input_param, "There is no such parameter")
print(user_input_param_check)