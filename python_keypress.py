import serial, sys
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

def press(char):
    keyboard.press(char)
    sleep(0.025)
    keyboard.release(char)
    #sleep(0.1)

COM = 'COM7'# /dev/ttyACM0 (Linux)
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(3)
print(ser.name)

#check args
if("-m" in sys.argv or "--monitor" in sys.argv):
	monitor = True
else:
	monitor= False

btn_prev = None
keys_press = [None, None]

while True:
    try:
        #print(keys_press)
        val = str(ser.readline().decode().strip('\r\n'))#Capture serial output as a decoded string
        
        if "X Axis" in val:
            if float(val.strip("X Axis")) < 2.5 and float(val.strip("X Axis")) >= 0:
                if keys_press[0] == Key.right:
                    keyboard.release(Key.right)
                    
                keyboard.press(Key.left)
                keys_press[0] = Key.left
            elif float(val.strip("X Axis")) > 2.5:
                if keys_press[0] == Key.left:
                    keyboard.release(Key.left)
                                     
                keyboard.press(Key.right)
                keys_press[0] = Key.right
            elif (val.strip("X Axis")) == "-1":
                if keys_press[0] != None:
                    keyboard.release(keys_press[0])

        elif "Y Axis" in val:
            if float(val.strip("Y Axis")) < 2.5 and float(val.strip("Y Axis")) >= 0:
                if keys_press[1] == Key.down:
                    keyboard.release(Key.down)
                    
                keyboard.press(Key.up)
                keys_press[1] = Key.up
            elif float(val.strip("Y Axis")) > 2.5:
                if keys_press[1] == Key.up:
                    keyboard.release(Key.up)
                    
                keyboard.press(Key.down)
                keys_press[1] = Key.down
                
            elif (val.strip("Y Axis")) == "-1":
                if keys_press[1] != None:
                    keyboard.release(keys_press[1])
        
        elif val == "High1" and val != btn_prev: #Press door only once
            press(Key.space)
        elif val == "High2": #IE, keep on shooting. Gun delay means that this wont be an issue.
            press(Key.ctrl_l)
        
    except:
        print("Exception")
