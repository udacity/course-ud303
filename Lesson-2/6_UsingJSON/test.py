#!/usr/bin/env python3
#
# Test script for UINames.py

import sys, re, traceback

try:
    import requests
except ImportError:
    print("You need to install the requests module.")
    sys.exit(1)

try:
    import UINames
except ImportError:
    print("Couldn't find your UINames.py code.")
    sys.exit(1)

try:
    s = UINames.SampleRecord()
except IndexError:
    traceback.print_exc()
    print()
    print("Make sure you're providing the three JSON fields in SampleRecord!")
    sys.exit(1)

pat = re.compile('My name is (\S+) (\S+) and the PIN on my card is (\S+).')
m = pat.match(s)

if not m:
    print("Output didn't look quite right:")
    print(s)
    sys.exit(1)

print("Tests pass!  Here are the fields I found in your code's output:")
print("Name:", m.group(1))
print("Surname:", m.group(2))
print("PIN:", m.group(3))

