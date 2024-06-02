import ctypes
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

from PIL.ImageDraw import ImageDraw
from PIL.ImageFont import ImageFont

ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Setup
# contrast border thumbnail
ws = Tk()
ws.geometry("1900x900")
# Used to make title of the application
applicationName = 'Rich Text Editor'
ws.title(applicationName)


# create functions
def selected():
    global image_path, image
    image_path = filedialog.askopenfilename(initialdir=os.getcwd())
    image = Image.open(image_path)
    image.thumbnail((1200, 600))
    # imgg = img.filter(ImageFilter.BoxBlur(0))
    image1 = ImageTk.PhotoImage(image)
    canvas2.create_image(605, 306, image=image1)
    canvas2.image = image1

def blur(event):
    global image_path, image1, imgg
    for m in range(0, v1.get() + 1):
        image = Image.open(image_path)
        image.thumbnail((1200, 600))
        imgg = image.filter(ImageFilter.BoxBlur(m))
        image1 = ImageTk.PhotoImage(imgg)
        canvas2.create_image(605, 306, image=image1)
        canvas2.image = image1

def brightness(event):
    global image_path, image2, image3
    for m in range(0, v2.get() + 1):
        image = Image.open(image_path)
        image.thumbnail((1200, 600))
        imgg = ImageEnhance.Brightness(image)
        image2 = imgg.enhance(m)
        image3 = ImageTk.PhotoImage(image2)
        canvas2.create_image(605, 306, image=image3)
        canvas2.image = image3

def contrast(event):
    global image_path, image4, image5
    for m in range(0, v3.get() + 1):
        image = Image.open(image_path)
        image.thumbnail((1200, 600))
        imgg = ImageEnhance.Contrast(image)
        image4 = imgg.enhance(m)
        image5 = ImageTk.PhotoImage(image4)
        canvas2.create_image(605, 306, image=image5)
        canvas2.image = image5
def rotate_image(event):
    global image_path, image6, image7
    image = Image.open(image_path)
    image.thumbnail((1200, 600))
    image6 = image.rotate(int(Rotate_combo.get()))
    image7 = ImageTk.PhotoImage(image6)
    canvas2.create_image(605, 306, image=image7)
    canvas2.image = image7
def flip_image(event):
    global image_path, image8, image9
    image = Image.open(image_path)
    image.thumbnail((1200, 600))
    if Flip_combo.get() == "FLIP LEFT TO RIGHT":
        image8 = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif Flip_combo.get() == "FLIP TOP TO BOTTOM":
        image8 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image9 = ImageTk.PhotoImage(image8)
    canvas2.create_image(605, 306, image=image9)
    canvas2.image = image9


def image_border(event):
    global image_path, image8, image9
    image = Image.open(image_path)
    image.thumbnail((1200, 600))
    if Flip_combo.get() == "FLIP LEFT TO RIGHT":
        image8 = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif Flip_combo.get() == "FLIP TOP TO BOTTOM":
        image8 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image9 = ImageTk.PhotoImage(image8)
    canvas2.create_image(605, 306, image=image9)
    canvas2.image = image9

def TextFont(event):
    global image_path, image8, image9
    image = Image.open(image_path)
    image.thumbnail((1200, 600))
    if Flip_combo.get() == "FLIP LEFT TO RIGHT":
        image8 = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif Flip_combo.get() == "FLIP TOP TO BOTTOM":
        image8 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image9 = ImageTk.PhotoImage(image8)
    canvas2.create_image(605, 306, image=image9)
    canvas2.image = image9
def TextSize(event):
    global image_path, image8, image9
    image = Image.open(image_path)
    image.thumbnail((1200, 600))
    if Flip_combo.get() == "FLIP LEFT TO RIGHT":
        image8 = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif Flip_combo.get() == "FLIP TOP TO BOTTOM":
        image8 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image9 = ImageTk.PhotoImage(image8)
    canvas2.create_image(605, 306, image=image9)
    canvas2.image = image9
