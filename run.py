# -*- coding: utf-8 -*-
import cPickle
import theano
from lab import *

import argparse

color2index = cPickle.load(open('pkl/char2id.pkl'))
function = cPickle.load(open('pkl/function.pkl'))

def char2rgb(function, color2index, word):
    characters = set(color2index.keys())

    chars_encoded, err = [], False

    for c in list(word):
        if c in characters:
            chars_encoded.append(color2index[c])
        else:
            chars_encoded.append(color2index['-'])
            err = True 

    pred = function([chars_encoded])
    rgb  = lab2rgb(pred)
    return rgb, err



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Give Me Conll data.')
    parser.add_argument('-f', type=str, help='provide text file')
    parser.add_argument('-ht', type=int, default=0, help='specify ourput wormat. text: 0, html: 1')
    args = parser.parse_args()

    if not args.ht:
        print 'word, R, G, B, OOV'

    for line in open(args.f):
        word = line.strip()
        if len(word) == 0: continue

        [r,g,b], err  = char2rgb(function, color2index, word) 

        if args.ht:
            if err:
                print "<p><span style='font-weight: bold; color:rgb({},{},{})'>{}</span> (There were out-of-character)</p>".format(r, g, b, word) 
            else:
                print "<p style='font-weight: bold; color:rgb({},{},{})'>{}</p>".format(r, g, b, word) 
        else:
            print "{},{},{},{},{}".format(word, r, g, b, err) 
