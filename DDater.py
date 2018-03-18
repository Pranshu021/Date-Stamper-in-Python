
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from PIL import Image, ImageDraw, ImageFont
import os, platform

root = Tk()
root.title('DDater')


def Filer():
    global filename
    filename = filedialog.askdirectory()

    if filename:
        try:
            global file_name
            file_name = Label(main_frame, text=str(filename)).grid(row=1, column=1, padx=40)
        except:
            tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename)
            return

def Stampit():
    if platform.system().lower() == 'linux':
        font_location = '/usr/share/fonts/truetype/dejavu'
    if platform.system().lower() == 'windows':
        font_location = 'C:\Windows\Fonts'
    os.makedirs(os.path.join(filename, 'Ddater'), exist_ok=True)
    os.chdir(str(filename) + '/Ddater')
    for hello in os.listdir(filename):
        x = str(hello)
        if not(hello.endswith('.png') or hello.endswith('.jpg') or hello.endswith('.jpeg') or hello.endswith('.JPG')):
            continue


        edited = Image.open(os.path.join(filename, x))
        image_width, image_height = edited.size
        if image_width < 800:
            my_font = ImageFont.truetype(os.path.join(font_location, 'Arial.ttf'), int(image_height/40))
        if image_width > 800:
            my_font = ImageFont.truetype(os.path.join(font_location, 'Arial.ttf'), int(image_height/30))
        if image_width > 1080:
            my_font = ImageFont.truetype(os.path.join(font_location, 'Arial.ttf'), int(image_height/25))

        draw = ImageDraw.Draw(edited)
        draw.text((int(image_width-int(image_width/5)),int(image_height-int(image_height/10))), str(day_field.get() + '-' + month_field.get() + '-' + year_field.get()), fill='orange', font=my_font)
        try:
            edited.save(x)
            i = 0;
        except:
            i = 1;

    if i == 0:
        tkinter.messagebox.showinfo('Success !', 'Images Stamped Successfuly !')
    else:
        tkinter.messagebox.showerror('Failed !', 'Images Could not be Stamped !')


main_frame = Frame(root, width=2, height=4)
main_frame.pack()

files_name = Label(main_frame, text="Specify Folder :")
files_name.grid(row=0, sticky=E, padx=50, pady=30)
files = Button(main_frame, text='Open Files', command=Filer)
files.grid(row=0, column=1, sticky=E, padx=50)
dates = Label(main_frame, text="Enter date : ")
dates.grid(row=2, sticky=E, padx=50, pady=40)
day_field = Entry(main_frame, width=2)
day_field.grid(row=2,sticky=E)
month_field = Entry(main_frame, width=2)
month_field.grid(row=2, column=1, padx=20 ,sticky=W)
year_field = Entry(main_frame, width=3)
year_field.grid(row=2, column=1, padx=60, sticky=W)

stamper = Button(main_frame, text="Stamp the Date", command=Stampit)
stamper.grid(row=3, column=1, padx=(0,40), pady=10, ipadx=30, sticky=W)

root.mainloop()