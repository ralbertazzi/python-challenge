# http://www.pythonchallenge.com/pc/def/linkedlist.php

from utils.web import get_url
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--next_nothing', type=int, default=12345)

current_next_nothing = parser.parse_args().next_nothing

while True:
    text = get_url('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(current_next_nothing))
    print text
    current_next_nothing = int(text.split()[-1])

# Solution: peak.html

