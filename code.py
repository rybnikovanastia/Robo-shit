import time
import board
import analogio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
from adafruit_circuitplayground import cp

# setup
kbd = Keyboard(usb_hid.devices)
# mouse = Mouse(usb_hid.devices)

# sensors
sensorA = analogio.AnalogIn(board.A4)
sensorB = analogio.AnalogIn(board.A7)
sensorC = analogio.AnalogIn(board.A0)

# thresholds 
THRESHOLD_A = 50000
THRESHOLD_B = 50000
THRESHOLD_C = 50000

# state tracking
c_pressed = False
g_pressed = False
space_pressed = False

while True:
    # read sensors
    valA = sensorA.value
    valB = sensorB.value
    valC = sensorC.value
    print("A:", sensorA.value, "B:", sensorB.value,  "C:", sensorC.value)
    time.sleep(0.01)
    # Sensor A
    if valA > THRESHOLD_A:
        if not c_pressed:
            kbd.press(Keycode.C)
            c_pressed = True
    else:
        if c_pressed:
            kbd.release(Keycode.C)
            c_pressed = False

    # Sensor B
    if valB > THRESHOLD_B:
        if not g_pressed:
            kbd.press(Keycode.G)
            g_pressed = True
    else:
        if g_pressed:
            kbd.release(Keycode.G)
            g_pressed = False
    # Sensor C
    if valC > THRESHOLD_C:
        if not space_pressed:
            kbd.press(Keycode.SPACE)
            space_pressed = True
    else:
        if space_pressed:
            kbd.release(Keycode.SPACE)
            space_pressed = False

    # delay
    time.sleep(0.01)
