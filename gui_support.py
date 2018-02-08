#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Oct 12, 2017 07:53:10 PM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

from PIL import Image, ImageTk
from lib import plotutil as plu

# Global variable to check if any function has been plotted
plotted = False


def Plot(fx, xpoints, color_name, theme, canvas, line_style, file_path,discrete=False):

    global plotted
    if fx:
        plu.plot(fx, xpoints, color_name, 'X-axis', 'Y-axis', theme, True, line_style, file_path,discrete)
        image = Image.open(".temp/generated_plot.png").resize(
            (canvas.winfo_width(), canvas.winfo_height()))
        gif1 = ImageTk.PhotoImage(image, Image.ANTIALIAS)
        canvas.create_image(0, 0, image=gif1, anchor=NW)
        canvas.gif1 = gif1
        plotted = True
    else:
        canvas.delete(ALL)

    sys.stdout.flush()

# def Plot_discrete(fx, xpoints, color_name, theme, canvas, line_style, file_path):

#     global plotted
#     if fx:
#         plu.plot(fx, xpoints, color_name, 'X-axis', 'Y-axis', theme, True, line_style, file_path,True)
#         image = Image.open(".temp/generated_plot.png").resize(
#             (canvas.winfo_width(), canvas.winfo_height()))
#         gif1 = ImageTk.PhotoImage(image, Image.ANTIALIAS)
#         canvas.create_image(0, 0, image=gif1, anchor=NW)
#         canvas.gif1 = gif1
#         plotted = True
#     else:
#         canvas.delete(ALL)

#     sys.stdout.flush()

def Plot_line(arrays, color_name, theme, canvas, line_style, file_path):

    global plotted
    if arrays:
        plu.plot_line(arrays, color_name, 'X-axis', 'Y-axis', theme, True, line_style, file_path)
        image = Image.open(".temp/generated_plot.png").resize(
            (canvas.winfo_width(), canvas.winfo_height()))
        gif1 = ImageTk.PhotoImage(image, Image.ANTIALIAS)
        canvas.create_image(0, 0, image=gif1, anchor=NW)
        canvas.gif1 = gif1
        plotted = True
    else:
        canvas.delete(ALL)

    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == "__main__":
    import gui_main
    gui_main.vp_start_gui()
