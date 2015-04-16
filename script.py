#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

hsep = "-"
vsep = "|"
olap = "+"

# Text alignment:
# 0 = center
# 1 = left
# 2 = right
mode = 0
lines = """
Think before you type. Sincerly, your Brain.
"""

rows, columns = os.popen('stty size', 'r').read().split()
rows    = int(rows)
columns = int(columns)
os.system("clear") # clears console, you can remove this if you like

print(olap + hsep * (columns - 2) + olap)

for line in lines.split("\n"):
    if mode == 0:
        print(vsep + str(line).center(columns - len(vsep) * 2) + vsep)
    elif mode == 2:
        print(vsep + str(line).rjust(columns - len(vsep) * 2) + vsep)
    else:
        print(vsep + str(line).ljust(columns - len(vsep) * 2) + vsep)

print(olap + hsep * (columns - 2) + olap)
