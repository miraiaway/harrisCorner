import cv2
import numpy as np 

img = cv2.imread('chss.jpg')

# Conver the image from BGR to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the image
cv2.imshow('gray', gray)

# Convert the image to 32 bit floats
gray = np.float32(gray)

# Detect the corners
# Parameter 1 -> input image (has to be gray scale and float32 type)
# Parameter 2 -> blockSize -> Size of neighborhood considered for corner detection
# Parameter 3 -> ksize -> Aperture parameter of sobel derivative used
# Parameter 4 -> k -> Harris detector free parameter in the equation
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

cv2.imshow('cornerCase', dst)

# Results are marked through the dilated corners
dst = cv2.dilate(dst, None)

cv2.imshow('dilated', dst)

# Threshold for an optimal value
# dst >  0.01 -> Returns a numpy array, if above 0.01, true(1), if below 0.01, then false(0)
# dst.max() -> Returns the max intensity value in the dst image
# Multiply each value in (dst > 0.01) by dst.max() so the img numpy array contains value of dst.max() and 0
# Mark the dst.max() values as red!
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('finalImage', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
