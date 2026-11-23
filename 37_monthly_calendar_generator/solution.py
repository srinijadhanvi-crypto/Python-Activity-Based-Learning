examples = [(2, 30), (6, 28), (7, 31), (0, 27)]
for start, days in examples:
    print("Calendar: start = {}, days = {}".format(start, days))
    if start < 0 or start > 6 or days not in (28, 29, 30, 31):
        print("Invalid calendar settings")
    else:
        print("Mo Tu We Th Fr Sa Su")
        print("   " * start, end="")
        for day in range(1, days + 1):
            print("{:2}".format(day), end="")
            if (start + day) % 7 == 0 or day == days:
                print()
            else:
                print(" ", end="")
