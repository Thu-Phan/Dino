import cv2
from cvzone.HandTrackingModule import HandDetector
from matplotlib.backend_bases import key_press_handler
from directkeys import PressKey, ReleaseKey
from directkeys import up_pressed
from directkeys import down_pressed
import time
from selenium import webdriver
from pynput.mouse import Button, Controller


def clickleft(Mouse):
    Mouse.position = (100, 100)
    Mouse.press(Button.left)
    Mouse.release(Button.left)


driver = webdriver.Chrome(".\driver\chromedriver.exe")
driver.set_window_position(0, 0)
driver.set_window_size(600, 600)

detector = HandDetector(detectionCon=0.8, maxHands=1)

up_key_pressed = up_pressed
######
down_key_pressed = down_pressed

current_key_pressed = set()

video = cv2.VideoCapture(0)
mouse = Controller()

while True:
    ret, frame = video.read()
    keyPresses = False
    spacePressed = False
    key_count = 0
    key_pressed = 0
    hands, img = detector.findHands(frame)
    cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)
        tmp = sum(fingerUp)

        if tmp == 1:
            driver.get("https://chromedino.com/")

            break
        elif tmp == 2:
            driver.get("https://chromedino.com/black/")

            break
        elif tmp == 3:
            driver.get("https://chromedino.com/batman/")

            break
        elif tmp == 4:
            driver.get("https://chromedino.com/mario/")

            break
        elif tmp == 5:
            driver.get("https://chromedino.com/joker/")

            break

tmp = 0
immotal_tmp = 0
lspeed_tmp = 0
bot_tmp = 0

refresh_tmp = 0
clickleft(mouse)

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
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'Finger Count: 0', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, 'Jumping', (440, 460), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 255, 255), 1, cv2.LINE_AA)
            PressKey(up_key_pressed)
            spacePressed = True
            current_key_pressed.add(up_key_pressed)
            key_pressed = up_key_pressed
            keyPressed = True
            key_count = key_count + 1

            #tmp here
            tmp = 0
            immotal_tmp = 0
            lspeed_tmp = 0
            bot_tmp = 0

            refresh_tmp = 0

            #tmp here
            tmp = 0
            immotal_tmp = 0
            lspeed_tmp = 0
            bot_tmp = 0

            refresh_tmp = 0

        #immortal
        if fingerUp == [0, 1, 0, 0, 0]:
            cv2.putText(frame, 'Immortal', (20, 460), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, '1 finger', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            #tmp here
            tmp = 0
            immotal_tmp += 1
            lspeed_tmp = 0
            bot_tmp = 0

            refresh_tmp = 0

        #out
        if fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(frame, 'Goodbye', (20, 460), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, '2 fingers', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            #tmp here
            tmp += 1
            immotal_tmp = 0
            lspeed_tmp = 0
            bot_tmp = 0

            refresh_tmp = 0

        #bot play
        if fingerUp == [0, 1, 1, 1, 0]:
            cv2.putText(frame, 'Bot auto play', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, '3 finger', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)

            #tmp here
            tmp = 0
            immotal_tmp = 0
            lspeed_tmp = 0
            bot_tmp += 1

            refresh_tmp = 0

        #lightning speed
        if fingerUp == [0, 1, 1, 1, 1]:
            cv2.putText(frame, 'Lightning Speed', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, '4 fingers', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            #tmp here
            tmp = 0
            immotal_tmp = 0
            lspeed_tmp += 1
            bot_tmp = 0

            refresh_tmp = 0

        #normal
        if fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, 'Normal', (20, 460), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            driver.execute_script('Runner.instance_.setSpeed(5)')
            #tmp here
            tmp = 0
            immotal_tmp = 0
            lspeed_tmp = 0
            bot_tmp = 0

            refresh_tmp = 0

        # press down arrow key to duck

        if fingerUp == [1, 1, 0, 0, 1]:
            cv2.putText(frame, 'Duck', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            PressKey(down_key_pressed)
            spacePressed = True
            current_key_pressed.add(down_key_pressed)
            key_pressed = down_key_pressed
            keyPressed = True
            key_count = key_count + 1
            #tmp here
            tmp = 0
            immotal_tmp = 0
            lspeed_tmp = 0
            bot_tmp = 0

            refresh_tmp = 0

        #refresh page
        if fingerUp == [0, 0, 0, 1, 1]:
            cv2.putText(frame, 'Refresh', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            #tmp here
            tmp = 0
            immotal_tmp = 0
            lspeed_tmp = 0
            bot_tmp = 0

            refresh_tmp += 1

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
    #Mod here

    if immotal_tmp == 15:
        driver.execute_script('Runner.prototype.gameOver = function(){}')
        driver.execute_script('Runner.instance_.setSpeed(5)')

    if bot_tmp == 15:
        driver.execute_script('Runner.prototype.gameOver = function(){}')
        driver.execute_script('Runner.instance_.setSpeed(5)')
        driver.execute_script(
            'function keyDown(keyCode) { var event = document.createEvent("KeyboardEvent"); Object.defineProperty(event, "keyCode", { get: function parseKeyDown() { return this.keyCodeVal; }, }); if (event.initKeyboardEvent) { event.initKeyboardEvent( "keydown", true, true, document.defaultView, keyCode, keyCode, "", "", false, "" ); } else { event.initKeyEvent( "keydown", true, true, document.defaultView, false, false, false, false, keyCode, 0 ); } event.keyCodeVal = keyCode; document.body.dispatchEvent(event); } function keyUp(keyCode) { var event = document.createEvent("KeyboardEvent"); Object.defineProperty(event, "keyCode", { get: function get() { return this.keyCodeVal; }, }); if (event.initKeyboardEvent) { event.initKeyboardEvent( "keyup", true, true, document.defaultView, keyCode, keyCode, "", "", false, "" ); } else { event.initKeyEvent( "keyup", true, true, document.defaultView, false, false, false, false, keyCode, 0 ); } event.keyCodeVal = keyCode; document.body.dispatchEvent(event); } setInterval(function () { if (Runner.instance_.horizon.obstacles.length > 0) { if ( Runner.instance_.horizon.obstacles[0].xPos < 25 * Runner.instance_.currentSpeed - Runner.instance_.horizon.obstacles[0].width / 2 && Runner.instance_.horizon.obstacles[0].yPos > 75 ) { keyUp(40); keyDown(38); } if ( Runner.instance_.horizon.obstacles[0].xPos < 30 * Runner.instance_.currentSpeed - Runner.instance_.horizon.obstacles[0].width / 2 && Runner.instance_.horizon.obstacles[0].yPos <= 75 ) { keyDown(40); } } }, 5);'
        )

    if lspeed_tmp == 15:
        driver.execute_script('Runner.instance_.setSpeed(100)')

    if refresh_tmp == 30:

        driver.refresh()
    ######################
    k = cv2.waitKey(1)
    if (tmp == 30):

        break
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
