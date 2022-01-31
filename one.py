from pymata_aio.pymata3 import PyMata3
import time

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
right=52
uright=-62

# lis=[L,R,F,B,U,D]
lis=[L]
# send the arduino a firmata reset
firmata.send_reset()

firmata.stepper_config(rel, L)



for i in range(100):	
	# for face in lis:
	# 	# time.sleep(1)
		# firmata.stepper_config(rel, 
		firmata.stepper_step(speed, 1)
		time.sleep(.2)
		# firmata.stepper_step(speed, uright)
		# print('ro = ',face)
		# firmata.send_reset()
		# time.sleep(1)

print('~~~~~finish~~~~~~')


# firmata.sleep(4)

# move motor #0 500 steps reverse at a speed of 20
# firmata.stepper_step(20, -500)

# close firmata
firmata.shutdown()