# Attendance Recovery: edit the sample scenarios below.
scenarios = [(60, 80, 75, 0), (60, 80, 75, 5), (9, 10, 100, 0), (10, 10, 100, 0), (8, 0, 75, 0)]
for attended, total, target, missed in scenarios:
    print("Scenario:", (attended, total, target, missed))
    if total <= 0 or attended < 0 or attended > total or target < 0 or target > 100 or missed < 0:
        print("Result: Invalid input")
    else:
        total = total + missed
        print("Current after missed classes: {:.2f}%".format(attended * 100 / total))
        if target == 100 and attended < total:
            print("Result: Impossible to reach 100%")
        else:
            needed = 0
            while attended * 100 < target * total:
                attended += 1
                total += 1
                needed += 1
            print("Result: {} consecutive classes".format(needed))
