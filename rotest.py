from pymata_aio.pymata3 import PyMata3
import time
import sys



doList=sys.argv[1].split(' ')
print("doList = ",doList)

stepPerRevolution=200
rpm=60
right=53
L=[50,51,52,53]
R=[46,47,48,49]
F=[42,43,44,45]
B=[38,39,40,41]
U=[34,35,36,37]
D=[30,31,32,33]

firmata = PyMata3(2)
firmata.send_reset()

def handCheck(face,t):
        firmata.digital_write(face[0],1)
        firmata.digital_write(face[1],1)
        firmata.digital_write(face[2],1)
        firmata.digital_write(face[3],1)

        firmata.digital_write(face[0],0)
        firmata.digital_write(face[1],0)
        firmata.digital_write(face[2],0)
        firmata.digital_write(face[3],0)
        #print("start handchecking")
        time.sleep(t)
        #print('end handchecking')


def rotate(face,clock):
	firmata.stepper_config(stepPerRevolution , face)
	time.sleep(.2)
	print(face)
	firmata.stepper_step(rpm,(right*clock))
	time.sleep(.2)
	handCheck(face,1.5)

for mo in doList:
		if mo=='R':
			rotate(R,-1)
		if mo=="R'":
			rotate(R,1)
		if mo=='R2':
			rotate(R,1)
			rotate(R,1)
		if mo=='U':
			rotate(U,-1)
		if mo=="U'":
			rotate(U,1)
		if mo=='U2':
			rotate(U,1)
			rotate(U,1)				
		if mo=='L':
			rotate(L,-1)
		if mo=="L'":
			rotate(L,1)
		if mo=='L2':
			rotate(L,1)
			rotate(L,1)				
		if mo=='D':
			rotate(D,-1)
		if mo=="D'":
			rotate(D,1)
		if mo=='D2':
			rotate(D,1)
			rotate(D,1)				
		if mo=='F':
			rotate(F,-1)
		if mo=="F'":
			rotate(F,1)
		if mo=='F2':
			rotate(F,1)
			rotate(F,1)				
		if mo=='B':
			rotate(B,-1)
		if mo=="B'":
			rotate(B,1)
		if mo=='B2':
			rotate(B,1)
			rotate(B,1)   
    

firmata.shutdown()
