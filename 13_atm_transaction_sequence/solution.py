balance = 1000
limit = 500
transactions = [("deposit", 250), ("withdraw", 400), ("withdraw", 600), ("deposit", -10), ("withdraw", 500), ("transfer", 10)]
accepted = 0
rejected = 0
for kind, amount in transactions:
    if amount <= 0 or (kind != "deposit" and kind != "withdraw"):
        reason = "invalid type or amount"
    elif kind == "withdraw" and amount > limit:
        reason = "withdrawal limit exceeded"
    elif kind == "withdraw" and amount > balance:
        reason = "insufficient balance"
    else:
        reason = ""
    if reason != "":
        rejected += 1
        print(kind, amount, "REJECTED:", reason)
    else:
        if kind == "deposit":
            balance += amount
        else:
            balance -= amount
        accepted += 1
        print(kind, amount, "ACCEPTED; balance:", balance)
print("Summary: accepted = {}, rejected = {}, balance = {}".format(accepted, rejected, balance))
