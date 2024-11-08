# -*- coding: utf-8 -*-
"""
Task 7.2b

Make a copy of the code from the task 7.2a.
Add this functionality: instead of printing to stdout,
the script should write the resulting lines to a file.

File names must be passed as arguments to the script:
  1. name of the source configuration file
  2. name of the destination configuration file

In this case, the lines that are contained in the ignore list and lines
that start with ! must be filtered.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""


s = input("Name of the source configuration file:")
d = input("Name of the destination configuration file:")
ignore = ["duplex", "alias", "configuration"]

with open(s, 'r', encoding="utf-8")as s, open(d, 'w')as d:
    for line in s:
        lines = line.strip('!').strip().strip("\n")
        if lines != '' and not any(word in lines for word in ignore):
            d.write(lines + '\n')
