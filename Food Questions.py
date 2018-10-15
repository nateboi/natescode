score = 0
difficulty = input("What difficulty of quiz do you want?  Easy Medium Hard : ")
if difficulty == "Easy":
    file = open("easyfoodquestions.txt", "r")
elif difficulty == "Medium":
    file = open("mediumfoodquestions.txt", "r")
elif difficulty == "Hard":
    file = open("hardfoodquestions.txt","r")
else:
    while score == 0:
        print("Invalid Option")
line = file.readline()
answer1 = input(line)
if answer1 == "A":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
line = file.readline()
answer2 = input(line)
if answer2 == "A":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
line = file.readline()
answer3 = input(line)
if answer3 == "B":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
line = file.readline()
answer4 = input(line)
if answer4 == "B":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
line = file.readline()
answer5 = input(line)
if answer5 == "A":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
line = file.readline()
answer6 = input(line)
if answer6 == "B":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
line = file.readline()
answer7 = input(line)
if answer7 == "A":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
line = file.readline()
answer8 = input(line)
if answer8 == "A":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
line = file.readline()
answer9 = input(line)
if answer9 == "A":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
line = file.readline()
answer10 = input(line)
if answer10 == "A":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
print ("Your end score was",score,"/ 10")
