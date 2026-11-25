# Monday is 0 and Sunday is 6.
examples = [(2, 30), (6, 28), (7, 31), (0, 27)]
for start, days in examples:
    print("Calendar: start = {}, days = {}".format(start, days))
    if start < 0 or start > 6 or days not in (28, 29, 30, 31):
        print("Invalid calendar settings")
    else:
        print("Mo Tu We Th Fr Sa Su")
        day = 1
        first_week = True
        while day <= days:
            week = ""
            for weekday in range(7):
                if first_week and weekday < start:
                    week += "   "
                elif day <= days:
                    week += str(day).rjust(2) + " "
                    day += 1
            print(week.rstrip())
            first_week = False
