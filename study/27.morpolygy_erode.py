import cv2

src = cv2.imread("../img/dandelion.jpg", cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5), anchor=(-1,-1))
dst_erode = cv2.erode(src, kernel, iteration=3)
dst_dilate = cv2.erode(src, kernel, iterations=3)

cv2.pyrDown(src,src)
cv2.pyrDown(dst_dilate)
cv2.pyrDown(dst_erode)



cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()