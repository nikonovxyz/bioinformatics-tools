#!/usr/local/bin/python3
import sys
import pandas as pd
import numpy as np
multiply = True
# Manual
if len(sys.argv) == 2:
    multiply = False
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        man = open(__file__[:-17]+"README")
        print(*man)
        man.close()
        sys.exit()
# Multiply file opener
infiles = dict()
filenames = {}
if len(sys.argv) == 1:
    filenames = input().split(" ")
else:
    filenames = sys.argv[1:]
if len(filenames) > 1:
    multiply = True
else:
    multiply = False
for name in filenames:
    if name.endswith(".csv"):
        try:
            infiles[name] = pd.read_csv(name, sep=';')
        except FileNotFoundError:
            print(__file__.split('/')[-1][:-3], ": ", name,
                  ": no such csv file", sep='')
            sys.exit(0)
        except Exception:
            print(__file__.split('/')[-1][:-3], ": ", name,
                  ": unable to open csv file", sep='')
            sys.exit(1)
    elif name.endswith(".xls") or name.endswith(".xlsx"):
        try:
            infiles[name] = pd.read_excel(name)
        except FileNotFoundError:
            print(__file__.split('/')[-1][:-3], ": ", name,
                  ": no such excel file", sep='')
            sys.exit(2)
        except Exception:
            print(__file__.split('/')[-1][:-3], ": ", name,
                  ": unable to open excel file", sep='')
            sys.exit(3)
    else:
        print(__file__.split('/')[-1][:-3], ": ", name,
              """: filenmae can end with ".csv", ".xls" or ".xlsx" only""",
              sep='')
# Program
for name, infile in infiles.items():
    if multiply:
        print("\n", name, ":", sep='')
    infile[''] = np.zeros
    print(infile.groupby(["# feature", "class"])[['']].count())
