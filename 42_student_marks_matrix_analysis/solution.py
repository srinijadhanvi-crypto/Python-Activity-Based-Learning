students = ["Anu", "Bala", "Charan"]
subjects = ["Math", "Science", "English"]
marks = [[80, 30, 70], [75, 40, 80], [80, 30, 70]]
valid = len(students) > 0 and len(subjects) > 0 and len(marks) == len(students)
for row in marks:
    if len(row) != len(subjects): valid = False
    for value in row:
        if value < 0 or value > 100: valid = False
if not valid:
    print("Invalid marks matrix")
else:
    totals = []
    for i in range(len(students)):
        total = 0
        for value in marks[i]: total += value
        totals.append(total)
        print("{}: total {}, average {:.2f}".format(students[i], total, total / len(subjects)))
    for j in range(len(subjects)):
        total = 0
        for i in range(len(students)): total += marks[i][j]
        average = total / len(students)
        label = "LOW" if average < 40 else "OK"
        print("{}: average {:.2f} {}".format(subjects[j], average, label))
    highest = max(totals)
    for i in range(len(students)):
        if totals[i] == highest: print("Top performer: {} ({})".format(students[i], highest))
