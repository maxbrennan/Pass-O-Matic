# Find a student's name given their id number
def lookup(id: int) -> str:
    with open("roster.csv", mode="r", encoding="utf-8") as csvfile:
        for line in csvfile:
            try:
                (sid, name) = line.split(",", 1)
                if id == int(sid):
                    name = name.strip()
                    print(name)
                    return {"id": id, "name": name}
            except:
                pass
    return {"id": id, "name": None}


# Print all students' name and ids from the roster
def print_all(printer) -> None:

    printer.bold = False
    printer.size = printer.SIZE_SMALL
    printer.justify = printer.JUSTIFY_LEFT

    with open("roster.csv", mode="r", encoding="utf-8") as csvfile:
        for line in csvfile:
            try:
                (sid, name) = line.split(",", 1)
                
                printer.print(sid + ": " + name.strip())
            except:
                pass

    
    printer.feed(3)