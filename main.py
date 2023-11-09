# import cv2
# from threading import Thread
# from queue import Queue

# url = 'rtsp://rtsp:Rtsp1234@188.170.176.190:8027/Streaming/Channels/101?transportmode=unicast&profile=Profile_1'
# username = 'admin'
# password = 'A1234567'
# url = f'rtsp://{username}:{password}@' + url.split('@')[1]
# video = cv2.VideoCapture(url)

# while True:
#     _, frame = video.read()
#     cv2.imshow('RTSP', frame)
#     k = cv2.waitKey(1)
#     if k == ord('q'):
#         break

# video.release()
# cv2.destroyAllWindows()
# # import numpy as np
# # import cv2
# # from threading import Thread

# # class Algo(Thread):
# #     def __init__(self, frame):
# #         Thread.__init__(self)
# #         self.frame = frame

# #     def run(self):
# #         faces = face_cascade.detectMultiScale(gray, 1.3,5)

# #         for (x,y,w,h) in faces:
# #             cv2.rectangle(frame, (x,y), (x+y, y+h), (255,0,0), 2)
# #             roi_gray = gray[y:y+h, x:x+w]
# #             roi_color = frame[y:y+h, x:x+w] 
# # url = 'rtsp://rtsp:Rtsp1234@188.170.176.190:8027/Streaming/Channels/101?transportmode=unicast&profile=Profile_1'
# # username = 'admin'
# # password = 'A1234567'
# # url = f'rtsp://{username}:{password}@' + url.split('@')[1]
# # cap = cv2.VideoCapture(url)

# # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# # while(True):
# #     # Capture frame-by-frame
# #     cap.grab()
# #     ret, frame = cap.retrieve()

# #     # Our operations on the frame come here
# #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #     gray.resize(gray, (640, ))
# #     thread_1 = Algo(frame)
# #     thread_1.start()
# #     thread_1.join()

# #     # Display the resulting frame
# #     cv2.imshow('frame', frame)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# #     # When everything done, release the capture
# # cap.release()
# # cv2.destroyAllWindows()