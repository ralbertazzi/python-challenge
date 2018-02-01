# http://www.pythonchallenge.com/pc/def/equality.html

import numpy as np
from utils.alphabet import get_uppercase_alphabet
from utils.web import get_html_comments
from utils.general import list_of_chars_to_string


def find_pattern(arr, pattern):
    
    """ Perform some kind of convolution in order to find a pattern.
        Might not be the most efficient way to compute this """  

    l = len(pattern)
    for idx in range(len(arr) - l):
        arr_slice = arr[idx:idx+l]
        yield 1 if np.array_equal(arr_slice, pattern) else 0


target = np.array([0, 1, 1, 1, 0, 1, 1, 1, 0])
    

pyurl = 'http://www.pythonchallenge.com/pc/def/equality.html'
pycomment = get_html_comments(pyurl)[-1]

u_alphabet = get_uppercase_alphabet()
condition = np.array([1 if c in u_alphabet else 0 for c in pycomment])

pattern_mask = np.array(list(find_pattern(condition, target)))
pattern_indexes = np.where(pattern_mask == 1)[0] + 4

print list_of_chars_to_string([c for idx, c in enumerate(pycomment) if idx in pattern_indexes and c != '\n'])

