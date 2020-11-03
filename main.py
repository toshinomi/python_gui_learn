import tkinter
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from image_process import ImageProcess

def open_image_file(fileName):
    try:
        image = Image.open(open(fileName, 'rb'))
        image.thumbnail((500, 500), Image.ANTIALIAS)
        photoImage = ImageTk.PhotoImage(image)
    except:
        return None
    return photoImage

def file_select():
    fileType = [("すべて","*")]
    filePath = tkinter.filedialog.askopenfilename(filetypes = fileType)

    openImage = open_image_file(filePath)
    if openImage is None:
        messagebox.showinfo('info', 'Cannot open the image file')
        return
        
    canvas.create_image(
        0,
        0,
        image=openImage,
        tag="illust",
        anchor=tkinter.NW
    )
    canvas.photo = openImage

    filePathTextBox.configure(state='normal')
    filePathTextBox.insert(tkinter.END, filePath)
    filePathTextBox.configure(state='readonly')

def image_process():
    try:
        inputImage = Image.open(filePathTextBox.get())
    except:
        messagebox.showinfo('info', 'Cannot open the image file')
        return
    imageProcess = ImageProcess()
    outputImage = imageProcess.gray_scale(inputImage)
    outputImage.thumbnail((500, 500), Image.ANTIALIAS)
    photoImage = ImageTk.PhotoImage(outputImage)

    canvas.create_image(
        0,
        0,
        image=photoImage,
        tag="illust",
        anchor=tkinter.NW
    )
    canvas.photo = photoImage

root = tkinter.Tk()
root.title("Python GUI")
root.geometry("800x600")

imageFileOpenButton = tkinter.Button(text="Open",command=file_select)
imageFileOpenButton.place(x=10, y=40)

imageProcessButton = tkinter.Button(text="Image Process",command=image_process)
imageProcessButton.place(x=80, y=40)

canvas = tkinter.Canvas(
    root,
    width=500,
    height=500,
)
canvas.place(x=10, y=80)
 
openImage = Image.open(open('sample.jpg', 'rb'))
openImage.thumbnail((500, 500), Image.ANTIALIAS)
photoImage = ImageTk.PhotoImage(openImage)
 
canvas.create_image(
    0,
    0,
    image=photoImage,
    tag="illust",
    anchor=tkinter.NW
)

filePathTextBox = tkinter.Entry(width=60)
filePathTextBox.configure(state='readonly')
filePathTextBox.place(x=10, y=10)
filePathTextBox.configure(state='normal')
filePathTextBox.insert(tkinter.END, 'sample.jpg')
filePathTextBox.configure(state='readonly')

root.mainloop()