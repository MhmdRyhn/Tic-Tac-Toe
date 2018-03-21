import tkinter as tk



class BoardSettings(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, parent)

        self.parnt = parent
        self.parnt.title("Board Setting")

        # This function makes window non-resizeable
        # widget.resizable(is_resizable_in_X , is_resizable_in_Y)
        self.parnt.resizable(False, False)

        self.bsize=3
        self.match=5

        # Board Size Label
        self.boardsizelabel=tk.Label(self.parnt, text='Board Size: ')
        self.boardsizelabel.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        # ***********

        # 'Board Size' Entry
        self.boardsizeentry=tk.Entry(self.parnt, width=10)
        self.boardsizeentry.insert(0, self.bsize)
        self.boardsizeentry.bind('<FocusIn>', lambda event: self.boardsizeentry.delete(0,'end'))
        self.boardsizeentry.grid(row=0, column=1, padx=5, pady=5)
        # **************

        # 'No. of Matches' Label
        self.matchlabel = tk.Label(self.parnt, text='No. of Matches: ')
        self.matchlabel.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        # ***********

        # No. of Matches' Entry
        self.matchentry = tk.Entry(self.parnt, width=10)
        self.matchentry.insert(0, self.match)
        self.matchentry.bind('<FocusIn>', lambda event: self.matchentry.delete(0, 'end'))
        self.matchentry.grid(row=1, column=1, padx=5, pady=5)
        # **************

        # 'Apply Settings' Button
        self.apply = tk.Button(self.parnt, text="Apply Settings", fg='black', bg='green', command=self.applyButtonAction)
        self.apply.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        # *****************

        # 'Ok' Button
        self.ok = tk.Button(self.parnt, text='Ok', fg='black', bg='green', state=tk.DISABLED, command=self.parnt.destroy)
        self.ok.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        # ***************


    def applyButtonAction(self):
        self.bsize=self.boardsizeentry.get()
        self.match=self.matchentry.get()

        self.ok['state']=tk.NORMAL

        self.apply['state'] = tk.DISABLED
        self.apply['bg'] = 'white'
        self.apply['fg'] = 'black'
