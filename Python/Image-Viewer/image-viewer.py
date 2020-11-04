import os
import tkinter as tk
from PIL import Image, ImageTk
from resizeimage import resizeimage


window = tk.Tk()
window.title("Image Viewer")
window.geometry("300x300")

picture = input("Drag 'n Drop picture here >> ")

resized = resizeimage.resize_cover(Image.open(picture), [300,300])
img_render = ImageTk.PhotoImage(resized)
img = tk.Label(window, image=img_render)
img.pack()

window.mainloop()
