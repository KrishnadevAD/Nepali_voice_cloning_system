import tkinter as tk
root = tk.Tk()
if root.winfo_screenwidth()==1366 and root.winfo_screenheight()==768:
    from interface import *
    hd(root)
# elif root.winfo_screenwidth()==1920 and root.winfo_screenheight()==1080:
#     fullhd(root)
elif root.winfo_screenwidth()==3840 and root.winfo_screenheight()==2160:
    from fourk.interface import *
    fourk(root)
