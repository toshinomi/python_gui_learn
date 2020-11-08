import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from image_process import ImageProcess

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.title("Python GUI")
        master.geometry("800x600")

        self.imageFileOpenButton = tk.Button(text="Open", command=self.file_select)
        self.imageFileOpenButton.place(x=10, y=40)

        self.imageProcessButton = tk.Button(text="Image Process", command=self.image_process)
        self.imageProcessButton.place(x=80, y=40)

        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.place(x=10, y=80)

        self.openImage = Image.open(open('sample.jpg', 'rb'))
        self.openImage.thumbnail((500, 500), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(self.openImage)
 
        self.canvas.create_image(0, 0, image=self.photoImage, tag="illust", anchor=tk.NW)

        self.filePathTextBox = tk.Entry(width=60)
        self.filePathTextBox.configure(state='readonly')
        self.filePathTextBox.place(x=10, y=10)
        self.filePathTextBox.configure(state='normal')
        self.filePathTextBox.delete(0, tk.END)
        self.filePathTextBox.insert(tk.END, 'sample.jpg')
        self.filePathTextBox.configure(state='readonly')

    def open_image_file(self, fileName):
        try:
            image = Image.open(open(fileName, 'rb'))
            image.thumbnail((500, 500), Image.ANTIALIAS)
            photoImage = ImageTk.PhotoImage(image)
        except:
            return None
        return photoImage

    def file_select(self):
        fileType = [("すべて","*")]
        filePath = tk.filedialog.askopenfilename(filetypes = fileType)

        openImage = self.open_image_file(filePath)
        if openImage is None:
            messagebox.showinfo('info', 'Cannot open the image file')
            return
            
        self.canvas.create_image(0, 0, image=openImage, tag="illust", anchor=tk.NW)
        self.canvas.photo = openImage

        self.filePathTextBox.configure(state='normal')
        self.filePathTextBox.delete(0, tk.END)
        self.filePathTextBox.insert(tk.END, filePath)
        self.filePathTextBox.configure(state='readonly')

    def image_process(self):
        try:
            inputImage = Image.open(self.filePathTextBox.get())
        except:
            messagebox.showinfo('info', 'Cannot open the image file')
            return
        imageProcess = ImageProcess()
        outputImage = imageProcess.gray_scale(inputImage)
        outputImage.thumbnail((500, 500), Image.ANTIALIAS)
        photoImage = ImageTk.PhotoImage(outputImage)

        self.canvas.create_image(0, 0, image=photoImage, tag="illust", anchor=tk.NW)
        self.canvas.photo = photoImage

def main():
    window = tk.Tk()
    applicaion = Application(master=window)
    applicaion.mainloop()

if __name__ == "__main__":
    main()