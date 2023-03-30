import cv2

image_gray = cv2.imread('./HYNN/image/iu05.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Gray instead Hangul', image_gray)

cv2.waitKey()

cv2.destroyAllWindows()

cv2.imwrite('./HYNN/image/iu_grayscale.png', image_gray)  # boolean = True
