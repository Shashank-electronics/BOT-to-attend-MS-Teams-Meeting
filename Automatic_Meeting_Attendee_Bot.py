import usb_hid
import time
import board
import digitalio
from adafruit_hid.mouse import Mouse
mouse=Mouse(usb_hid.devices)

while True:
    time.sleep(5)
    mouse.move(y=-2000,x=-3000)
    time.sleep(1)
    mouse.move(y=160,x=10) #Clicking Calender
    time.sleep(1)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(1) 
    mouse.move(y=-2000,x=-3000)
    time.sleep(1)
    mouse.move(y=165,x=120) #Clicking Teams meeting link
    time.sleep(1)
    mouse.click(Mouse.LEFT_BUTTON)
    mouse.move(y=-2000,x=-3000)  # Reference Co-ordinate
    time.sleep(2)
    # to click join button
    mouse.move(y=65,x=100) 
    time.sleep(2)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(2)
    mouse.move(y=-2000,x=-3000)  
    time.sleep(2)
    # To Click Join Now
    mouse.move(y=-2000,x=-3000)
    time.sleep(2)
    mouse.move(y=232,x=385) 
    time.sleep(2)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(2)
    mouse.move(y=-2000,x=-3000)  

    # To Click Leave Button
    time.sleep(3) # Amount of duration you want your BOT to attend MEETING for you
    mouse.move(y=-2000,x=-3000)
    time.sleep(1)
    mouse.move(y=40,x=420) 
    time.sleep(1)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(1)
    mouse.move(y=-2000,x=-3000)  
    time.sleep(2)
    
    
    