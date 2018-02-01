# http://www.pythonchallenge.com/pc/def/peak.html

import sys
import cPickle as pickle
from utils.web import get_url

url_pickle = get_url('http://www.pythonchallenge.com/pc/def/banner.p')
data = pickle.loads(url_pickle)

# Print the data
for line in data:
    for ch, repeat in line:
        sys.stdout.write(ch * repeat)
    sys.stdout.write('\n')

