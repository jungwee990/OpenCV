import cv2 as cv


alpha = 0.0
beta = 1.0
alpha_weight = 0.1
beta_weight = -0.1
img1 = cv.imread('beach.png', cv.IMREAD_COLOR)
img2 = cv.imread('cat.png', cv.IMREAD_COLOR)
while True:
    dst = cv.addWeighted(img1, alpha, img2, beta, 0)

    print( alpha, " ", beta)

    # cv.imshow('dst',dst)
    # key = cv.waitKey(0)

    cv.imshow('dst',dst)
    key = cv.waitKey(33)
    if key == ord('q'):
        break
    alpha = round(alpha + alpha_weight, 1)
    beta = round(beta + beta_weight, 1)

    if alpha >= 1 or alpha <=0:
        alpha_weight = -alpha_weight
    if beta >= 1 and beta <=0:
        beta_weight = -beta_weight
cv.destroyAllWindows()