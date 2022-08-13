import board
import busio

import adafruit_thermal_printer

# Pick which version thermal printer class to use depending on the version of
# your printer.  Hold the button on the printer as it's powered on and it will
# print a test page that displays the firmware version, like 2.64, 2.68, etc.
# Use this version in the get_printer_class function below.
ThermalPrinter = adafruit_thermal_printer.get_printer_class(1.11)

# Define RX and TX pins for the board's serial port connected to the printer.
# Only the TX pin needs to be configued, and note to take care NOT to connect
# the RX pin if your board doesn't support 5V inputs.  If RX is left unconnected
# the only loss in functionality is checking if the printer has paper--all other
# functions of the printer will work.
RX = board.GP1
TX = board.GP0

# Create a serial connection for the printer.  You must use the same baud rate
# as your printer is configured (print a test page by holding the button
# during power-up and it will show the baud rate).  Most printers use 19200.
printer_uart = busio.UART(TX, RX, baudrate=9600)

# Create the printer instance.
printer = ThermalPrinter(printer_uart,  byte_delay_s=0.00057346, dot_feed_s=0.0021, dot_print_s=0.003)

# Initialize the printer.  Note this will take a few seconds for the printer
# to warm up and be ready to accept commands (hence calling it explicitly vs.
# automatically in the initializer with the default auto_warm_up=True).
printer.warm_up()

printer.bold = True
printer.size = adafruit_thermal_printer.SIZE_LARGE
printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
printer.print("F407 Hall Pass")

printer.bold = False
printer.size = adafruit_thermal_printer.SIZE_SMALL

printer.print("Time: 00:00     Date: 00/00/00")

printer.print("Name: xxxxxxxxxx")

id = "123456"

# printer.justify = adafruit_thermal_printer.JUSTIFY_LEFT
# printer.print_barcode("123456", printer.CODE39)

printer.send_command("\x1Dw\x03")  # Barcode width 3 (0.375/1.0mm thin/thick)
printer.send_command("\x1Dk{0}".format(chr(printer.CODE39)))  # Barcode type
# Write length and then string (note this only works with 2.64+).
#printer.send_command(chr(len(id)))
printer.send_command(id)
printer.send_command("\x00")
printer._set_timeout((printer._barcode_height + 40) * printer._dot_print_s)
printer.print(id)

printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
printer.feed(2)
printer.print("________________________________")
printer.print("Not valid outside of F400")
printer.print("unless signed by teacher")

# Feed a few lines to see everything.
printer.feed(3)