import tkinter as tk
from PIL import ImageTk as itk
from PIL import Image as im


class AuthorInfo(tk.Frame):
    def __init__(self,parent):
        # tk.Frame.__init__(self, parent)

        self.parnt = parent
        self.parnt.title("About Author")
        self.parnt.geometry('700x250')

        # This function makes window non-resizeable
        # widget.resizable(is_resizable_in_X , is_resizable_in_Y)
        self.parnt.resizable(False,False)

        # Getting the image
        # path of image
        self.path='image/rayhan.JPG'
        # opens image from the specified 'path'
        self.myImage=im.open(self.path)
        # resize the image into preferred ssize
        self.myImage=self.myImage.resize((250,160),im.ANTIALIAS)
        # load the image
        self.myPhoto=itk.PhotoImage(self.myImage)
        #************ End getting image *****************************

        # Label for displaying image
        self.imageLabel=tk.Label(self.parnt,image=self.myPhoto)
        # This keeps a reference to the image
        # Without keeping the reference, image don't show up in window
        self.imageLabel.image=self.myPhoto # keep a reference
        self.imageLabel.grid(row=0, column=0, padx=5, pady=20)
        #*************************************************************

        t='Tic-Tac-Toe (c) Copyright 2018-Present Mahmood Al Rayhan\n\n'
        t+='Mahmood Al Rayhan\n'
        t+='Dept. of Computer Science & Engineering\n'
        t+='Rajshahi University of Engineering & Technology (RUET)\n'
        t+='Rajshahi, Bangladesh'
        # justify='left', this option alligns the text to left
        # justify=['left' , 'right' , 'center'] ; default is 'center'
        self.infoLabel=tk.Label(self.parnt, text=t, justify='left')
        self.infoLabel.grid(row=0, column=1, padx=20, pady=20)

        self.b=tk.Button(self.parnt, text='Close', width=15, command=self.parnt.destroy)
        self.b.grid(row=1, column=0, columnspan=2)


'''
root=tk.Tk()
AuthorInfo(root)
root.mainloop()
'''


