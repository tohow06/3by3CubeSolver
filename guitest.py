import tkinter as tk
from tkinter.font import Font
from rubik_solver import utils
import pycuber as pc
from pycuber.solver import CFOPSolver
import os


# 步驟二：建立主視窗。
mainWin = tk.Tk()
# 視窗標題
mainWin.title("Cube Robot")
# 視窗大小


mainWin.geometry("1024x768")
mainWin.config(bg='#DCDCDC')




mouseColor=''
cans=[]
panel=[]
boxsize=50
color=['yellow','red','green','orange','blue','white']
ctext=['y','r','g','o','b','w']
fsize=Font(size=20)
myfont=Font(size=35)
doList=[]

def change(event):
	global mouseColor
	x=int(event.x_root/50)+1
	y=int(event.y_root/50)
	num=0
	if y <= 3:
		num=x-3+(y-1)*3-1
	elif y <= 6 and x<=3:
		num=9+(y-4)*3+x-1
	elif y <= 6 and x<=6:
		num=18+(y-4)*3+x-3-1
	elif y <= 6 and x<=9:
		num=27+(y-4)*3+x-6-1
	elif y <= 6 and x<=12:
		num=36+(y-4)*3+x-9-1
	else:
		num=45+(y-7)*3+x-3-1
	cans[num].config(bg=mouseColor)			
	return



for i in range(54):
	cans.append(tk.Canvas(mainWin,bd=0,width=boxsize,height=boxsize,bg="gray"))
for i in range(9):
	cans[i].place(x=(i%3+3)*50,y=(int(i/3))*50)
	cans[i].bind("<Button-1>", change)		
for i in range(9,18):
	cans[i].place(x=(i%3)*50,y=(int(i/3))*50)	
	cans[i].bind("<Button-1>", change)
for i in range(18,27):
	cans[i].place(x=(i%3+3)*50,y=(int(i/3)-3)*50)
	cans[i].bind("<Button-1>", change)
for i in range(27,36):
	cans[i].place(x=(i%3+6)*50,y=(int(i/3)-6)*50)
	cans[i].bind("<Button-1>", change)
for i in range(36,45):
	cans[i].place(x=(i%3+9)*50,y=(int(i/3)-9)*50)
	cans[i].bind("<Button-1>", change)			
for i in range(45,54):
	cans[i].place(x=(i%3+3)*50,y=(int(i/3)-9)*50)
	cans[i].bind("<Button-1>", change)	

cans[4].config(bg="yellow")
cans[13].config(bg="blue")
cans[22].config(bg="red")
cans[31].config(bg="green")
cans[40].config(bg="orange")
cans[49].config(bg="white")


def changeMouse(k):
	global	mouseColor
	mouseColor=color[k]


panel.append(tk.Button(mainWin,text=ctext[0],font=(fsize),width=5,command=lambda:changeMouse(0)))
panel.append(tk.Button(mainWin,text=ctext[1],font=(fsize),width=5,command=lambda:changeMouse(1)))
panel.append(tk.Button(mainWin,text=ctext[2],font=(fsize),width=5,command=lambda:changeMouse(2)))
panel.append(tk.Button(mainWin,text=ctext[3],font=(fsize),width=5,command=lambda:changeMouse(3)))
panel.append(tk.Button(mainWin,text=ctext[4],font=(fsize),width=5,command=lambda:changeMouse(4)))
panel.append(tk.Button(mainWin,text=ctext[5],font=(fsize),width=5,command=lambda:changeMouse(5)))
for i in range(6):
	panel[i].place(x=330+i*75,y=400)


var=tk.StringVar()

cubeColor=""

def solco():
	global cubeColor
	global doList
	for c in cans:
		cubeColor=cubeColor+c['bg'][0]	
	print(cubeColor)
	doList=utils.solve(cubeColor,'Kociemba')
	doList=list(map(str,doList))
	var.set(doList)
	print(doList)

texting=tk.Label(mainWin,textvariable=var,font=myfont,bg="#C0C0C0")
texting.pack(side='bottom')

def convertForToList(f):
	l=str(f).split(' ')
	return l


def rando():
	global doList
	random_alg = pc.Formula().random()
	var.set(random_alg)
	doList=convertForToList(random_alg)
	print(doList)



def rota():
	global doList
	str1 = ' '.join(str(e) for e in doList)
	os.system('python testrotate.py "%s"' %(str1))
	print("~~~~~~~~~~~move complete ~~~~~~~~~~~")

def solra():
	global doList
	str1 = ' '.join(str(e) for e in doList)
	c=pc.Cube()								
	c(str1)
	solver=CFOPSolver(c)
	doList=convertForToList(solver.solve())
	var.set(doList)




solcol = tk.Button(mainWin,text="solve color",font=myfont,command=solco)
solcol.place(x=150,y=550)

ran=tk.Button(mainWin,text="random",font=myfont,command=rando)
ran.place(x=450,y=550)
solran = tk.Button(mainWin,text="solve random",font=myfont,command=solra)
solran.place(x=650,y=550)

rot=tk.Button(mainWin,text="rotate",font=myfont,command=rota)
rot.pack(side='bottom')



# 步驟四： 進入事件處理迴圈。
mainWin.mainloop()
