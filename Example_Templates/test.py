#!/usr/bin/env python

from __future__ import print_function
import sys

def main():
    filename = "test"
    f = open(filename+".in", 'rU')
    fout = open(filename+".out", "w") # Use "a" instead of "w" to append to file
    cases = int(f.readline())

    for case in range(1, cases + 1):
        credit = int(f.readline())
        numItems = int(f.readline())
        itemsList = map(int, f.readline().split())

        itemsDict = {}
        for i in range(1, numItems + 1):
            itemsDict[itemsList[i - 1]] = i

        for i in range(numItems):
            key = credit - itemsList[i]
            if key in itemsDict and itemsDict[key] != i + 1:
                fout.write("Case #" + str(case) + ": " + str(i + 1) + " " + str(itemsDict[key])+"\n")
                print("Case #" + str(case) + ": " + str(i + 1) + " " + str(itemsDict[key]))
                break

    f.close()
    fout.close()

if __name__ == '__main__':
    main()