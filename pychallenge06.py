# http://www.pythonchallenge.com/pc/def/channel.html
# http://www.pythonchallenge.com/pc/def/channel.zip

import zipfile
import sys
from os.path import join

def extract_zip():
    with zipfile.ZipFile('data/channel.zip') as zip_handle:
        zip_handle.extractall('data/06_channel')

def analyze_files(start):

    current_next_nothing = start
    while True:
        next_nothing_filename = join('data/06_channel', '{}.txt'.format(current_next_nothing))
        with open(next_nothing_filename, 'r') as nn_handle:
            text = nn_handle.read()
            print current_next_nothing, text
            current_next_nothing = int(text.split()[-1])


def collect_comments(start):

    def add_txt(number):
        return '{}.txt'.format(number)
    
    current_nn_filename = add_txt(start)
    
    with zipfile.ZipFile('data/channel.zip') as archive:
        comments = {info.filename : info.comment for info in archive.infolist()}
        
        while True:
            sys.stdout.write(comments[current_nn_filename])
            text = archive.read(current_nn_filename)
            current_nn_filename = add_txt(text.split()[-1])


# readme.txt: start from 90052

# extract_zip()
# analyze_files(90052)
collect_comments(90052)
