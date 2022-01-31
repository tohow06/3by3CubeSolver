from PyMata.pymata import PyMata 
import time
import sys



doList=sys.argv[1].split(' ')
print("doList = ",doList)
stepPerRevolution=200
rpm=200
right=50
# L=[50,51,52,53]
# R=[46,47,48,49]
# U=[42,43,44,45]
# D=[38,39,40,41]
# F=[34,35,36,37]
# B=[30,31,32,33]
L=[2,3,4,5]
R=[6,7,8,9]
U=[2,3,4,5]
D=[2,3,4,5]
F=[6,7,8,9]
B=[6,7,8,9]

firmata = PyMata("/dev/cu.wchusbserial14510")
firmata.reset()


def rotate(face,clock):
	time.sleep(.5)
	firmata.stepper_config(stepPerRevolution , face)
	time.sleep(.5)
	firmata.stepper_request_library_version()
	firmata.stepper_step(rpm,(right*clock))
	time.sleep(.5)
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