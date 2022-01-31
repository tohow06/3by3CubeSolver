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


firmata.digital_write(2,0)

firmata.digital_write(50,1)
firmata.digital_write(51,0)
firmata.digital_write(52,1)
firmata.digital_write(53,0)
print("sdsdsds")

time.sleep(3)

firmata.digital_write(50,1)
firmata.digital_write(51,1)
firmata.digital_write(52,1)
firmata.digital_write(53,1)
print("sdsd")
time.sleep(3)

firmata.digital_write(50,1)
firmata.digital_write(51,0)
firmata.digital_write(52,0)
firmata.digital_write(53,1)
print("sdsd")
time.sleep(3)

print('~~~~~finish~~~~~~')

firmata.shutdown()