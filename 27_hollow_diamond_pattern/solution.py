dimensions = [4, 1, 0]
for n in dimensions:
    print("Dimension:", n)
    if n < 1 or n > 20:
        print("Invalid dimension; use 1 to 20")
    else:
        for row in range(1, n + 1):
            spaces = " " * (n - row)
            if row == 1:
                print(spaces + "*")
            else:
                print(spaces + "*" + " " * (2 * row - 3) + "*")
        for row in range(n - 1, 0, -1):
            spaces = " " * (n - row)
            if row == 1:
                print(spaces + "*")
            else:
                print(spaces + "*" + " " * (2 * row - 3) + "*")
