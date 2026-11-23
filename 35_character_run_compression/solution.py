samples = ["AAABBCCCC", "ABCD", "", "111111", "AAAAAAAAAAAA"]
for text in samples:
    encoded = ""
    i = 0
    while i < len(text):
        char = text[i]
        count = 1
        i += 1
        while i < len(text) and text[i] == char:
            count += 1
            i += 1
        encoded += str(count) + char
    print("Input: {!r}; encoded: {!r}; lengths: {} -> {}".format(text, encoded, len(text), len(encoded)))
    if len(encoded) < len(text):
        print("Result: beneficial")
    else:
        print("Result: not beneficial")
