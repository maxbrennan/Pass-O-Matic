class HallPass:
    def __init__(self, title, student, time) -> None:
        self.student = student
        self.time = time
        self.title = title

    def print(self, printer) -> bool:
        # if not printer.has_paper():
        #     return False

        printer.bold = True
        printer.size = printer.SIZE_LARGE
        printer.justify = printer.JUSTIFY_CENTER
        printer.print(self.title)

        printer.bold = False
        printer.size = printer.SIZE_SMALL

        hour = self.time.tm_hour
        if (hour > 12):
            hour = hour - 12
        year = str(self.time.tm_year)[2:4]

        printer.print("{:11}{:>21}".format(
            "Time: {}:{:02}".format(hour, self.time.tm_min), 
            "Date: {}/{:}/{}".format(self.time.tm_mon, self.time.tm_mday, year)))

        name = None
        name_label = "Name: "
        if self.student is not None:
            printer._set_timeout((printer._barcode_height + 40) * printer._dot_print_s)
            if self.student["id"]:
                printer.print(str(self.student["id"]))
                printer.print_barcode(str(self.student["id"]))
            if self.student["name"]:
                name = name_label + self.student["name"]
                
        if name is None:
            printer.feed(2)
            name = "{:_<32}".format(name_label)

        printer.print(name)
        
        printer.justify = printer.JUSTIFY_CENTER
        printer.feed(2)
        printer.print("________________________________")
        printer.print("Not valid outside of F400")
        printer.print("unless signed by teacher")

        # Feed a few lines to see everything.
        printer.feed(3)

        return True