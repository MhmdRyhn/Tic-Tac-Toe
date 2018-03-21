import tkinter as tk
from PIL import ImageTk as itk
from PIL import Image as im


class AboutGame(tk.Frame):
    def __init__(self,parent):

        self.parnt = parent
        self.parnt.title("About the Game")
        # self.parnt.geometry('700x250')

        # This function makes window non-resizeable
        # widget.resizable(is_resizable_in_X , is_resizable_in_Y)
        self.parnt.resizable(False,False)


        t='\nThis is a Tic Tac Toe Game.\n'
        t+='It is a simple Game.\n'
        t+='It is quite easy to play.\n'
        t+='People of all ages can enjoy this game.\n'
        t+='Specially it can be most enjoyable to the children.\n'

        # justify='left', this option alligns the text to left
        # justify=['left' , 'right' , 'center'] ; default is 'center'
        self.ruleLabel=tk.Label(self.parnt, text=t, justify='center')
        self.ruleLabel.pack()

        self.b=tk.Button(self.parnt, text='Close', width=15, command=self.parnt.destroy)
        self.b.pack()


