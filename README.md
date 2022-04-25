# Histogram and Histogram Equalization of an image
## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1: 
Read the gray and color image using imread() 


### Step2:
Print the image using imshow().

### Step3:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### Step4:
cv2.equalize() is used to transform the gray image to equalized form.

### Step5:
The Histogram of gray scale image and color image is shown.

## Program:
```python
# Developed By:LOKESH KRISHNAA M 
# Register Number: 212220230030

import cv2
import matplotlib.pyplot as plt

# Write your code to find the histogram of gray scale image and color image channels.

import cv2
import matplotlib.pyplot as plt 

#gray scale and color image  
gray_image = cv2.imread("gray.jpg")
color_image = cv2.imread("tata.jpg")

#resizing and printing the image 
gray_image= cv2.resize(gray_image, (300,170))
cv2.imshow('GRAY IMAGE',gray_image)

color_image= cv2.resize(color_image, (300,170))
cv2.imshow('COLOR IMAGE',color_image)

cv2.waitKey(0)


#plotting the gray image in graph
plt.imshow(gray_image)
plt.show()


#plotting the color image in graph
plt.imshow(color_image)
plt.show()



# Display the histogram of gray scale image and any one channel histogram from color image

gray_hist=cv2.calcHist([gray],[0],None,[256],[0,255])
color_hist=cv2.calcHist([color],[2],None,[256],[0,255])
plt.figure()
plt.title("GRAY IMAGE")
plt.xlabel("GRAYSCALE VALUE")
plt.ylabel("PIXEL COUNT")
plt.stem(gray_hist)
plt.show()

plt.figure()
plt.title("COLOR IMAGE")
plt.xlabel("COLORSCALE VALUE")
plt.ylabel("PIXEL COUNT")
plt.stem(color_hist)
plt.show()





# Write the code to perform histogram equalization of the image. 

import cv2
Gray_image=cv2.imread('gray.jpg',0)
equalize=cv2.equalizeHist(Gray_image)
#resizing image 
Gray_image= cv2.resize(Gray_image, (270,190))
equalize= cv2.resize(equalize, (270,190))

#output
cv2.imshow('GRAY IMAGE',Gray_image)
cv2.imshow('EQUALIZED IMAGE',equalize)
cv2.waitKey(0)
cv2.destroyAllWindows()






```
## Output:
### Input Grayscale Image and Color Image
<br>
![Screenshot (39)](https://user-images.githubusercontent.com/75234646/165097244-6eecb077-ff8a-4725-b2a2-7f647618d287.png)


<br>

### Histogram of Grayscale Image and any channel of Color Image
<br>

![Screenshot (42)](https://user-images.githubusercontent.com/75234646/165099097-47a9b8f0-d2ff-44e7-ba35-0e24a2eee42a.png)


<br>

### Histogram Equalization of Grayscale Image
<br>

![Screenshot (41)](https://user-images.githubusercontent.com/75234646/165097271-8ff972bc-ac97-48a5-af5b-2de9a00d61cd.png)


<br>

## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.
