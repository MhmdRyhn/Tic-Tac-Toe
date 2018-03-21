import tkinter as tk
import PlayerSettings as ps
import BoardSettings as bs
import Author as ainf
import GameRule as gr
import TheGame as tg
from math import ceil

class Game(tk.Frame):

    def __init__(self,parent): #constructor of 'Game' class
        # tk.Frame.__init__(self,parent)

        self.parnt=parent
        self.parnt.title("Tic Tac Toe")
        # This function makes window non-resizeable
        # widget.resizable(is_resizable_in_X , is_resizable_in_Y)
        self.parnt.resizable(False, False)

        # Player Info ************************
        self.player1name = 'Player 1'
        self.player2name = 'Player 2'
        self.player1sysbol = 'x'
        self.player2sysbol = 'o'

        self.boardSize = 3
        self.latestBoardSize=self.boardSize
        self.noOfMatch = 3

        self.totalPlayed = 0
        self.p1score = 0
        self.p2score = 0

        self.turn = 0
        self.cnt=0
        self.filledEntry = 0
        self.winner = 'NoBody'
        self.winningPoint='None'
        #######################################

        # Menubar********************************
        self.menubar=tk.Menu(self.parnt)
        ##########################################

        # 'settings' menu *************************************************************
        self.settingsOption=tk.Menu(self.menubar, tearoff=0)
        self.settingsOption.add_command(label='Player Settings', command=self.playerSettingsAction)
        self.settingsOption.add_command(label='Board Settins', command=self.boardSettingsAction)
        self.menubar.add_cascade(label='Setings', menu=self.settingsOption)
        ###############################################################################

        # 'about' menu**************************************************************
        self.aboutOption=tk.Menu(self.menubar,tearoff=0)
        self.aboutOption.add_command(label='The Game', command=self.aboutTheGame)
        self.aboutOption.add_command(label='Game Rules', command=self.gameRule)
        self.aboutOption.add_command(label='Author', command=self.authInfo)
        self.menubar.add_cascade(label='About', menu=self.aboutOption)
        #############################################################################

        # without using this method, menubar isn't shown in Frame *************
        self.parnt.config(menu=self.menubar)
        ######################################################################

        # Main (Default) Input board of the game *************************************
        self.r = self.boardSize
        self.c = self.r
        self.boardSize=self.r
        self.board=[[None for x in range(self.c)] for y in range(self.r)]
        for i in range(self.r):
            for j in range(self.c):
                # print(i,j,board[i][j])
                self.board[i][j]=tk.Entry(self.parnt,width=4)
                self.board[i][j].grid(row=i, column=j, padx=10, pady=10)
        ###############################################################################

        # 'Next' button **********************************************************
        self.next=tk.Button(self.parnt,text="Next", command=self.nextButtonAction)
        self.next.grid(row=self.boardSize, column=0, columnspan=ceil(self.boardSize / 2), padx=20, pady=10)
        # self.next.grid(row=self.r, column=0, columnspan=self.r, padx=20, pady=10)
        ###########################################################################

        # "Clear Board" Button ******************************************************************
        self.clrbrd = tk.Button(self.parnt, text='Clear\nBoard',
                                command=lambda: [self.clearBoard()])
        self.clrbrd.grid(row=self.boardSize, column=ceil(self.boardSize / 2),
                         columnspan=int(self.boardSize / 2), padx=5, pady=5)
        ##########################################################################################

        # LabelFrame to show current score *******************************************
        self.scoreBoard = tk.LabelFrame(self.parnt, text="Score Board")
        self.scoreBoard.grid(row=0, column=self.c, rowspan=self.r+1, padx=10, pady=10)
        self.score=tk.Label(self.scoreBoard, text=self.scoreBoardInfo(), justify='left')
        self.score.pack()
        ###############################################################################



    ################################### Start of "Menu" options' Action ########################################

    # 'Player Settings' menu action **********************************************
    def playerSettingsAction(self): # function inside 'Game' class
        self.top=tk.Toplevel(self.parnt)
        self.playerSettingsWindow=ps.playerSettings(self.top)
        self.getVariablePlayerSettings()

    def getVariablePlayerSettings(self): # function inside 'Game' class
        # if self.playerSettingsWindow:
        if self.playerSettingsWindow.winfo_exists():
            self.player1name = self.playerSettingsWindow.p1name
            self.player2name=self.playerSettingsWindow.p2name
            self.player1sysbol = self.playerSettingsWindow.p1symbol
            self.player2sysbol = self.playerSettingsWindow.p2symbol
            self.parnt.after(500, self.getVariablePlayerSettings)
        else:
            self.score['text'] = self.scoreBoardInfo()
            # print('Got real name: ',self.player1name)
    ###############################################################################

    # 'Board Settings' menu action ********************************************************************************
    def boardSettingsAction(self): # function inside 'Game' class
        self.top=tk.Toplevel(self.parnt)
        self.boardSettingsWindow=bs.BoardSettings(self.top)
        self.getVariableBoardSettings()

    def getVariableBoardSettings(self): # function inside 'Game' class
        if self.boardSettingsWindow.winfo_exists():
            # self.latestBoardSize=self.boardSize
            self.boardSize=int(self.boardSettingsWindow.bsize)
            self.noOfMatch=int(self.boardSettingsWindow.match)
            self.parnt.after(100, self.getVariableBoardSettings)
        else:
            self.scoreBoard.grid_forget()
            self.next.grid_forget()
            # print(self.boardSize,self.r, self.noOfMatch)
            if self.boardSize > self.r:
                # print('big')
                # d=self.boardSize-self.r
                for i in range(self.r):
                    for j in range(self.r, self.boardSize):
                        self.board[i].append(None)
                for i in range(self.r):
                    for j in range(self.r, self.boardSize):
                        # self.board[i].append(None)
                        # print(i,j)
                        self.board[i][j]=tk.Entry(self.parnt, width=4)
                        self.board[i][j].grid(row=i, column=j, padx=10, pady=10)

                for i in range(self.r, self.boardSize):
                    self.board.append([None for x in range(self.boardSize)])
                for i in range(self.r, self.boardSize):
                    for j in range(self.boardSize):
                        # self.board[i].append(None)
                        # print(i,j)
                        self.board[i][j]=tk.Entry(self.parnt, width=4)
                        self.board[i][j].grid(row=i, column=j, padx=10, pady=10)

            self.scoreBoard.grid(row=0, column=self.boardSize, rowspan=self.boardSize+1, padx=10, pady=10)
            self.next.grid(row=self.boardSize, column=0, columnspan=ceil(self.boardSize / 2), padx=20, pady=10, sticky=tk.E)
            self.clrbrd.grid(row=self.boardSize, column=ceil(self.boardSize / 2),
                             columnspan=int(self.boardSize / 2), padx=5, pady=5, sticky=tk.W)
    ##############################################################################################################


    # "The Game" menu action ***************************
    def aboutTheGame(self):
        self.top = tk.Toplevel(self.parnt)
        self.rule = tg.AboutGame(self.top)
    ####################################################

    # "Game Rule" menu action [Detail Game Rule] **************
    def gameRule(self):
        self.top = tk.Toplevel(self.parnt)
        self.rule = gr.RulesOfGame(self.top)
    ###########################################################

    # "Author" menu action [Details of Author (Mahmood Al Rayhan)] **********
    def authInfo(self):
        self.top = tk.Toplevel(self.parnt)
        self.author = ainf.AuthorInfo(self.top)
    #########################################################################

    ################################### End of "Menu" options' Action ########################################



    # Score Board Informatin ************************************************
    def scoreBoardInfo(self):
        t=''
        info='Total Match:'+str(self.noOfMatch)+'\n'
        info+='Played Match: '+str(self.totalPlayed)+'\n'
        info+='Remaining: '+str(self.noOfMatch-self.totalPlayed)+'\n\n'
        info+=str(self.player1name)+'\'s Score: '+str(self.p1score)+'\n'
        info += str(self.player2name) + '\'s Score: ' + str(self.p2score) + '\n'
        info+='Draw: '+str(self.totalPlayed -(self.p1score+self.p2score))

        if self.cnt==self.boardSize:
            info+='\nwinner: '+self.winner
            if self.winningPoint!='None':
                info+='\nWinning point: '+self.winningPoint
        elif self.turn != self.boardSize * self.boardSize:
            if self.turn%2:
                info+='\n'+self.player2name+'\'s turn'
            else:
                info += '\n'+self.player1name + '\'s turn'
        else:
            info+='\nwinner: '+self.winner

        # When all the matches are played
        if self.noOfMatch == self.totalPlayed:
            self.summaryRes()

        return info
    ################################################################################################

    # if self.noOfMatch == self.totalPlayed *********************
    def summaryRes(self):
        if self.p1score > self.p2score:
            t = '\nFinally ' + self.player1name + ' has won\n'
        elif self.p1score < self.p2score:
            t = '\nFinally ' + self.player2name + ' has won\n'
        else:
            t = '\nFinally the matches are draw\n'

        self.rt = tk.Toplevel(self.parnt)
        self.rt.title('Match result')
        self.msg = tk.Label(self.rt, text=t)
        self.msg.pack()
        d = lambda: [self.reset(), self.rt.destroy()]
        self.btn = tk.Button(self.rt, text='Ok', command=d)
        self.btn.pack()
    ############################################################


    # Clearing the board entry*****************************
    def clearBoard(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                # self.board[i][j].insert(0,'')
                # self.board[i][j].grid_forget()
                self.board[i][j].delete(0,'end')

        self.winningPoint='None'
        self.winner='NoBody'
        self.cnt=0
        self.turn=0
        self.score['text']=self.scoreBoardInfo()
    #######################################################

    # Resetting the score related variable **********************
    def reset(self):
        self.totalPlayed = 0
        self.p1score = 0
        self.p2score = 0
        #*****************************
        self.filledEntry = 0
        self.winningPoint = 'None'
        #*****************************
        self.score['text'] = self.scoreBoardInfo()
    ###########################################################


    # "Next Button" action ************************************************************************************
    def nextButtonAction(self): # function inside 'Game' class
        self.fromBoard=[[None for x in range(self.boardSize)] for y in range(self.boardSize)]

        # Check if any invalid symbol
        self.a=False
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                self.fromBoard[i][j]=self.board[i][j].get()
                # if there is any invalid symbol, give a warning
                if self.fromBoard[i][j]!='x' and self.fromBoard[i][j]!='o' and self.fromBoard[i][j]!='':
                    self.a=True
                    t = 'Invalid Symbol in Row '+str(i+1)+', Column '+str(j+1)
                    self.rt=tk.Toplevel(self.parnt)
                    self.rt.title('Warning')
                    self.msg = tk.Label(self.rt, text=t)
                    self.msg.pack()
                    self.btn=tk.Button(self.rt, text='Ok', command=self.rt.destroy)
                    self.btn.pack()
                    return

        # When there is no invalid symbol
        self.turn=0
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                self.fromBoard[i][j]=self.board[i][j].get()
                if self.fromBoard[i][j]=='x' or self.fromBoard[i][j]=='o':
                    self.turn+=1

        #** Evaluate after inputting to each entry **#
        self.cnt=0
        # check for any row matches #
        for i in range(self.boardSize):
            self.cnt=1
            for j in range(1, self.boardSize):
                if self.fromBoard[i][j]==self.fromBoard[i][0] and self.fromBoard[i][0]!='':
                    self.cnt+=1
                else:
                    break
            if self.cnt==self.boardSize:
                self.winningPoint = 'Row ' + str(i + 1)
                if self.fromBoard[i][0]=='x':
                    self.p1score+=1
                    self.winner=self.player1name
                else:
                    self.p2score+=1
                    self.winner = self.player2name
                break

        # if there is any row match
        if self.cnt == self.boardSize:
            # print('someone won')
            self.totalPlayed += 1
            self.score['text'] = self.scoreBoardInfo()
            return
        # end checking row

        # check for any column matches #
        for i in range(self.boardSize):
            self.cnt=1
            for j in range(1, self.boardSize):
                if self.fromBoard[j][i]==self.fromBoard[0][i] and self.fromBoard[0][i]!='':
                    self.cnt+=1
                else:
                    break
            if self.cnt==self.boardSize:
                self.winningPoint = 'Column ' + str(i + 1)
                if self.fromBoard[0][i]=='x':
                    self.p1score+=1
                    self.winner = self.player1name
                else:
                    self.p2score+=1
                    self.winner = self.player2name
                break

        # if there is any column match
        if self.cnt == self.boardSize:
            # print('someone won')
            self.totalPlayed += 1
            self.score['text'] = self.scoreBoardInfo()
            return
        # end checking column

        # check for diagonal match #
        self.cnt=1
        for i in range(1,self.boardSize):
            if self.fromBoard[i][i]==self.fromBoard[0][0] and self.fromBoard[0][0]!='':
                self.cnt+=1
        if self.cnt == self.boardSize:
            if self.fromBoard[0][0] == 'x':
                self.winningPoint = 'Diagonal'
                self.p1score += 1
                self.winner = self.player1name
            else:
                self.p2score += 1
                self.winner = self.player2name

        # if the diagonal matches
        if self.cnt == self.boardSize:
            # print('someone won')
            self.totalPlayed += 1
            self.score['text'] = self.scoreBoardInfo()
            return
        # end cheeking diagonal

        # check for reverse diagonal match #
        self.cnt = 1
        for i in range(1, self.boardSize):
            if self.fromBoard[i][self.boardSize-1-i] == self.fromBoard[0][self.boardSize-1] \
                    and self.fromBoard[0][self.boardSize-1]!='':
                self.cnt += 1
        if self.cnt == self.boardSize:
            self.winningPoint = 'Reverse\n                       Diagonal'
            if self.fromBoard[0][self.boardSize-1] == 'x':
                self.p1score += 1
                self.winner = self.player1name
            else:
                self.p2score += 1
                self.winner = self.player2name

        # if the reverse diagonal matches
        if self.cnt == self.boardSize:
            # print('someone won')
            self.totalPlayed += 1
            self.score['text'] = self.scoreBoardInfo()
            return
        # end cheeking reverse diagonal

        # if there i no matching, i.e. match DRAW
        # self.totalPlayed+=1
        self.score['text'] = self.scoreBoardInfo()

        # if the board is full
        if self.turn==self.boardSize*self.boardSize:
            self.totalPlayed+=1
            self.winner='NoBody'
            self.score['text']=self.scoreBoardInfo()



        return
    ######################### End "Next Button" Action ##########################################################



def main():
    root=tk.Tk()
    Game(root)
    root.mainloop()

main()