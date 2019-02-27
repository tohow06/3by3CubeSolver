import tkinter as tk

mainWin=tk.Tk()


mainWin.geometry('800x600')


boxsize=50
cans=[]



def change(event):
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
	cans[num].config(bg='red')			
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

mainWin.mainloop()

