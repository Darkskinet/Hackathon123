import serial.tools.list_ports
import pyautogui
import string
import cv2 as cv
import mediapipe as m
import time
import threading
import webbrowser
import eventlet
import socketio
# import eventlet
from flask import Flask, render_template
# eventlet.monkey_patch()

num = 0

webserver = Flask(__name__)
sio = socketio.Server(cors_allowed_origins='*',
 logger=True, engineio_logger=True)
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def hello(sid, data):
    print('message ', data)
    sio.emit('hello', "world")
    emit_gesture(1)
    print(num)

def emit_gesture(num):
    sio.emit('gesture', num)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

# emit event
def gestures():
    global num
    global sio
    t = 0
    print('starting....')
    mp = m.solutions.hands
    hands = mp.Hands(False, 1)
    draw = m.solutions.drawing_utils
    cap = cv.VideoCapture(0)
    cap.set(3, 1000)
    cap.set(4, 1000)
    x1 = x2 = 0
    to_check = [(8, 6), (12, 10), (16, 14), (20, 18)]
    while True:
        bol, img = cap.read()
        img = cv.flip(img, 3)
        # img = cv.flip(img, 1)
        img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        process = hands.process(img1)
        lm = process.multi_hand_landmarks
        h, w, d = img.shape

        if lm:
            shree = []
            Shree = []
            for hand in lm:
                draw.draw_landmarks(img, hand, mp.HAND_CONNECTIONS)
                for id, coord in enumerate(hand.landmark):
                    x = int(coord.x * w)
                    y = int(coord.y * h)
                    # print(id, x, y)
                    shree.append((x, y))
            
            num = 0
            for i in to_check:
                if shree[i[0]][1] > shree[i[1]][1]:
                    Shree.append(1)
                    num += 1
                else:
                    Shree.append(0)
            if shree[4][0] < shree[2][0]:
                num += 1
                Shree.append(1)
            else:
                Shree.append(0)

            nfv = 0
            for nf in range(0, 5):
                nfv = nfv + Shree[nf]
            print(nfv)

            if nfv == 0:
                time.sleep(0.7)
                t = t + 1
                if t == 5:
                    t = 0
                    print('no fingers are closed')
                    sio.emit("gesture", 0)
                    emit_gesture(0)
                    # Send data to frontend that no five fingers are closed
            if nfv == 1:
                time.sleep(0.7)
                t = t + 1
                if t == 5:
                    t = 0
                    sio.emit("gesture", 1)
                    print('one finger is closed')
                    emit_gesture(1)
                    webbrowser.open(
                        "http://localhost:5000/static/main/timetable.pdf")
                    # Send data to frontend that one finger is closed
            if nfv == 2:
                time.sleep(0.7)
                t = t + 1
                if t == 5:
                    t = 0
                    print(sio)
                    sio.emit("gesture", 2)
                    print('two finger are closed')
                    emit_gesture(2)
                    webbrowser.open("https://cbseacademic.nic.in/")
                    # Send data to frontend that two finger are closed
            if nfv == 3:
                time.sleep(0.7)
                t = t + 1
                if t == 5:
                    t = 0
                    sio.emit("gesture", 3)
                    print('3 fingers are closed')
                    emit_gesture(3)
                    webbrowser.open("https://ict.dunesinternationalschool.com")
                    # Send data to frontend that 3 fingers are closed
            if nfv == 4:
                time.sleep(0.7)
                t = t + 1
                if t == 5:
                    t = 0
                    sio.emit("gesture", 4)
                    print('4 fingers are closed')
                    emit_gesture(4)
                    webbrowser.open("https://ncert.nic.in/textbook.php")
                    # Send data to frontend that 4 fingers are closed
            if nfv == 5:
                time.sleep(0.7)
                t = t + 1
                if t == 5:
                    t = 0
                    sio.emit("gesture", 5)
                    print('5 fingers are closed')
                    emit_gesture(5)
                    # Send data to frontend that 5 fingers are closed

            # print(Shree)
            cv.putText(img, str(num), (150, 150),
                       cv.FONT_HERSHEY_PLAIN, 12, (255, 0, 0), 12)
            emit_gesture(num)
        cv.imshow('', img)
        if cv.waitKey(1) & 0xFF == ord('c'):
            break


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

serialInst.baudrate = 9600
serialInst.port = 'COM4'
# serialInst.open()
usr = 1
users = ['Shree', 'Haazim']

# CHANGE THIS TO TRUE IF YOU WANT TO USE THE RFID TAGS
while False:
    if serialInst.in_waiting:
        pp = serialInst.readline()
        # print(pp.decode('utf'))
        x, y = pyautogui.position()

        a = pp.decode('utf')
        print(a)
        with open('The_data.txt', 'w') as fw:
            fw.write(
                str(a.translate({ord(c): None for c in string.whitespace})))
        with open('The_data.txt', 'r') as fr:
            uid = fr.readlines()
        if uid[0] == 'RFIDTagUID:33B10C17':
            usr = 1
            break
        elif uid[0] == 'RFIDTagUID:7A81CF5C':
            usr = 2
            break


def startGestures():
    if usr == 1:
        # Send data to frontend as user 1
        print('User 1')
        gestures()


    if usr == 2:
        # Send data to frontend as user 2
        print('User 2')
        gestures()

def startWebServer():
    webbrowser.open("http://localhost:5000")
    webserver.run()

def startSocketIO():
    eventlet.wsgi.server(eventlet.listen(('', 1337)), app)

if __name__ == "__main__":
    t1 = threading.Thread(target=startGestures)
    t2 = threading.Thread(target=startWebServer)
    t3 = threading.Thread(target=startSocketIO) 
    
    t1.start()
    t2.start()
    t3.start()

    # t1.join()

@webserver.route("/")
def run():
    return render_template("index.html", user = users[usr])

