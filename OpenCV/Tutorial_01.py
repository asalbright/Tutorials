# OpenCV Python Tutorial #1 - Introduction & Images
'''
00:00 | Introduction & Series Overview  
01:46 | Installation & Setup  
05:45 | Loading an Image  
07:56 | Displaying an Image  
10:35 | Resizing an Image  
12:45 | Rotating an Image  
'''

import cv2
from matplotlib import pyplot as plt

img = cv2.imread("OpenCV/figures/Unknown.jpeg", -1)     # -1, 0, 1 for different colors
img = cv2.resize(img, (0,0), fx=4, fy=4) # (pixel, pixel) or (0,0) fx=float, fy=float
img = cv2.rotate(img, cv2.ROTATE_180) # bunch of rotate options

cv2.imshow("Image", img) # shows the image, alt you could use matplotlibs plt.show      
cv2.waitKey(0)  # 0 would be infinity or a number is milliseconds
cv2.destroyAllWindows() # closes all the windows
