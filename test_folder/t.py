import cv2
import numpy as np


path = 'C:\\Users\\trisk\\OneDrive\\Dokumenty\\GitHub\\maze-solver\\mazes\\maze0.png'

img = cv2.imread(path)              #  img [ rows ] [ cols ] [ pixel ]
img_size = (len(img), len(img[0]))  # (x_axis_pixel_len, y_axis_pixel_len)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

(_, black_white_img) = cv2.threshold(grey_img, 127, 255, cv2.THRESH_BINARY)      # (thresh, black&white)




# crop image
zeros_occurences = np.where(black_white_img == 0)[0]
top_line_index = zeros_occurences[0]
bottom_line_index = zeros_occurences[-1]

zeros_occurences = np.where(black_white_img[top_line_index] == 0)[0]
l_line_index = zeros_occurences[0]
r_line_index = zeros_occurences[-1]


black_white_img = black_white_img[top_line_index:bottom_line_index, l_line_index:r_line_index]
# cv2.imshow('', black_white_img)



cv2.waitKey(0)
cv2.destroyAllWindows()