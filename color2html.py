# -*- coding: utf-8 -*-
from lab import *
import argparse

parser = argparse.ArgumentParser(description='Give Me Conll data.')
parser.add_argument('-f', type=str, help='provide text file, examples are in example_result/rgb_example.csv')
parser.add_argument('-lab', type=int, default=0, help='if you feed rgb color set 0, lab color set 1')
args = parser.parse_args()

for i, line in enumerate(open(args.f)):
    if i == 0: continue
    line = line.strip().split(',')
    word = line[0]
    
    if args.lab == 0:
        r,g,b = map(int, line[1:4])
        print "<p style='font-weight: bold; color:rgb({},{},{})'>{} </p>".format(r, g, b, word) 
    else:
        l,a,b = lab2rgb(map(float, line[1:4]))
        print "<p style='font-weight: bold; color:rgb({},{},{})'>{} </p>".format(l, a, b, word) 
