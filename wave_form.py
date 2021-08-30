import  matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def default_wave(root):

    fig = plt.figure()
    ax, bx = fig.subplots(2)
    ax.set_xticks([])
    ax.set_yticks([])
    bx.set_xticks([])
    bx.set_yticks([])
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=90, y=200, width=700, height=120)
    canvas.draw()

