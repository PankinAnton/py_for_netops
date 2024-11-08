# -*- coding: utf-8 -*-
"""
Task 7.2a

Make a copy of the code from the task 7.2.

Add this functionality: The script should not print to the stdout commands,
which contain words from the ignore list.

The script should also not print lines that begin with !.

Check the script on the config_sw1.txt configuration file.
The filename is passed as an argument to the script.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

f = input("Введите имя файла:")
ignore = ["duplex", "alias", "configuration"]

with open(f, 'r', encoding="utf-8")as f:
    for line in f:
        lines = line.strip('!').strip().strip("\n")
        if lines != '' and not any(word in lines for word in ignore):
            print(lines)
