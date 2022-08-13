import board
import busio

RX = board.GP5
TX = board.GP4

scanner_uart = busio.UART(TX, RX, baudrate=9600, timeout=0.01)

while True:
    data = scanner_uart.readline()
    
    if data is not None:
        str = data.decode()
        print(str)  # this is a bytearray type
