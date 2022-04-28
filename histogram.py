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
#plotting the gray image in graph
plt.imshow(gray_image)
plt.show()
#plotting the color image in graph
plt.imshow(color_image)
plt.show()



# Write your code to find the histogram of gray scale image and color image channels.
gray=cv2.imread("gray.jpg")
color=cv2.imread("tata.jpg")
gray=cv2.resize(gray,(500,400))
color=cv2.resize(color,(500,400))

cv2.imshow("GRAY IMAGE ",gray)
cv2.imshow("COLOR IMAGE ",color)

cv2.waitKey(0)


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





