# main code for pass-o-matic

import time
import board
import busio
import adafruit_ds3231

from scanner import Scanner
from printer import Printer
from hallpass import HallPass
import roster
import activity

# Connect to the realtime clock
i2c = busio.I2C(scl=board.GP27, sda=board.GP26)  # uses board.SCL and board.SDA
rtc = adafruit_ds3231.DS3231(i2c)

# RX and TX pins for the board's serial port connected to the barcode scanner.
SCAN_RX = board.GP5
SCAN_TX = board.GP4
barcode = Scanner(SCAN_TX, SCAN_RX)

# RX and TX pins for the board's serial port connected to the printer.
PRINT_RX = board.GP1
PRINT_TX = board.GP0
printer = Printer(PRINT_TX, PRINT_RX, rtc)

# The current date and time as a string
def time_str():
    # Lookup table for names of months (nicer printing).
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

    t = rtc.datetime

    str = ""

    # print(t)     # uncomment for debugging
    str = str + "The date is {} {} {}\n".format(
            months[t.tm_mon - 1], t.tm_mday, t.tm_year
        )
    str = str + "The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec)

    return str

print(time_str())

while True:
    scan = barcode.check_scan()

    if scan is None:
        continue

    print(str(scan))

    if scan.type == "TIME":
        rtc.datetime = scan.data

        # Display the new time on the console
        print(time_str())
        
        # print the new time as a receipt
        printer.print(time_str())
        # Feed a few lines to see everything.
        printer.feed(3)
        time.sleep(3)
        barcode.clear()
    
    elif scan.type == "ROSTER":
        print("Printing roster")
        roster.print_all(printer)

    elif scan.type == "ACTIVITY":
        print("Printing activity report")
        printer.print("ACTIVITY REPORT")
        printer.feed(3)        

    elif scan.type == "ID":
        student = roster.lookup(scan.data)
        activity.record_student(student, rtc.datetime)
        hallpass = HallPass("F407 Hall Pass", student, rtc.datetime)
        hallpass.print(printer)

    elif scan.type == "ERROR":
        print("Scan error: " + scan.data)
