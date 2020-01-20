#!/usr/bin/env python3
#FFSS: FASTA FILE SPECIE SEPARATOR
#This pyhon software will look for a determinated specie in your fasta file and add it to another folder
#Version 1.0 - 10th Dezember, 2019
#
# Copyright © 2019 Lucas Jose Luduverio Pizauro
#
# FFSS is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# FFSS is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
# License for more details.

import os
import argparse

def run(input, specie, new_dir):
    original_file = open(input)
    header = original_file.readline()
    if specie in header:
        with open(input, "rt") as old_file, open(new_dir + '/' + input , "wt") as new_file:
            for line in old_file:
                new_file.write(line)
        
    else:
        print("not found")
    
    
def main():
    parser=argparse.ArgumentParser(description="change the name of a fasta file to its first line")
    parser.add_argument("-in",help="fasta input file" ,dest="input", nargs='+', required=True)
    parser.add_argument("-nd", help="director for the exit file", dest="new_dir",)
    parser.add_argument("-sp", help="specie to be looked for", dest="s_input", required=True)
    args=parser.parse_args()

    if args.new_dir:
        os.mkdir(args.new_dir)
        new_dir = args.new_dir
    else:
        new_dir = '.'
    if args.s_input:
        s_input = args.s_input

        
    for file in args.input:
        run(file, s_input, new_dir)

if __name__=="__main__":
    main()
