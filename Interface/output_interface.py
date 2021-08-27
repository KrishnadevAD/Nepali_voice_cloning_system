from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
import time
import threading
from  wave_form import wave,default_wave
import sounddevice as sd
from scipy.io.wavfile import write
from  tkinter import  messagebox,ttk
import  sys
from demo_cli import *
import tkinter as tk
win = tk.Tk()


# root widget
win.resizable(0, 0)
win.title("Nepali AI Anchor")
# Window size
appWidth = 852
appHeight = 480
font = "Times New Roman"

#option
option=["05 sec","10 sec", "20 sec ", "30 sec", "60 sec"]
global file_path

screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()


x = int((screenWidth / 2) - (appWidth / 2))
y = int((screenHeight / 2) - (appHeight / 2))

# window pops up on center of the screen
win.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')


win.mainloop()
