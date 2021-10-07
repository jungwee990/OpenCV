import cv2

capture = cv2.VideoCapture("../img/Star.mp4")

while True:
    ret, frame = capture.read()
    # 동영상이 끝났으면 다시 시작해라
    if(capture.get(cv2.CAP_PROP_POS_FRAMES)==capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("Star.mp4")

    cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(33) ==ord('q'):break

capture.release()
cv2.destroyAllWindows()
