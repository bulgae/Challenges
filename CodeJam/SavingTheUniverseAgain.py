#!/usr/bin/env python

from __future__ import print_function
import sys

def main():
    filename = "SavingTheUniverseAgain"
    fin = open(filename+".in", 'rU')
    fout = open(filename+".out", "w") # Use "a" instead of "w" to append to file
    cases = int(fin.readline())
    

    for case in range(1, cases + 1):
        numItems = str(fin.readline())
        itemsList = map(str, fin.readline().split())
        
        maxDamage = int(itemsList[0])
        inst = [c for c in itemsList[1]]
        print("instr = " + inst)
        print("maxDamage = " +maxDamage)

           
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()