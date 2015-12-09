# -*- coding: utf-8 -*-
import cPickle
import theano
from lab import *


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
    lab  = map(float, pred) 
    rgb  = lab2rgb(pred)
    return rgb, lab, err



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Give Me Conll data.')
    parser.add_argument('-f', type=str, help='provide text file')
    parser.add_argument('-ht', type=int, default=0, help='specify ourput wormat. text: 0, html: 1')
    parser.add_argument('-l',  type=int, default=0, help='to get lab result, set 1')
    parser.add_argument('-c',  type=int, default=0, help='to run character by character set 1')
    args = parser.parse_args()

    if not args.ht:
        print 'word, R, G, B, OOV'

    if args.l == 1:
        assert args.ht == 0, 'Lab output is anly available for text output, set -ht = 0'

    for line in open(args.f):
        word = line.strip()
        if len(word) == 0: continue

        if args.c:
            words = [ word[:i] for i in range(1, len(word)+1) ]
        else:
            words = [word]

        for word in words:
            rgb, lab, err  = char2rgb(function, color2index, word) 

            if args.ht:
                if err:
                    print "<span><span style='font-weight: bold; color:rgb({},{},{})'>{}</span> (There were out-of-character)</span>".format(rgb[0], rgb[1], rgb[2], word) 
                else:
                    print "<span style='font-weight: bold; color:rgb({},{},{})'>{} </span>".format(rgb[0], rgb[1], rgb[2], word) 
            else:
                if args.l:
                    print "{},{},{},{},{}".format(word, lab[0], lab[1], lab[2], err) 
                else:
                    print "{},{},{},{},{}".format(word, rgb[0], rgb[1], rgb[2], err) 
