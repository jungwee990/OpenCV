import cv2

capture = cv2.VideoCapture("Star.mp4")
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
videowrite = cv2.VideoWriter()
isWrite = False

while True:
    ret, frame = capture.read()

    if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("Star.mp4")

    cv2.imshow("VideoFrame", frame)
    key = cv2.waitkey(33)

    if key == 4:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoWriter.open("Video.avi", fourcc, 30, (width, height), True)
    isWrite = True

    elif key == 24:
    videowriter.release()
    isWrite = Flase

    elif key == ord('q'):
    break

    if isWrite == True:
        videoWriter.write(frame)

videoWriter.release()
capture.release()
cv2.destroyALLWindows()

