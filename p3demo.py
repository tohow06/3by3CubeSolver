from pymata_aio.pymata3 import PyMata3
import time
import signal

# create a PyMata instance
# ping callback function
def vr(data):
    # print('hello')
    print('version')
    print(data)

# create a PyMata instance
# create a PyMata instance
firmata = PyMata3(2)

L=[50,51,52,53]
R=[46,47,48,49]
F=[42,43,44,45]
B=[38,39,40,41]
U=[34,35,36,37]
D=[30,31,32,33]
speed=60
rel=200
right=53


lis=[R]
# lis=[U,D]

# send the arduino a firmata reset
firmata.send_reset()


def exit(signum, frame):
        print('You choose to stop me.')
        firmata.shutdown()
        exit()
signal.signal(signal.SIGINT, exit)


def handCheck(face,t):
	firmata.digital_write(face[0],1)
	firmata.digital_write(face[1],1)
	firmata.digital_write(face[2],1)
	firmata.digital_write(face[3],1)

	firmata.digital_write(face[0],0)
	firmata.digital_write(face[1],0)
	firmata.digital_write(face[2],0)
	firmata.digital_write(face[3],0)
	print("start handchecking")
	time.sleep(t)
	print('end handchecking')

for i in range(20):	
	for face in lis:
		firmata.stepper_config(rel, face)
		time.sleep(.2)
		firmata.stepper_step(speed, right)
		print('ro = ',face)
		time.sleep(.2)
		handCheck(face,2)


# face=R
# t=3
# firmata.stepper_config(rel, face)
# time.sleep(.2)
# firmata.stepper_step(speed, right)
# print('ro = ',face)
# time.sleep(10000)

# firmata.digital_write(face[0],1)
# firmata.digital_write(face[1],1)
# firmata.digital_write(face[2],1)
# firmata.digital_write(face[3],1)
# print("start handchecking")
# time.sleep(t)
# print('end handchecking')

# firmata.stepper_config(rel, face)
# time.sleep(.2)
# firmata.stepper_step(speed, right)
# print('ro = ',face)
# time.sleep(.2)




print('~~~~~finish~~~~~~')

firmata.shutdown()