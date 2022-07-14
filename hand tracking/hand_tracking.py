import mediapipe as mp
import cv2
import time


cap = cv2.VideoCapture(0)

mphands  = mp.solutions.hands
hands1 = mphands.Hands()
mpdraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
while True:
    success ,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    resault = hands1.process(imgRGB)
    if resault.multi_hand_landmarks:
        for handLms in resault.multi_hand_landmarks:
            for idm , lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                print("id is:",idm,"x is:",cx,"y is:",cy)
                if idm == 4:
                    cv2.circle(img,(cx,cy),12,(255,0,0),cv2.FILLED)

     
            
            mpdraw.draw_landmarks(img,handLms,mphands.HAND_CONNECTIONS)
            

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("Hallo :)",img)
    cv2.waitKey(1)
    

    