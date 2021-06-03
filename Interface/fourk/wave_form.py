import tkinter as Tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pyaudio
import numpy as np
import threading


def wave(root, cancel, rec):
    def plot_wave():
        class run:
            FORMAT = pyaudio.paFloat32
            CHANNELS = 1
            RATE = 44100
            CHUNK = int(RATE/2)
            START = 0
            N = 512

            wave_x = 0
            wave_y = 0
            spec_x = 0
            spec_y = 0
            data = []

            def __init__(self):
                self.pa = pyaudio.PyAudio()
                self.stream = self.pa.open(format=self.FORMAT,
                                           channels=self.CHANNELS,
                                           rate=self.RATE,
                                           input=True,
                                           output=False,
                                           frames_per_buffer=self.CHUNK)
                # Main loop
                self.loop()

            def loop(self):
                # try:
                while True:
                    self.data = self.audioinput()
                    self.fft()
                    self.graphplot()
                    if cancel == 0 or rec == 0:
                        break

                # except KeyboardInterrupt:
                #     self.pa.close()

            def audioinput(self):
                ret = self.stream.read(self.CHUNK)
                ret = np.fromstring(ret, np.float32)
                return ret

            def fft(self):
                self.wave_x = range(self.START, self.START + self.N)
                self.wave_y = self.data[self.START:self.START + self.N]
                self.spec_x = np.fft.fftfreq(self.N, d=1.0 / self.RATE)
                y = np.fft.fft(self.data[self.START:self.START + self.N])
                self.spec_y = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in y]

            def graphplot(self):
                lines.set_xdata(self.wave_x)
                lines.set_ydata(self.wave_y)
                canvas.draw()
                bx.set_xlim(0, self.RATE/2)
                bx.set_ylim(0, 50)
                lines1.set_xdata(self.spec_x)
                lines1.set_ydata(self.spec_y)
                canvas.draw()

        thread = threading.Thread(target=run)
        thread.start()

    fig = plt.figure()
    ax, bx = fig.subplots(2)
    ax.set_xlim(0, 500, "")
    ax.set_ylim(-0.5, 0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    bx.set_xticks([])
    bx.set_yticks([])
    lines = ax.plot([], [])[0]
    lines1 = bx.plot([], [])[0]
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=190, y=410, width=1620, height=300)
    canvas.draw()

    plot_wave()


def default_wave(root):
    fig = plt.figure()
    ax, bx = fig.subplots(2)
    ax.set_xticks([])
    ax.set_yticks([])
    bx.set_xticks([])
    bx.set_yticks([])
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=190, y=410, width=1620, height=300)
    canvas.draw()
