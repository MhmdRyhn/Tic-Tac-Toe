import tkinter as tk
from PIL import ImageTk as itk
from PIL import Image as im


class RulesOfGame(tk.Frame):
    def __init__(self,parent):

        self.parnt = parent
        self.parnt.title("Game Rule")
        # self.parnt.geometry('700x250')

        # This function makes window non-resizeable
        # widget.resizable(is_resizable_in_X , is_resizable_in_Y)
        self.parnt.resizable(False,False)


        t='\nHow to play:\n\n'
        t+='1. Score Board is at the Right side of the Game Board\n'
        t+='    This will show the latest Score Update\n'
        t+='2. At the bottom of the Score Board, \"Player\'s turn\" will be shown\n'
        t+='    (Always keep watching the Score Board)'
        t+='3. Directed Player will input to the Entry one at a time and click \"Next\" button\n'
        t+='4. Press \"Next\" Button after giving input to each Entry\n'
        t+='5. If someone wins, it will show in the Score Board\n'
        t+='6. A popup window will be shown after the end of the tournament\n'

        # justify='left', this option alligns the text to left
        # justify=['left' , 'right' , 'center'] ; default is 'center'
        self.ruleLabel=tk.Label(self.parnt, text=t, justify='left')
        self.ruleLabel.pack()

        self.b=tk.Button(self.parnt, text='Close', width=15, command=self.parnt.destroy)
        self.b.pack()


