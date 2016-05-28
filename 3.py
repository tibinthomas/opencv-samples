import cv2

videoCapture = cv2.VideoCapture('Video1.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('MyOutputVid.avi',cv2.VideoWriter_fourcc(*'DIVX'),fps,size)
success,frame = videoCapture.read()

while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()


