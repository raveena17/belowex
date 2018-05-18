sequence = raw_input("Please input:")
for letter in sequence:
    if letter not in "atcg":
        print("invalid input, sequence coule only contain the following letters (a,t,c,g)")

