import board
import digitalio
import random
import time

button1 = digitalio.DigitalInOut(board.D0)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.DOWN

chars = "abcdefghijklmnopqrstuvwxyz "
chari = 0
txt = ""
while True:
    if button1.value:
        time.sleep(0.5)
        if button1.value:
            txt += chars[chari]
            chari = 0
            print(txt)
        else:
            chari += 1
            if chari >= len(chars):
                chari = 0
        print(f"current char: {chars[chari]}")

        while button1.value:
            pass
