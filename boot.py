import board
import digitalio
import storage

usb_connected = digitalio.DigitalInOut(board.GP24)
usb_connected.directon = digitalio.Direction.INPUT

if usb_connected.value == True:
    storage.remount("/", True)
    print("USB connected. Computer can write to drive, activity cannot be recorded.")
else:
    storage.remount("/", False)
    print("USB not connected. Computer cannot write to drive, activity will be recorded.")
