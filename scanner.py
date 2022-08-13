import busio
import time

class Scan:
    def __init__(self, scan_string) -> None:
        self._str = scan_string
        self.type = None
        
        # T scans = set current time in "TYYYYMMDDHHmmSS" format
        if (scan_string.startswith("T") and len(scan_string) == 16):
            self.type = "TIME"
            year = int(scan_string[1:5])
            month = int(scan_string[5:7])
            day = int(scan_string[7:9])
            hour = int(scan_string[9:11])
            min = int(scan_string[11:13])
            sec = int(scan_string[13:15])
            self.data = time.struct_time((year, month, day, hour, min, sec, -1, -1, -1))
        else:
            try:
                # simple numbers are IDs
                self.data = int(scan_string)
                self.type = "ID"

            except:
                pass

    def __str__(self) -> str:
        if (self.type == "ID"):
            return "ID:" + str(self.data)
        elif (self.type == "TIME"):
            return "TIME:" + str(self.data.tm_year) + "-" + str(self.data.tm_mon) + "-" + str(self.data.tm_mday) \
                + " " + str(self.data.tm_hour) + ":" + str(self.data.tm_min) + ":" + str(self.data.tm_sec)

        return "Scan: " + self._str


class Scanner:
    def __init__(self, tx, rx) -> None:
        self._uart = busio.UART(tx, rx, baudrate=9600, timeout=0.01)

    def check_scan(self) -> Scan:
        data = self._uart.readline()
    
        if data is not None:
            str = data.decode()
            return Scan(str);

        return None