# main code for pass-o-matic

import time
import board
import busio
import adafruit_ds3231

i2c = busio.I2C(scl=board.GP27, sda=board.GP26)  # uses board.SCL and board.SDA
rtc = adafruit_ds3231.DS3231(i2c)

from scanner import Scanner

SCAN_RX = board.GP5
SCAN_TX = board.GP4
barcode = Scanner(SCAN_TX, SCAN_RX)

def print_time():
    # Lookup table for names of days (nicer printing).
    days = ("Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun")
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

    t = rtc.datetime
    # print(t)     # uncomment for debugging
    print(
        "The date is {}, {} {} {}".format(
            days[int(t.tm_wday)], months[t.tm_mon - 1], t.tm_mday, t.tm_year
        )
    )
    print("The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))

print_time()

while True:
    scan = barcode.check_scan()

    if scan is None:
        continue

    print(str(scan))

    if scan.type == "TIME":
        rtc.datetime = scan.data
        print_time()    

