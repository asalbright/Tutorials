# OpenCV Python Tutorial #2 - Image Fundamentals and Manipulation
'''
00:00 | Intro
01:45 | Image Representation
04:02 | Values that Represent our Pixels
07:20 | Accessing Pixel Values
08:45 | Changing Pixel Colors
11:37 | Copying & Pasting Parts of Image
15:07 | Outro
'''

import cv2
import random

img = cv2.imread("OpenCV/figures/Unknown.jpeg", -1)

print(img) # an array
print(type(img)) # image is stored in an array
print(img.shape) # pixels are represented as BGR (blu, grn, red)

# lets look at the first row of the image
print(img[0])
# some of the first row
print(img[0][25:35])

# loop through some pixels and change them
for ii in range(50):
    for jj in range(img.shape[1]):
        img[ii][jj] = [random.randint(0, 255), 
                     random.randint(0, 255), 
                     random.randint(0, 255)]

# copy a part of the image and paste it elseware
copy = img[100:150, 250:300]
img[0:50, 0:50] = copy

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()