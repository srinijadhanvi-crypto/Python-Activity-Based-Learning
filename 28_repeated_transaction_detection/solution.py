transactions = [("T01", 1000), ("T02", 6000), ("T01", 7000), ("", 20), ("T03", -1), ("T04", 5000)]
threshold = 5000
seen = []
suspicious = 0
invalid = 0
for identifier, amount in transactions:
    if identifier.strip() == "" or amount < 0:
        invalid += 1
        print("INVALID:", identifier, amount)
    else:
        reasons = []
        if identifier in seen:
            reasons.append("duplicate ID")
        else:
            seen.append(identifier)
        if amount > threshold:
            reasons.append("above threshold")
        if len(reasons) > 0:
            suspicious += 1
            print("SUSPICIOUS:", identifier, amount, ", ".join(reasons))
        else:
            print("OK:", identifier, amount)
print("Summary: suspicious = {}, invalid = {}".format(suspicious, invalid))
