from PyMata.pymata import PyMata 
import time
import sys



doList=sys.argv[1].split(' ')
print("doList = ",doList)
stepPerRevolution=200
rpm=200
right=50
L=[2,3,4,5]
R=[2,3,4,5]
U=[8,9,10,11]
D=[2,3,4,5]
F=[2,3,4,5]
B=[2,3,4,5]

firmata = PyMata("/dev/cu.wchusbserial14510")
firmata.reset()


def rotate(face,clock):
    firmata.stepper_config(stepPerRevolution , face)
    time.sleep(.5)
    firmata.stepper_step(rpm,(right*clock))
    print("ro")

for mo in doList:
		if mo=='R':
			rotate(R,1)
		if mo=="R'":
			rotate(R,-1)
		if mo=='R2':
			rotate(R,1)
			rotate(R,1)
		if mo=='U':
			rotate(U,1)
		if mo=="U'":
			rotate(U,-1)
		if mo=='U2':
			rotate(U,1)
			rotate(U,1)				
		if mo=='L':
			rotate(L,1)
		if mo=="L'":
			rotate(L,-1)
		if mo=='L2':
			rotate(L,1)
			rotate(L,1)				
		if mo=='D':
			rotate(D,1)
		if mo=="D'":
			rotate(D,-1)
		if mo=='D2':
			rotate(D,1)
			rotate(D,1)				
		if mo=='F':
			rotate(F,1)
		if mo=="F'":
			rotate(F,-1)
		if mo=='F2':
			rotate(F,1)
			rotate(F,1)				
		if mo=='B':
			rotate(B,1)
		if mo=="B'":
			rotate(B,-1)
		if mo=='B2':
			rotate(B,1)
			rotate(B,1)   
    

firmata.close()