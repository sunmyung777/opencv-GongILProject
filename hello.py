import cv2
image=cv2.imread("img/flower.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("flower",image)
cv2.waitKey(0)
cv2.destroyAllWindows()