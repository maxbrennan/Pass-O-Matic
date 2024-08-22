class HallPass:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def print(self, printer) -> bool:
        # if not printer.has_paper():
        #     return False

        printer.bold = True
        printer.size = printer.SIZE_LARGE
        printer.justify = printer.JUSTIFY_CENTER
        printer.print("Scavenger Hunt")

        printer.feed(2)

        printer.bold = False
        printer.size = printer.SIZE_SMALL
        printer.print("Name: " + self.name)
        printer.print("ID: " + str(self.ID))

        # Feed a few lines to see everything.
        printer.feed(3)

        return True
