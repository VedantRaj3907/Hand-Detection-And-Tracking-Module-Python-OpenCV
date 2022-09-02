import mediapipe as mp
import cv2 as cv
import time 

vid = cv.VideoCapture(0)
mphands = mp.solutions.hands  #taking solution of hands
hands = mphands.Hands()       #taking hands 
mpdraw = mp.solutions.drawing_utils     #taking solutions to draw connections and landmarks

cTime = 0
pTime = 0

while True:
    yes,frame = vid.read()
    video_flip = cv.flip(frame, 1)
    imgRGB = cv.cvtColor(video_flip, cv.COLOR_BGR2RGB) #converting to RGB as mediapipe works with RGB
    results = hands.process(imgRGB)              #processing hands with RGb image taken

    if (results.multi_hand_landmarks):            #if hand is detected it gives u the location and then  checking for multiple hands in a frame
        for handLndMs in results.multi_hand_landmarks:      #IF YES THEN DRAWING LANDMARKS AND CONNECTIONS BETWEEN THE LANDMARKS
            for id, ld in enumerate(handLndMs.landmark):
                h, w, c = video_flip.shape
                cx, cy = int(ld.x*w), int(ld.y*h)
                print(id,cx,cy)
                if id:
                    cv.circle(video_flip, (cx,cy),10,(0,255,0), cv.FILLED)
            mpdraw.draw_landmarks(video_flip,handLndMs,mphands.HAND_CONNECTIONS)

    cTime = time.time()     #taking current time
    fps = 1/(cTime - pTime) #taking fps
    pTime = cTime           #giving previous time the value of currrent time

    cv.putText(video_flip, str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX, 3, (255,0,0), 3) #putting fps on the screen (converting it to int and str)
    cv.imshow("video",video_flip)
    if(cv.waitKey(1)==ord('q')):
        break

vid.release()
cv.destroyAllWindows()