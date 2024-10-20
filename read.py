#image reading
import cv2 as cv
#img = cv.imread('cat1.jpeg')
#cv.imshow('Cat',img)
#cv.waitKey(0)


#video reading
vid=cv.VideoCapture('catv.mp4')
while True:
    isTrue, frame =vid.read()
    cv.imshow('Video', frame)
    if cv.waitKey(0) & 0xFF==ord('d'):
        break
    
vid.release()
cv.destroyAllWindows()
