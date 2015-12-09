# -*- coding: utf-8 -*-
import cPickle
import theano
from lab import *

import requests
from bs4 import BeautifulSoup

color2index = cPickle.load(open('pkl/char2id.pkl'))
function = cPickle.load(open('pkl/function.pkl'))

def get_html(url):
    html = None
    try:
        header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
        r = requests.get(url, headers=header)
        if  r.status_code == 200:
            html = r.text
    except:
        pass
    return html

def char2html(function, color2index, word):
    # Take English word, return html
    characters = set(color2index.keys())
    chars_encoded, err = [], False
    cleaned_word = ''
    for c in list(word):
        if c in characters:
            chars_encoded.append(color2index[c])
            cleaned_word += c
        else:
            chars_encoded.append(color2index['-'])
            err = True 

    pred = function([chars_encoded])
    r,g,b  = lab2rgb(pred)

    html = "<span style='font-weight: bold; color:rgb({},{},{})'>{} </span>".format(r, g, b, cleaned_word) 
    return html

def text2html(function, color2index, text):
    text = text.encode('utf-8')
    return map(lambda x: char2html(function, color2index, x), text.split())

def replace(target, color_html):
    target.string = ''
    target.append(BeautifulSoup(color_html, "html.parser"))
    return target

#url = 'http://greatist.com/eat/healthy-mug-recipes' 
#url = 'http://greatist.com/health/super-berry-quinoa-salad'
#url = 'http://www.nytimes.com/2015/12/10/opinion/trumps-anti-muslim-plan-is-awful-and-constitutional.html?action=click&pgtype=Homepage&clickSource=story-heading&module=opinion-c-col-left-region&region=opinion-c-col-left-region&WT.nav=opinion-c-col-left-region'

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Web text to color')
    parser.add_argument('-f', type=str, default='http://greatist.com/health/super-berry-quinoa-salad', help='provide url')

    args = parser.parse_args()

    html = get_html(args.f)
    soup = BeautifulSoup(html, "html.parser") 


    # Get contents
    title = soup.find('h1') 
    links = soup.find('a') 
    ps    = soup.findAll('p')
    lis   = soup.findAll('li')

    print '<p> cite:: {}</p>'.format(args.f)
    ### Replace Title
    if title is not None:
        try:
            title_text = text2html(function, color2index, title.text)
            title = replace(title, ' '.join(title_text))
        except:
            print '<p>Ignore error in h1 tag</p>'

    ### Replace Title
    if links is not None:
        for link in links:
            try:
                link_text = text2html(function, color2index, link.text)
                link = replace(link, ' '.join(link_text))
            except:
                print '<p>Ignore error in a tag</p>'

    ### Replace <p>
    if ps is not None:
        for p in ps:
            try:
                p_text = text2html(function, color2index, p.text)
                p = replace(p, ' '.join(p_text))
            except:
                print '<p>Ignore error in p tag</p>'

    ### Replace <li>
    if lis is not None:
        for li in lis:
            try:
                li_text = text2html(function, color2index, li.text)
                li = replace(li, ' '.join(li_text))
            except:
                print '<p>Ignore error in li tag</li>'

    print soup.prettify().encode('UTF-8')
