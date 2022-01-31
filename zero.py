from pymata_aio.pymata3 import PyMata3
import time
import tkinter as tk
from tkinter.font import Font
import os

# create a PyMata instance
# ping callback function
def vr(data):
    # print('hello')
    print('version')
    print(data)

# create a PyMata instance
# create a PyMata instance
mainWin = tk.Tk()
# 視窗標題
mainWin.title("zeroing")

L=[50,51,52,53]
R=[46,47,48,49]
F=[42,43,44,45]
B=[38,39,40,41]
U=[34,35,36,37]
D=[30,31,32,33]
speed=60
rel=200
step=1


wait=[F,B,L,R,U,D]
position=0
myfont=Font(size=35)



firmata = PyMata3(2)




firmata.stepper_config(rel,L)

def start():
	firmata.stepper_step(speed,1)
def see():
	position=position+1
	print(position)
def clo():
	firmata.shutdown()		


sta=tk.Button(mainWin,text="start",font=myfont,command=start)
sta.pack()
se=tk.Button(mainWin,text="set",font=myfont,command=see)
se.pack()
close=tk.Button(mainWin,text="close",font=myfont,command=clo)
close.pack()


def eventhandler(event):
    if event.keysym == 'Left':
        print('按下了方向键左键')
        firmata.stepper_step(speed,5)
    elif event.keysym == 'Right':
        print('按下了方向键右键！')


btn = tk.Button(mainWin, text='button')
btn.bind_all('<KeyPress>', eventhandler)
btn.pack()


mainWin.mainloop()



