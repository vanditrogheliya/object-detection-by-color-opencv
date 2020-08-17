import cv2
import numpy as np
def nothing(x):
    pass

cv2.namedWindow('Track')
cv2.createTrackbar('LH','Track', 0, 255, nothing)
cv2.createTrackbar('LS','Track', 0, 255, nothing)
cv2.createTrackbar('LV','Track', 0, 255, nothing)
cv2.createTrackbar('UH','Track', 255, 255, nothing)
cv2.createTrackbar('US','Track', 255, 255, nothing)
cv2.createTrackbar('UV','Track', 255, 255, nothing)

image = cv2.imread('ball.jpg')
image = cv2.resize(image, (320, 320))
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
while(1):

    l_h = cv2.getTrackbarPos('LH', 'Track')
    l_s = cv2.getTrackbarPos('LS', 'Track')
    l_v = cv2.getTrackbarPos('LV', 'Track')

    u_h = cv2.getTrackbarPos('UH', 'Track')
    u_s = cv2.getTrackbarPos('US', 'Track')
    u_v = cv2.getTrackbarPos('UV', 'Track')

    l = np.array([l_h,l_s,l_v])
    u = np.array([u_h,u_s,u_v])

    img = cv2.inRange(hsv, l, u)

    result = cv2.bitwise_and(image, image, mask=img)

    cv2.imshow('result', result)
    cv2.imshow('Original', image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()