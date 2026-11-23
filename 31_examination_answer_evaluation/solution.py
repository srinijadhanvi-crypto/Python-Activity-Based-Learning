key = "ABCDAB"
responses = [("Anu", "AB-DAC"), ("Bala", "ABCDAB"), ("Charan", "------"), ("Deepa", "ABCXAB"), ("Esha", "AB")]
key_valid = len(key) > 0
for char in key:
    if char not in "ABCD": key_valid = False
if not key_valid:
    print("Invalid answer key")
else:
    for name, answer in responses:
        valid = len(answer) == len(key)
        for char in answer:
            if char not in "ABCD-": valid = False
        if not valid:
            print(name, "INVALID response")
        else:
            correct, incorrect, unanswered = 0, 0, 0
            for i in range(len(key)):
                if answer[i] == "-": unanswered += 1
                elif answer[i] == key[i]: correct += 1
                else: incorrect += 1
            score = correct * 4 - incorrect
            print("{}: correct {}, incorrect {}, unanswered {}, score {}".format(name, correct, incorrect, unanswered, score))
