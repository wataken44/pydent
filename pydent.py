#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pydent.py


"""

import os
import re
import sys

def main():
    ifn = sys.argv[1]

    ifp = open(ifn)

    ofp = sys.stdout
    if len(sys.argv) == 3:
        ofp = open(sys.argv[2], "w")
        
    reindent(ifp, ofp)
        
    ifp.close()
    if ofp != sys.stdout:
        ofp.close()

def reindent(ifp, ofp):
    prev_spaces = 0
    prev_level = 0

    ptn_spaces = re.compile('^(\s*)')
    ptn_empty = re.compile('^(\s*)$')
    
    for line in ifp.readlines():
        s = line.rstrip()
        mo = ptn_empty.match(s)
        if mo:
            ofp.write("\n")
            continue
        mo = ptn_spaces.match(s)
        if mo:
            spaces = len(mo.group(1))
            level = prev_level
            if spaces > prev_spaces:
                level += 1
            elif spaces < prev_spaces:
                level = max(level - 1, 0)
            ofp.write("    " * level + s.lstrip() + "\n")
            prev_spaces = spaces
            prev_level = level
    
if __name__ == "__main__":
    main()
