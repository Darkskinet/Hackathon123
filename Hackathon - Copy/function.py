from PIL import Image as im
import os
import time
import webbrowser as wb
from tkinter import *
import pynput.keyboard as keyboard
import pynput.mouse as mouse
import tkinter as tk
from tkvideo import tkvideo

ctrl = keyboard.Controller()
ctrl_mouse = mouse.Controller()

def right_click():
    ctrl_mouse.press(mouse.Button.left)
def click_ctrl_W():
    ctrl.press(keyboard.Key.ctrl)
    ctrl.press('w')
    ctrl.release('w')
    ctrl.release(keyboard.Key.ctrl)

def click_ctrl_0():
    ctrl.press(keyboard.Key.ctrl)
    ctrl.press('0')
    ctrl.release('0')
    ctrl.release(keyboard.Key.ctrl)

win = Tk()
pg = 0
a = 0

pgs = [1,2,3,4,5]

with open('pg.txt', 'w') as pug1:
    pug1.write('-')

while True:
    with open(r'C:\Users\haazi\OneDrive\Desktop\Coding\BRS Hackathon\Hackathon - Copy\gst.txt', 'r') as gus:
        gst = gus.readlines()
    with open(r'C:\Users\haazi\OneDrive\Desktop\Coding\BRS Hackathon\Hackathon - Copy\user.txt', 'r') as us:
        usr = us.readlines()
    if pg == 0:
        with open('pg.txt', 'w') as pug1:
            pug1.write('0')
        if gst == ['0']:
            exit()
            time.sleep(1)
            a = 0
        if gst == ['1']:
            os.system('tb.png')
            click_ctrl_0()
            time.sleep(1)
            pg = 1
        if gst == ['2']:
            wb.open('http://ict.dunesinternationalschool.com/RPSM/')
            time.sleep(1)
            pg = 2
        if gst == ['3']:
            wb.open('https://cbseacademic.nic.in/')
            time.sleep(1)
            pg = 3
        if gst == ['4']:
            os.system(r'files\TT.pdf')
            time.sleep(1)
            pg = 4

    if pg == 1:
        if a == 0:
            with open('gst.txt', 'w') as gus:
                gus.write('-')
            time.sleep(2)
            with open(r'C:\Users\haazi\OneDrive\Desktop\Coding\BRS Hackathon\Hackathon - Copy\gst.txt', 'r') as gus:
                gst = gus.readlines()
            if gst == ['0']:
                print('yes')
                click_ctrl_W()
                pg = 0
                print(pg)
            if gst == ['1']:
                os.startfile(r'files\tb\ch_1_math.pdf')
                pg = 7
                a +=1
            if gst == ['2']:
                os.startfile(r'files\tb\ch_1_sci.pdf')
                pg = 7
                a += 1
            if gst == ['3']:
                os.startfile(r'files\tb\ch_1_eng.pdf')
                pg = 7
                a += 1
            if gst == ['4']:
                os.startfile(r'files\tb\ch_1_geo.pdf')
                pg = 7
                a += 1
            if gst == ['5']:
                os.startfile(r'files\tb\ch_1_hin.pdf')
                pg = 7
                a += 1

    if pg == 7:
        with open(r'C:\Users\haazi\OneDrive\Desktop\Coding\BRS Hackathon\Hackathon - Copy\gst.txt', 'w') as gus:
            gus.write('-')
        time.sleep(2)
        if gst == ['0']:
            time.sleep(1)
            click_ctrl_W()
            pg = 1
            a = 0
        # scrolling
        if gst == ['1']:
            right_click()
            for i in range(2):
                ctrl.press(keyboard.Key.down)
                ctrl.release(keyboard.Key.down)
        if gst == ['2']:
            right_click()
            for i in range(2):
                ctrl.press(keyboard.Key.up)
                ctrl.release(keyboard.Key.up)



    # for pg in pgs:
    #     if gst == ['0']:
    #         click_ctrl_W()
    #         pg = 0