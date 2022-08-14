import board
import busio

import adafruit_thermal_printer.thermal_printer_legacy as thermal_printer
class Printer(thermal_printer.ThermalPrinter):
    from adafruit_thermal_printer.thermal_printer import (
        JUSTIFY_LEFT,
        JUSTIFY_CENTER,
        JUSTIFY_RIGHT,
        SIZE_SMALL,
        SIZE_MEDIUM,
        SIZE_LARGE,
        UNDERLINE_THIN,
        UNDERLINE_THICK,
    )

    def __init__(self, tx, rx, rtc) -> None:
        self._uart = busio.UART(tx, rx, baudrate=9600)
        self._rtc = rtc

        # Create the printer instance.
        super().__init__(self._uart, byte_delay_s=0.00057346, dot_feed_s=0.0021, dot_print_s=0.003)
        self.warm_up()

    def print_barcode(self, data):
        # if not self.has_paper():
        #     return

        self.send_command("\x1Dw\x03")  # Barcode width 3 (0.375/1.0mm thin/thick)
        self.send_command("\x1Dk{0}".format(chr(self.CODE39)))  # Barcode type
        # Write length and then string (note this only works with 2.64+).
        #printer.send_command(chr(len(id)))
        self.send_command(data)
        self.send_command("\x00")
