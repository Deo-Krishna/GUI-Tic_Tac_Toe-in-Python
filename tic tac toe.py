from tkinter import *
import tkinter.messagebox as tmsg
import os

def callback(r,c):
    global player

    if player=='X' and states[r][c]==0 and stop_game == False:
        b[r][c].configure(text='X' ,fg='blue',bg='white')
        states[r][c] ='X'
        player= 'O'
        check_for_winner('X')

    if player=='O' and states[r][c]==0 and stop_game == False:
        b[r][c].configure(text='O' ,fg='orange',bg='black')
        states[r][c] ='O'
        player= 'X'   
        check_for_winner('O')

def check_for_winner(xo):
    global stop_game
    for i in range (3):
        if states[i][0] == states[i][1]==states[i][2]!=0:
            b[i][0].config(bg='grey')
            b[i][1].config(bg='grey')
            b[i][2].config(bg='grey')
            stop_game =True
            print(f"THE WINNER IS {xo}")
            tmsg.showinfo("winner",f"THE WINNER IS     {xo}")
    for i in range (3):
        if states[0][i] == states[1][i]==states[2][i]!=0:
            b[0][i].config(bg='grey')
            b[1][i].config(bg='grey')
            b[2][i].config(bg='grey')
            stop_game =True
            print(f"THE WINNER IS {xo}")
            tmsg.showinfo("winner",f"THE WINNER IS      {xo}")
        if states[0][0]==states[1][1]==states[2][2]!=0:
            b[0][0].config(bg='grey')
            b[1][1].config(bg='grey')
            b[2][2].config(bg='grey')
            stop_game =True
            print(f"THE WINNER IS {xo}")
            tmsg.showinfo("winner",f"THE WINNER IS       {xo}")
        if states[2][0]==states[1][1]==states[0][2]!=0:
            b[2][0].config(bg='grey')
            b[1][1].config(bg='grey')
            b[0][2].config(bg='grey')
            stop_game =True
            print(f"THE WINNER IS {xo}")
            tmsg.showinfo("winner",f"THE WINNER IS       {xo}")
    
root = Tk()
root.title("Tic Tac Toe by DEO")
root.geometry("594x495")
root.minsize(594,495)
root.maxsize(594,495)

def restart():
    root.destroy()
    os.startfile("ttt.py")

b= [[0,0,0],
    [0,0,0],
    [0,0,0]]
states= [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(3):
    for j in range (3):
        b[i][j]= Button(font=("Arial",60),width=4,bg='powder blue',command= lambda r=i, c=j: callback(r,c))
        b[i][j].grid(row=i,column=j, sticky=E)
player='X'
stop_game = False

Button(root,bg="black", fg="white",width=27,  text="RESTART", command=restart).grid(row=3,column=1)

root.mainloop()