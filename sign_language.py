import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            #acessando os pontos de referência pela sua posição
            lm_list=[]
            finger_fold_status = (True)
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
                for tip in finger_tips:
                    x,y = int(lm_list[tip].x*w), int(lm_list[tip].y*h)
                    cv2.circle(img(x,y),15,(0,255,0),cv2.FILLED)
                    if lm_list[tip].x < lm_list[tip - 3].x:
                        cv2.circle(img,(x,y), 15,(255,0,0), cv2.FILLED)
                        finger_fold_status.appennd(True)
                    else:
                        finger_fold_status.appennd(False)
                    if lm_list[tip].y < lm_list[tip - 4].y:
                        cv2.circle(img,(x,y), 15,(255,0,0), cv2.FILLED)
                        finger_fold_status.appennd(True)
                    else:
                        finger_fold_status.appennd(False)
                    if all(finger_fold_status):
                        if lm_list[thump_tip].y < lm_list[thump_tip-1].y < lm_list[thump_tip-2].y:
                            print("curti")
                            cv2.putText(img,"curti",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
                        if lm_list[thump_tip].y < lm_list[thump_tip-1].y < lm_list[thump_tip-2].y:
                            print("não curti")
                            cv2.putText(img,"não curti",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)

            

             #O código vai aqui  
            fingers_tips = [8,12,16,20]
            
            


            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("detector de maos", img)
    cv2.waitKey(1)