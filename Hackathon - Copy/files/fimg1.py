from PIL import ImageTk, Image
from tkinter import *

def img(a):
    win = Tk()
    win.geometry("1366x768")

    frame = Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open(a))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()

    win.mainloop()

while True:
    with open(r'C:\Users\haazi\OneDrive\Desktop\Coding\BRS Hackathon\Hackathon - Copy\pg.txt', 'r') as pug:
        pgt = pug.readlines()
    if pgt == ['1']:
        img('tb.png')