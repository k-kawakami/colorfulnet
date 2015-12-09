# color_turing_test
Enjoy colorful word representation!! 

## Dependencies

- [Theano 7.0](http://deeplearning.net/software/theano/install.html)
- A recent version of NumPy and SciPy

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

## OOV
The code produce color even your input have characters which are not in training data.
It replace unknown character with '-' and predict color for it.

## Update
The model will be updated later.
