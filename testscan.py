import board
import busio

RX = board.GP5
TX = board.GP4

scanner_uart = busio.UART(TX, RX, baudrate=9600)

while True:
    data = scanner_uart.read(32)  # read up to 32 bytes
    if data is not None:
        print(data)  # this is a bytearray type