# http://www.pythonchallenge.com/pc/def/ocr.html
from bs4 import BeautifulSoup, Comment
import urllib2
from utils.alphabet import get_lowercase_alphabet
from utils.web import get_html_comments

# 1. Get the comment to be analysed using urllib and BeautifulSoup
pyurl = 'http://www.pythonchallenge.com/pc/def/ocr.html'
all_comments = get_html_comments(pyurl)
pycomment = all_comments[-1]

# 2. Find the comment characters that belong to the alphabet
alphabet = get_lowercase_alphabet()
result = [comment_char for comment_char in pycomment if comment_char in alphabet]

print ''.join(result)

