import cv2 #for image processing


cam = cv2.VideoCapture(0)

while 1:
    ret,frame = cam.read()
    grayScaleimg = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    smoothGrayScale = cv2.medianBlur(grayScaleimg, 5)

    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)

    colorImage = cv2.bilateralFilter(frame, 9, 300, 300)

    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)

    cv2.imshow('cartoonified',cartoonImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()