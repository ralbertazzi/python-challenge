from bs4 import BeautifulSoup, Comment
import urllib2

def get_url(pyurl, **kwargs):
    
    if 'username' in kwargs and 'password' in kwargs:
        
        import base64
        
        base64string = base64.encodestring('%s:%s' % (kwargs['username'], kwargs['password'])).replace('\n', '')
        request = urllib2.Request(pyurl)
        request.add_header("Authorization", "Basic %s" % base64string) 
        result = urllib2.urlopen(request)
        
        return result.read()
   
    else:
        return urllib2.urlopen(pyurl).read()

def get_url_bs4(pyurl, **kwargs):
    return BeautifulSoup(get_url(pyurl, **kwargs), 'html.parser')

def get_html_comments(pyobj, **kwargs):
    if type(pyobj) == str:
        pysoup = get_url_bs4(pyobj, **kwargs)
    elif type(pyobj) == BeautifulSoup:
        pysoup = pyobj
    else:
        raise ValueError('Invalid input pyobj')

    return list(pysoup.find_all(string=lambda text:isinstance(text,Comment)))

def get_image_from_url(pyurl, **kwargs):
    
    import numpy as np
    import cv2

    arr = np.asarray(bytearray(get_url(pyurl, **kwargs)), dtype='uint8')
    return cv2.imdecode(arr, cv2.IMREAD_COLOR)    