def TextPod(event):
    global image_path, image8, image9
    image = Image.open(image_path)
    image.thumbnail((1200, 600))
    if Flip_combo.get() == "FLIP LEFT TO RIGHT":
        image8 = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif Flip_combo.get() == "FLIP TOP TO BOTTOM":
        image8 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image9 = ImageTk.PhotoImage(image8)
    canvas2.create_image(605, 306, image=image9)
    canvas2.image = image9
def selecte8d(event):
    global image_path, image8, image9
    image = Image.open(image_path)
    image.thumbnail((1200, 600))
    if Flip_combo.get() == "FLIP LEFT TO RIGHT":
        image8 = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif Flip_combo.get() == "FLIP TOP TO BOTTOM":
        image8 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image9 = ImageTk.PhotoImage(image8)
    canvas2.create_image(605, 306, image=image9)
    canvas2.image = image9

image1 = None
image3 = None
image5 = None
image7 = None
image9 = None
image11 = None


def save():
    global image_path, imgg, image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11
    # file=None
    ext = image_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}",
                             filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    if file:
        if canvas2.image == image1:
            imgg.save(file)
        elif canvas2.image == image3:
            image2.save(file)
        elif canvas2.image == image5:
            image4.save(file)
        elif canvas2.image == image7:
            image6.save(file)
        elif canvas2.image == image9:
            image8.save(file)
        elif canvas2.image == image11:
            image10.save(file)
        # create labels, scales and comboboxes


blurr = Label(ws, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=15, y=100)
v1 = IntVar()
scale = ttk.Scale(ws, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur)
scale.place(x=150, y=105)

bright = Label(ws, text="Brightness:", font=("ariel 17 bold"))
bright.place(x=8, y=150)
v2 = IntVar()
Scale1 = ttk.Scale(ws, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness)
Scale1.place(x=150, y=155)

contrast = Label(ws, text="Contrast:", font=("ariel 17 bold"))
contrast.place(x=35, y=200)
v3 = IntVar()
Scale2 = ttk.Scale(ws, from_=0, to=10, variable=v3, orient=HORIZONTAL, command=contrast)
Scale2.place(x=150, y=205)

Rotate = Label(ws, text="Rotate:", font=("ariel 17 bold"))
Rotate.place(x=60, y=250)
values = [0, 90, 180, 270, 360]
Rotate_combo = ttk.Combobox(ws, values=values, font=('ariel 10 bold'))
Rotate_combo.place(x=150, y=255)
Rotate_combo.bind("<<ComboboxSelected>>", rotate_image)

Flip = Label(ws, text="Flip:", font=("ariel 17 bold"))
Flip.place(x=90, y=300)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
Flip_combo = ttk.Combobox(ws, values=values1, font=('ariel 10 bold'))
Flip_combo.place(x=150, y=305)
Flip_combo.bind("<<ComboboxSelected>>", flip_image)

border = Label(ws, text="Add border:", font=("ariel 17 bold"))
border.place(x=8, y=350)
values2 = [i for i in range(10, 45, 5)]
Border_combo = ttk.Combobox(ws, values=values2, font=("ariel 10 bold"))
Border_combo.place(x=150, y=355)
Border_combo.bind("<<ComboboxSelected>>", image_border)

fonts = Label(ws, text="Text Font:", font=("ariel 17 bold"))
border.place(x=890, y=350)


sizes= Label(ws, text="Text size:", font=("ariel 17 bold"))
border.place(x=8, y=350)

pods = Label(ws, text="Add border:", font=("ariel 17 bold"))
border.place(x=8, y=350)

# create canvas to display image
canvas2 = Canvas(ws, width="1200", height="600", relief=RIDGE, bd=2)
canvas2.place(x=500, y=60)
# create buttons
button1 = Button(ws, text="Select Image", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
                 command=selected)
button1.place(x=495, y=845)
button2 = Button(ws, text="Save", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=save)
button2.place(x=675, y=845)
button3 = Button(ws, text="Exit", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
                 command=ws.destroy)
button3.place(x=855, y=845)
ws.mainloop()