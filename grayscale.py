#  https://www.geeksforgeeks.org/python-grayscaling-of-images-using-opencv/?ref=rp

######################## Method 1: Using the cv2.cvtColor() function  ############################


# import opencv
import cv2

# Load the input image
image = cv2.imread('yoruxanya.jpg')
# cv2.imshow('Original', image)
# cv2.waitKey(0)

# Use the cvtColor() function to grayscale the image
print ('Creating...' )
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale', gray_image)
# cv2.waitKey(0) 

# writing the gray image
status = cv2.imwrite('grayimage.jpg', gray_image)
print("Image written to file-system : ",status)

# Window shown waits for any key pressing event
cv2.destroyAllWindows()

### Note:  cv2.imwrite() returned true which means the file has been successfully written to the path specified. Reading the return value of imwrite() is very important as sometimes there could be multiple reasons that fail the disk write operation and resulting in the image not written to disk.

# ##################### Method 2: Using the cv2.imread() function with flag = zero  ########################

# # Import opencv
# import cv2

# # Use the second argument or (flag value) zero
# # that specifies the image is to be read in grayscale mode
# img = cv2.imread('yoruxanya.jpg', 0)

# # cv2.imshow('Grayscale Image', img)
# # cv2.waitKey(0)

# # writing the gray image
# status = cv2.imwrite('grayimage.jpg', img)
# print("Image written to file-system : ",status)

# # Window shown waits for any key pressing event
# cv2.destroyAllWindows()



# ############### Method 3: Using the pixel manipulation (Average method) ############
# # Slower compared to above two

# # Import opencv
# import cv2

# # Load the input image
# img = cv2.imread('yoruxanya.jpg')

# # Obtain the dimensions of the image array
# # using the shape method
# (row, col) = img.shape[0:2]

# # Take the average of pixel values of the BGR Channels
# # to convert the colored image to grayscale image
# for i in range(row):
# 	for j in range(col):
# 		# Find the average of the BGR pixel values
# 		img[i, j] = sum(img[i, j]) * 0.33

# # cv2.imshow('Grayscale Image', img)
# # cv2.waitKey(0)

# # writing the gray image
# status = cv2.imwrite('grayimage.jpg', img)
# print("Image written to file-system : ",status)

# # Window shown waits for any key pressing event
# cv2.destroyAllWindows()


# ################ Method 4: using cv2.IMREAD_GRAYSCALE  #####################

# import cv2
 
# # read image as grey scale
# grey_img = cv2.imread('yoruxanya.jpg', cv2.IMREAD_GRAYSCALE)
 
# # save image
# status = cv2.imwrite('grayscale.png',grey_img)
 
# print("Image written to file-system : ",status)