import tkinter as tk


class playerSettings(tk.Frame):
    def __init__(self,parent=tk.Frame):
        tk.Frame.__init__(self,parent)

        self.parnt=parent
        self.parnt.title("Player Setting")

        # This function makes window non-resizeable
        # widget.resizable(is_resizable_in_X , is_resizable_in_Y)
        self.parnt.resizable(False, False)

        self.p1name='Player 1'
        self.p2name='Player 2'
        self.p1symbol='x'
        self.p2symbol='o'

        # 'Player 2: Name' label and entry
        self.p1NameLabel = tk.Label(self.parnt, text='Player 1: Name ')
        self.p1NameLabel.grid(row=0, column=0, padx=5, pady=5)
        self.p1NameEntry = tk.Entry(self.parnt)
        self.p1NameEntry.insert(0,self.p1name)
        self.p1NameEntry.bind('<FocusIn>', lambda event:self.p1NameEntry.delete(0,'end'))
        self.p1NameEntry.grid(row=0, column=1, padx=5, pady=5)
        # **********************
        # Player 1 'Symbol'
        self.p1SymbolLabel = tk.Label(self.parnt, text='Symbol ')
        self.p1SymbolLabel.grid(row=0, column=2, padx=5, pady=5)
        self.p1SymbolEntry = tk.Entry(self.parnt)
        self.p1SymbolEntry.insert(0, self.p1symbol)
        self.p1SymbolEntry.bind('<FocusIn>', lambda event: self.p1SymbolEntry.delete(0, 'end'))
        self.p1SymbolEntry.grid(row=0, column=3, padx=5, pady=5)
        #*****************

        # 'Player 2: Name' label and entry
        self.p2NameLabel = tk.Label(self.parnt, text='Player 2: Name ')
        self.p2NameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.p2NameEntry = tk.Entry(self.parnt)
        self.p2NameEntry.insert(0, self.p2name)
        self.p2NameEntry.bind('<FocusIn>', lambda event: self.p2NameEntry.delete(0, 'end'))
        self.p2NameEntry.grid(row=1, column=1, padx=5, pady=5)
        #****************
        # Player 2 'Symbol'
        self.p2SymbolLabel = tk.Label(self.parnt, text='Symbol ')
        self.p2SymbolLabel.grid(row=1, column=2, padx=5, pady=5)
        self.p2SymbolEntry = tk.Entry(self.parnt)
        self.p2SymbolEntry.insert(0, self.p2symbol)
        self.p2SymbolEntry.bind('<FocusIn>', lambda event: self.p2SymbolEntry.delete(0, 'end'))
        self.p2SymbolEntry.grid(row=1, column=3, padx=5, pady=5)
        #**********************

        # 'Apply Settings' Button
        self.apply=tk.Button(self.parnt, text="Apply Settings", fg='black', bg='green', command=self.applyButtonAction)
        self.apply.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=tk.E)
        # *****************

        # 'Ok' Button
        self.ok=tk.Button(self.parnt, text='Ok', fg='black', bg='green', state=tk.DISABLED, command=self.parnt.destroy)
        self.ok.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky=tk.W)
        # ***************


    def applyButtonAction(self):
        self.p1name=self.p1NameEntry.get()
        self.p2name=self.p2NameEntry.get()
        self.p1symbol=self.p1SymbolEntry.get()
        self.p2symbol=self.p2SymbolEntry.get()

        self.ok['state']=tk.NORMAL

        # 'Apply Settings' button is disabled after clicking it
        self.apply['state']=tk.DISABLED
        self.apply['bg']='white'
        self.apply['fg']='black'
        # **************

