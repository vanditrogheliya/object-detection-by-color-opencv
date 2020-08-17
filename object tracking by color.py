import cv2
import numpy as np
def nothing(x):
    pass

stream = cv2.VideoCapture(0)

cv2.namedWindow('Track')
cv2.createTrackbar('LH','Track', 0, 255, nothing)
cv2.createTrackbar('LS','Track', 0, 255, nothing)
cv2.createTrackbar('LV','Track', 0, 255, nothing)
cv2.createTrackbar('UH','Track', 255, 255, nothing)
cv2.createTrackbar('US','Track', 255, 255, nothing)
cv2.createTrackbar('UV','Track', 255, 255, nothing)

while(1):
    _, frame = stream.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos('LH', 'Track')
    l_s = cv2.getTrackbarPos('LS', 'Track')
    l_v = cv2.getTrackbarPos('LV', 'Track')

    u_h = cv2.getTrackbarPos('UH', 'Track')
    u_s = cv2.getTrackbarPos('US', 'Track')
    u_v = cv2.getTrackbarPos('UV', 'Track')

    l = np.array([l_h,l_s,l_v])
    u = np.array([u_h,u_s,u_v])

    img = cv2.inRange(hsv, l, u)

    result = cv2.bitwise_and(frame, frame, mask=img)

    cv2.imshow('result', result)
    cv2.imshow('Original', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

stream.release()
cv2.destroyAllWindows()