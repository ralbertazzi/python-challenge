from bs4 import BeautifulSoup, Comment
import urllib2

def get_url(pyurl):
    return urllib2.urlopen(pyurl).read()

def get_url_bs4(pyurl):
    return BeautifulSoup(get_url(pyurl), 'html.parser')

def get_html_comments(pyobj):
    if type(pyobj) == str:
        pysoup = get_url_bs4(pyurl)
    elif type(pyobj) == BeautifulSoup:
        pysoup = pyobj
    else:
        raise ValueError('Invalid input pyobj')

    return list(pysoup.find_all(string=lambda text:isinstance(text,Comment)))

def get_image_from_url(pyurl):
    
    import numpy as np
    import cv2

    arr = np.asarray(bytearray(get_url(pyurl)), dtype='uint8')
    return cv2.imdecode(arr, cv2.IMREAD_COLOR)    
