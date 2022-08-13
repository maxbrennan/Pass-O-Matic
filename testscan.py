import board
import busio

RX = board.GP9
TX = board.GP8

scanner_uart = busio.UART(TX, RX, baudrate=9600)

while True:
    data = scanner_uart.read(32)  # read up to 32 bytes
    print(data)  # this is a bytearray type