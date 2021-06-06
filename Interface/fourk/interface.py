from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
import time
import threading
from wave_form import wave, default_wave
import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import messagebox,ttk
import sys
import ctypes

def fourk(win):
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

    print("screen resolution is {} by {}".format(w, h))


    # root widget
    win.resizable(0, 0)
    win.title("Nepali AI Anchor")
    # Window size
    appWidth = 1920
    appHeight = 1080
    font = "Times New Roman"

    # option
    option = ["05 sec", "10 sec", "20 sec ", "30 sec", "60 sec"]

    screenWidth = win.winfo_screenwidth()
    screenHeight = win.winfo_screenheight()


    x = int((screenWidth / 2) - (appWidth / 2))
    y = int((screenHeight / 2) - (appHeight / 2))

    # window pops up on center of the screen
    win.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

    # label widget
    myLabel1 = Label(win, text="Nepali AI Anchor",
                     font=("Calibri", 20), fg="Blue", anchor=N)  # Title
    myLabel2 = Label(win, text="Modern Anchor Reimagined")  # Motto


    # Print on Screen
    myLabel1.grid(row=0, column=0, sticky="nsew")
    myLabel2.grid(row=1, column=0, sticky="nsew", pady=(2, 8))


    # alert when closing window

    def warn():
        if messagebox.askquestion("Confirm", "Are you sure?") == 'yes':
            win.destroy()
            sys.exit("exit")


    # import audio file
    def import_file():
        file = askopenfile(filetypes=[("Audio Files", ".wav .ogg .mp3 ")])
        f = str(file)
        print(f)
        f = f.split("/")
        f = f[-1]
        f_name = f.replace("' mode='r' encoding='UTF-8'>", "")
        if len(f_name) > 15:
            f_name = f_name[:-(len(f_name)-10)]+".wav"
        if file is not None:
            Output.config(text=f_name, font=("Calibri", 10))
            #Output.insert(INSERT,f.replace("' mode='r' encoding='UTF-8'>",""))
            messagebox.showinfo("showinfo", "Uploaded Successfully")

    global wf,rec,cancel
    wf = 1
    rec = 1
    cancel = 1


    def cancel_record():
        global cancel, wf
        cancel = 0
        wf = 1

    # timer


    def record_audio():
        def run():
            global cancel, wf, rec
            rec = 1
            wf = 0
            t_value = variable1.get()
            y = int(t_value[0]+t_value[1])-1
            if cancel == 1:
                button1 = Button(win, text="X", command=cancel_record, anchor=W)
                button1.place(relx=0.81, rely=0.2)

            for i in range(0, int(t_value[0] + t_value[1])):
                timer = y
                if y < 10:
                    timer = "0" + str(y)
                text = Label(text=("00:" + str(timer)))
                text.place(relx=0.65, rely=0.185)
                if pb['value'] != 100:
                    pb['value'] += (100 / int(t_value[0] + t_value[1]))
                    y = y - 1
                    time.sleep(1)
                if cancel == 0:
                    cancel = 1
                    rec = 0
                    pb['value'] = 0
                    default_wave(win)
                    button1.destroy()
                    text.config(text=("00:00"))
                    break
            pb['value'] = 0
            button1.destroy()
            default_wave(win)
            wf = 1
            if rec == 1:
                messagebox.showinfo("showinfo", "Recorded Successfully")

        def run1():
            global wf, cancel

            if wf == 0 and cancel == 1:
                wave(win,cancel,rec)

        def record():
            global rec
            fs = 44100  # Sample rate
            value = variable1.get()
            seconds = int(value[0] + value[1])  # time duration
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            if rec == 1:
                write('output1.wav', fs, myrecording)

        t1 = threading.Thread(target=record)
        t1.daemon = True
        t1.start()
        t2 = threading.Thread(target=run)
        t2.daemon = True
        t2.start()
        t3 = threading.Thread(target=run1)
        t3.daemon = True
        t3.start()

    # Define Buttons


    variable1 = StringVar(win)
    variable1.set(option[0])  # default value
    t_value = variable1.get()

    button_frame = Frame(win, highlightbackground="black",
                         highlightthickness=1)

    originalImg1 = Image.open("browse.png")
    resized1 = originalImg1.resize((55, 75), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(resized1)
    button_import = Button(win, padx=20,
                           pady=5, command=import_file, image=img1)


    Output = Label(text="", height=2,
                   width=15,
                   bg="light cyan")

    # Output=Text(height = 1.5,
    #               width = 15,
    #               bg = "light cyan")
    originalImg = Image.open("microphone.png")
    resized = originalImg.resize((70, 75), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resized)

    button_record = Button(win, padx=20, pady=5, command=record_audio,
                           fg="Red", bg="#e6e6e6", image=img)


    down = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0e\x00\x00\x00\x07\x08\x06\x00\x00\x008G|\x19\x00\x00\x00\tpHYs\x00\x00\x10\x9b\x00\x00\x10\x9b\x01t\x89\x9cK\x00\x00\x00\x19tEXtSoftware\x00www.inkscape.org\x9b\xee<\x1a\x00\x00\x00OIDAT\x18\x95\x95\xce\xb1\x0e@P\x0cF\xe1\xefzI\x8fc$\x12\x111\x19\xec\x9e\x12\xcb\x95 A\x9d\xa4K\xff\x9e\xb6\t\x13J\xffX \xa1\xc7\x16\xac\x19\xc5\xb1!*\x8fy\xf6BB\xf7"\r_\xff77a\xcd\xbd\x10\xedI\xaa\xa3\xd2\xf9r\xf5\x14\xee^N&\x14\xab\xef\xa9\'\x00\x00\x00\x00IEND\xaeB`\x82'
    imgDown = PhotoImage(master=win, data=down)

    # drop_down1
    variable2 = StringVar(win)
    variable2.set("English")
    d1 = OptionMenu(win, variable2, "English", "Nepali")
    d1.configure(indicatoron=0, compound=RIGHT,
                 image=imgDown, width=120, height=60)

    # drop_down2
    d2 = OptionMenu(win, variable1, *option)
    d2.configure(indicatoron=0, compound=RIGHT,
                 image=imgDown, width=120, height=60)

    # progress_bar
    pb = ttk.Progressbar(
        win,
        orient='horizontal',
        mode='determinate',
        length=200,

    )
    # place the progressbar

    pb.place(relx=0.57, rely=0.23)

    # audio waveform
    text = Label(text=("Input Waveform"))
    text.place(relx=0.1, rely=0.33)
    default_wave(win)


    # input text
    inputtxt = Text(win, height=7, width=60)
    inputtxt.insert("end-1c", "Text goes here...(TTS)")
    inputtxt.place(relx=0.1, rely=0.7)


    # generate button

    button_generate = Button(win, text="Generate Audio", padx=20,
                             pady=5)
    button_generate.place(relx=0.79, rely=0.8)


    button_import.place(relx=0.1, rely=0.2)
    Output.place(relx=0.135, rely=0.2)
    button_record.place(relx=0.53, rely=0.2)
    d1.place(relx=0.3, rely=0.2)
    d2.place(relx=0.42, rely=0.2)

    # Center the Content
    win.columnconfigure(0, weight=1)
    win.protocol("WM_DELETE_WINDOW", warn)
    win.mainloop()
