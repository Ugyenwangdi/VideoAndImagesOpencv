# To explore opencv:  https://learnopencv.com/getting-started-with-opencv/

# From: https://www.geeksforgeeks.org/extract-images-from-video-in-python/
# 1. Create virtual env
# 2. activate env : .\env\Scripts\activate
# 3. install opencv
# pip install opencv-python

# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
video = cv2.VideoCapture("clock.mp4")

try:
	
	# creating a folder named images
	if not os.path.exists('images'):
		os.makedirs('images')

# if not created then raise error
except OSError:
	print ('Error while creating directory of images')

# frame
currentframe = 0

while(True):
	
	# reading from frame
	ret, frame = video.read()

	if ret:
		# if video is still left continue creating images
		name = './images/' + str(currentframe) + '.jpg'
		print ('Creating...' + name)

		# let's downscale the image using new  width and height
		down_width = 300
		down_height = 200
		down_points = (down_width, down_height)
		frame = cv2.resize(frame, down_points, interpolation= cv2.INTER_LINEAR)

		# # let's upscale the image using new  width and height
		# up_width = 1200
		# up_height = 900
		# up_points = (up_width, up_height)
		# frame = cv2.resize(frame, up_points, interpolation= cv2.INTER_LINEAR)
		
		# writing the extracted images
		cv2.imwrite(name, frame)

		# increasing counter 
		# to name images with number of images created
		currentframe += 1
	else:
		break

# Release all space and windows once done
video.release()
cv2.destroyAllWindows()
