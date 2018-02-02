# http://www.pythonchallenge.com/pc/def/oxygen.html
from utils.web import get_image_from_url
import numpy as np
from utils.general import list_of_chars_to_string


image = get_image_from_url('http://www.pythonchallenge.com/pc/def/oxygen.png').astype(np.int)

# 1. Find the coordinates of the grayscale pixels -> where all the 3 channels have the same value
masks = [np.abs(image[:,:,ch1] - image[:,:,ch2]) for ch1, ch2 in ((0,1), (0,2), (1,2))]
gray_mask = np.sum(masks, axis=0)

gray_idx_y, gray_idx_x = np.where(gray_mask == 0)

# 2. Since the number 7 drawn in the image is also grayscale (but we don't want it),
#     filter the lines that contains x_max grayscale
gray_x_max = gray_idx_x.max()
filter_max_x = np.where(gray_idx_x == gray_x_max)
gray_idx_y = gray_idx_y[filter_max_x]

# Select one gray row (the first one), only one channel (since they have the same value
gray_line = image[gray_idx_y[0], :gray_x_max + 1, 0]
# Sample one value every 7
changing_values = gray_line[::7]

print list_of_chars_to_string(map(chr, changing_values))
print list_of_chars_to_string(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))

