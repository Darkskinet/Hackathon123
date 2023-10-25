import tkinter as tk
from tkvideo import tkvideo

def start(file):
    root = tk.Tk()
    # root.geometry("640x480")
    root.attributes('-fullscreen', True)
    videoPlayer = tk.Label(root)
    videoPlayer.pack()
    video = tkvideo(file + ".mp4", videoPlayer, loop=1, size=(1366,768))
    video.play()
    root.mainloop()



while True:
    with open('user.txt', 'r') as us:
        usr = us.readlines()
    with open('pg.txt', 'r') as pug:
        pgt = pug.readlines()
    if usr == ['User 1']:
        if pgt == ['0']:
            start("hp")
