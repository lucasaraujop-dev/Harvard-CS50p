question = input("What is the Great Question of Life, the Universe and Everything? ")
userinput = question.lower().strip()
answer = False

if userinput == "42":
    answer = True
elif userinput == "forty-two":
    answer =True
elif userinput == "forty two":
    answer = True
else:
    answer == False

if answer == True:
    print("Yes")
else:
    print("No")
