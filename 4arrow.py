import cv2
from cvzone.HandTrackingModule import HandDetector
from directkeys import PressKey, ReleaseKey
from directkeys import up_pressed
from directkeys import down_pressed
from directkeys import left_pressed
from directkeys import right_pressed
import time

detector = HandDetector(detectionCon=0.8, maxHands=1)

up_key_pressed = up_pressed
down_key_pressed = down_pressed
left_key_pressed = left_pressed
right_key_pressed = right_pressed

time.sleep(2.0)

current_key_pressed = set()

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    keyPressed = False
    spacePressed = False
    key_count = 0
    key_pressed = 0
    hands, img = detector.findHands(frame)
    cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)
        print(fingerUp)
        #up
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'Up', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            PressKey(up_key_pressed)
            spacePressed = True
            current_key_pressed.add(up_key_pressed)
            key_pressed = up_key_pressed
            keyPressed = True
            key_count = key_count + 1

        # normal
        if fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, 'Normal', (20, 460), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 255, 255), 1, cv2.LINE_AA)
        #right
        if fingerUp == [0, 0, 1, 1, 1]:
            cv2.putText(frame, 'Right', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (255, 255, 255), 1, cv2.LINE_AA)

            PressKey(right_key_pressed)
            spacePressed = True
            current_key_pressed.add(right_key_pressed)
            key_pressed = right_key_pressed
            keyPressed = True
            key_count = key_count + 1

        # left
        if fingerUp == [1, 1, 0, 0, 0]:
            cv2.putText(frame, 'Left', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (255, 255, 255), 1, cv2.LINE_AA)

            PressKey(left_key_pressed)
            spacePressed = True
            current_key_pressed.add(left_key_pressed)
            key_pressed = left_key_pressed
            keyPressed = True
            key_count = key_count + 1

        #down
        if fingerUp == [1, 1, 0, 0, 1]:
            cv2.putText(frame, 'Down', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (255, 255, 255), 1, cv2.LINE_AA)

            PressKey(down_key_pressed)
            spacePressed = True
            current_key_pressed.add(down_key_pressed)
            key_pressed = down_key_pressed
            keyPressed = True
            key_count = key_count + 1

        if not keyPressed and len(current_key_pressed) != 0:
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()
        elif key_count == 1 and len(current_key_pressed) == 2:
            for key in current_key_pressed:
                if key_pressed != key:
                    ReleaseKey(key)
            current_key_pressed = set()
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
