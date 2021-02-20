#!/usr/local/bin/python3
import sys
# Options
full_names = {"all": 'a', "gc": 'c', "length": 'l', "partial": 'p',
              "frequency": 'f', "number": 'n', "help": 'h'}
options = {'a': False, 'c': False, 'f': False, 'h': False, 'l': False,
           'p': False, 'n': False}
arg = 1
for word in sys.argv[1:]:
    if word.startswith("-"):
        if word[1] == "-":
            if word[2:] in full_names.keys():
                options[full_names[word[2:]]] = True
                arg += 1
            else:
                print(__file__.split('/')[-1][:-3],
                      ": illegal option -- ", word[2:], sep='')
                sys.exit(0)
        else:
            for char in word[1:]:
                if char in options.keys():
                    options[char] = True
                else:
                    print(__file__.split('/')[-1][:-3],
                          ": illegal option -- ", word[1:], sep='')
                    sys.exit(1)
            arg += 1
    else:
        break
# Manual
if options["h"]:
    man = open(__file__[:-18]+"README")
    print(*man)
    man.close()
    sys.exit()
# Multiply file opener
isnames = True
infiles = dict()
if len(sys.argv) == arg:
    isnames = False
    filenames = input().split(" ")
    for name in filenames:
        infiles[name] = open(name)
else:
    for i in range(arg, len(sys.argv)):
        try:
            infiles[sys.argv[i]] = open(sys.argv[i])
        except Exception:
            print(__file__.split('/')[-1][:-3], ": ", sys.argv[i],
                  ": no such file", sep='')
            sys.exit(2)
# Program
if len(infiles) != 1:
    multiply = True
else:
    multiply = False
for name, infile in infiles.items():
    if multiply:
        print("\n", name, ":")
    total = 0
    gc_dict = dict()
    parts = dict()
    for line in infile:
        if line.startswith(">"):
            part = line[1:]
            parts[part] = 0
        else:
            for char in line.strip():
                parts[part] += 1
                total += 1
                if char in gc_dict.keys():
                    gc_dict[char] += 1
                else:
                    gc_dict[char] = 1
    gc = 0
    if not options["n"] or options["f"] or options["a"]:
        for key in sorted(gc_dict.keys()):
            if not options["f"] and not options["a"]:
                print(key, ": ", gc_dict[key], sep="")
            elif options["n"] and not options["a"]:
                print(key, ": ", gc_dict[key]/total, sep="")
            else:
                print(key, ": ", gc_dict[key], " ", gc_dict[key]/total, sep="")
        print("\n")
    for key in sorted(gc_dict.keys()):
        if key in ["G", "g", "C", "c"]:
            gc += gc_dict[key]
    if options["p"] or options["a"]:
        for key, value in parts.items():
            print(key, ": ", value, sep='')
        print("\n")
    if options["l"] or options["a"]:
        print("total length:", total)
    if options["c"] or options["a"]:
        print("GC-content:", gc/total)
    infile.close()
