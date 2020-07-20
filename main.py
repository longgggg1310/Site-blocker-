import cv2
import numpy as np


class Camera():

	def __init__(self):
		self.cap = cv2.VideoCapture(0)
		print("Camera warming up...")

	def get_frame(self):
		s,img = self.cap.read()
		if s:
			pass
		return img
		
	def release_camera(self):
		self.cap.realse()
	def rgb2gray(self,frame):
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		return frame
	
	def filter_color(self,frame):
		blur = cv2.GaussianBlur(frame,(11,11),0)
		hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
		
		lower = np.array([0,0,168], dtype=np.uint8)
		upper = np.array([172,111,255], dtype=np.uint8)
		
		mask =cv2.inRange(hsv,lower,upper)
		mask =cv2.erode(mask,None,iterations = 2)
		mask =cv2.dilate(mask,None,iterations = 2)
		res = cv2.bitwise_and(frame,frame, mask= mask)


	


	
	
		return res
	def mask(self,frame): 
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		lower = np.array([0,0,168], dtype=np.uint8)
		upper = np.array([172,111,255], dtype=np.uint8)
		mask = cv2.inRange(hsv, lower, upper)
		return mask
	

    
    	
        	

   
   	
camera=Camera()
def main():
	
	while (True):
		
		cam1 = camera.get_frame()



		frame = cv2.resize(cam1,(0,0),fx=0.9, fy=0.9)
		frame = camera.filter_color(frame)
		
		mask = camera.mask(frame)
		
		
		
		cv2.imshow("Frame",frame)
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
		cv2.imshow("mask",mask)
		cv2.imshow("origin",cam1)
		
		

	camera.release_camera()
	return()



if __name__ =="__main__":
	main()
	cv2.destroyAllWindows()
    
