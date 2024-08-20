import cv2
img = cv2.imread("banner.jpg")
height,width,channels = img.shape
print(f"Size(Resolution) of your image is {width} X {height}")
