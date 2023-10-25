from PIL import Image as im
import os
import time
import webbrowser as wb
from tkinter import *
from pynput.keyboard import Key,Controller
import tkinter as tk
# from tkvideo import tkvideo

ctrl = Controller()

def click_ctrl_W():
    ctrl.press(Key.ctrl)
    ctrl.press('w')
    ctrl.release('w')
    ctrl.release(Key.ctrl)

win = Tk()
global a
a = 0
pg = 0
subject_pg = 0
while True:
    with open('gst.txt', 'r') as gus:
        gst = gus.readlines()
    with open('user.txt', 'r') as us:
        usr = us.readlines()
    if pg == 0:
        if gst == ['0']:
            time.sleep(1)
            a = 0
            exit()
        if gst == ['1']:
            os.system(r'files\ch1.pdf')
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
        if gst == ['0']:
            click_ctrl_W()
            pg = 0
            a = 0
        if gst == ['1']:
            '''file: Science'''
            subject_pg = 1 # Science
        if gst == ['2']:
            '''file: Math'''
            subject_pg = 2  # Math
        if gst == ['3']:
            '''file: English'''
            subject_pg = 3  # English
        if gst == ['4']:
            '''file: Social Science'''
            subject_pg = 4  # Social Science
        if gst == ['5']:
            '''file: Hindi'''
            subject_pg = 5  # Hindi
        if subject_pg == 1:
            os.startfile('ch_1_sci.pdf')
            pg = 7
        if subject_pg == 2:
            os.startfile('ch_1_math.pdf')
            pg = 7
        if subject_pg == 3:
            os.startfile('ch_1_eng.pdf')
            pg = 7
        if subject_pg == 4:
            os.startfile('ch_1_geo.pdf')
            pg = 7
        if subject_pg == 5:
            os.startfile('ch_1_hin.pdf')
            pg = 7
    if pg == 7:
        if gst == ['0']:
            time.sleep(1)
            click_ctrl_W()
            pg = 1
        # scrolling
        if gst == ['1']:
            ctrl.press(Key.down)
            ctrl.release(Key.down)
            time.sleep(0.1)
        if gst == ['2']:
            ctrl.press(Key.up)
            ctrl.release(Key.up)
            time.sleep(0.1)







