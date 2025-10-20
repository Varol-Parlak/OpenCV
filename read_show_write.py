import cv2 as cv

# read a video

video = cv.VideoCapture("E:\Python\OpenCV\Photos\CatVideo.mp4")

while True:
    isTrue ,frame = video.read()

    cv.imshow("Cat", frame)
    
    
    if cv.waitKey(30) & 0xFF==ord("q"):
        break

video.release()
cv.destroyAllWindows()


##########################################

# read a photo

photo = cv.imread("E:\Python\OpenCV\Photos\car.jpg")

cv.imshow("car",photo)
cv.waitKey(0)

##########################################

# write a photo 

photo = cv.imread("E:\Python\OpenCV\Photos\dog.jpg")

cv.imwrite("OpenCV/Photos/dog.webp", photo)
cv.waitKey(0)