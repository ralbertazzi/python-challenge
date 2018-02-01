from bs4 import BeautifulSoup, Comment
import urllib2

def get_url(pyurl):
    return urllib2.urlopen(pyurl).read()

def get_url_bs4(pyurl):
    return BeautifulSoup(get_url(pyurl), 'html.parser')

def get_html_comments(pyurl):
    pysoup = get_url_bs4(pyurl)
    return list(pysoup.find_all(string=lambda text:isinstance(text,Comment)))
