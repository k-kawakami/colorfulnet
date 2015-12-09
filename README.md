# color_turing_test
Enjoy colorful word representation!! 

## Dependencies

- [Theano 7.0](http://deeplearning.net/software/theano/install.html)
- A recent version of NumPy and SciPy
- Beautiful Soup, Requests (for Web demo)

If you use virtualenv

```bash
    cd ~/
    virtualenv color-test
    source ~/color-test/bin/activate
    cd /path/to/color_turing_test
    pip install -r requirements.txt
```

## Getting Started
Provide text file which contains list of words (-f). To visualize color, use html output with -ht = 1.

```bash 
    python run.py -f example_data/example.txt -ht 1 > example.html
```

## Character Base Model
If you want to see what's going on in character base model, try to look colors character by character.

```bash 
    python run.py -f example_data/example.txt -ht 1 -c 1 > example.html
```

## Colorful document
The code download an article and replace Title and paragraphs with colorful string. Since the crawler is not carefully written, it will fail for some websites.

If you want to have some examples, please check example_result folder.

```bash
    python web.py -f http://greatist.com/health/super-berry-quinoa-salad > example_result/recipie.html 
```

## OOV
The code produce color even your input have characters which are not in training data.
It replace unknown character with '-' and predict color for it.

## Update
The model will be updated later.
