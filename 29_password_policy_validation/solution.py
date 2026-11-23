passwords = ["Good7!xy", "abc", "AAAabc1!", "MyPassword1!", "NoSpecial7"]
for password in passwords:
    errors = []
    if len(password) < 8:
        errors.append("minimum length 8")
    upper = False
    lower = False
    digit = False
    special = False
    repeated = False
    for i in range(len(password)):
        char = password[i]
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": upper = True
        if char in "abcdefghijklmnopqrstuvwxyz": lower = True
        if char in "0123456789": digit = True
        if char in "!@#$%": special = True
        if i >= 2 and password[i] == password[i - 1] and password[i] == password[i - 2]: repeated = True
    if not upper: errors.append("missing uppercase")
    if not lower: errors.append("missing lowercase")
    if not digit: errors.append("missing digit")
    if not special: errors.append("missing special character")
    if repeated: errors.append("three repeated characters")
    if "password" in password.lower() or "admin" in password.lower(): errors.append("prohibited substring")
    if len(errors) == 0:
        print(password, "ACCEPTED")
    else:
        print(password, "REJECTED:", "; ".join(errors))
