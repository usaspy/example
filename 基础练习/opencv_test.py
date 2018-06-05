import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while(True):
    ret,frame = cap.read()
    frame = cv.flip(frame, 1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('CANMA',frame)
    cv.imshow('CANMA-2', gray)
    k = cv.waitKey(30) & 0xFF
    print(k)
    if k == ord("s"):
        break
cap.release()
cv.destroyAllWindows()