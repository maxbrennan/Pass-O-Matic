def record_student(student, time) -> bool:
    time_str = "{}-{:02}-{:02}T{:02}:{:02}".format(time.tm_year, time.tm_mon, time.tm_mday,
                                       time.tm_hour, time.tm_min)
    id = str(student["id"])
    name = str(student["name"])
    record = time_str + ', ' + id + ', ' + name
    print (record)

    try:
        with open("activity.csv", mode="a", encoding="utf-8") as actfile:
            actfile.write(record + "\n")
        return True
    except:
        return False
