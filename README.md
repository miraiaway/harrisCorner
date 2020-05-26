# harrisCorner

What is Harris Corner Detection?<br />
It is a commonly used computer vision algorithm to extract corners of an image. Introduced by Chris Harris and Mike Stephens.

**Corner Detection**: Locations in an image with a large change of intensity along the x and y axis 

Simple steps of Harris Corner Detection algorithm:
1.	Determine (a window) what part of the image have a large variation in intensity when moved along the x and y axis. 
2.	Within each window, compute the value R.
3.	Apply a threshold to select and mark the corners

Mathematical view of algorithm:
1.	Determine windows that contain large variations of intensity.<br />
Window: (x,y)<br />
Intensity of a pixel: I(x,y)<br />
Window shift displacement: (u, v)<br />
Intensity of pixel at location with displacement: I(x + u, y + v)<br />
Difference in intensity: I(x + u, y + v) – I(x, y)<br />

Window function outputs the weights to pixels by using the rectangular window or gaussian window. To maximize the function below, the second term has to be maximized. To do so efficiently, the Taylor Expansion is used.
<p align="center">
  <img width="400" height="200" src="Images/WindowFunction.png">
</p>
<br />
The Taylor expansion is used to find the infinite sum at a single point. As a result, it generates the mathematical equation below.
<p align="center">
  <img width="400" height="200" src="Images/TaylorExpansion.png">
</p>
<br />

2.	Determine if a window contains a corner
By computing the value R, it returns a gray scale image with the corners (in code). The R value will tell the user if the window is a flat region, corner region or edge region.
<p align="center">
  <img width="500" height="300" src="Images/Flat_Corner_Edge.png">
</p>
<br />

R is computed by calculating the determinant of M subtracted by the empirically determined constant multiplied by the square of the trace of M.
<p align="center">
  <img width="400" height="200" src="Images/cornerEq.png">
</p>
<br />

•	When |R| is small --> Both eigenvalues are small, so it is a flat region <br />
•	When R < 0 --> One eigenvalue is greater than the other, so it is an edge <br />
•	When R is large --> Both eigenvalues are large and close in numbers, so the region is a corner <br />
<p align="center">
  <img width="400" height="410" src="Images/harris_region.jpg">
</p>
<br />

**Code Breakdown**
<br />
<p align="center">
  <img width="400" height="230" src="Images/CodeBreakdown_1.PNG">
</p>

Line 1 + 2: Import necessary libraries to use for this code
Line 4: Read in image file and assign to variable ‘img’<br />
Line 7: Convert the image from BGR to gray scale<br />
Line 10: Show gray scale image to user<br />
Line 13: Convert the image to be 32 bit float data type because the Harris Corner function only takes in 32 bit floats<br />

<br />
<p align="center">
  <img width="600" height="200" src="Images/CodeBreakdown_2.PNG">
</p>

Line 20: Use OpenCV’s library function called cornerHarris to detect the corner cases in the image
Line 22: Display all the corners in the image<br />
Line 25: Dilate the corners to look more visible to the user<br />
Line 27: Display to user the dilated corners in image<br />

<br />
<p align="center">
  <img width="700" height="230" src="Images/CodeBreakdown_3.PNG">
</p>

Line 34: Threshold value R and color the corners red.
Line 36: Display image with corners marked red<br />
Line 38: Press any key to kill all windows and kill code<br />
Line 39: Deallocate all memory used for this code<br />

References:<br />
[Open CV Documentation](https://docs.opencv.org/master/dc/d0d/tutorial_py_features_harris.html)<br />
[Detect Corners Medium Blog](https://medium.com/pixel-wise/detect-those-corners-aba0f034078b)<br />

