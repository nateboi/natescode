import time
score = 0
answer = input("do you want to A)see the results or B)take the quiz(please use the correct capitalized letter):")
if answer == "A":
    file = open("quiz results.txt", "r")
    contents = file.read()
    print(contents)
    file.close()
    leave = input("would you like time to look(you will be given 3 minutes)")
    if leave == "yes" :
        time.sleep(180)
    while score == 0:
        print("please exit program")
else:
    print ("please enter firstname")
    firstname = input()
    print ("please enter age")
    age = input()
    username = firstname[:3] + age
    subject = input("what subject do you want  ict , foood , history")
    difficulty = input("What difficulty of quiz do you want?  easy medium hard : ")
    subdiff = (subject + difficulty)
    
    if subdiff == "foodeasy":
        file = open("easyfoodquestions.txt", "r")
    elif subdiff == "foodmedium":
        file = open("mediumfoodquestions.txt", "r")
    elif subdiff == "foodhard":
        file = open("hardfoodquestions.txt","r")
    elif subdiff == "icteasy":
        file = open("easyictquestions.txt", "r")
    elif subdiff == "ictmedium":
        file = open("mediumictquestions.txt", "r")
    elif subdiff == "icthard":
        file = open("hardictquestions.txt","r")
    elif subdiff == "historyeasy":
        file = open("easyhistoryuestions.txt", "r")
    elif subdiff == "historymedium":
        file = open("mediumhistoryquestions.txt", "r")
    elif subdiff == "historyhard":
        file = open("hardhistoryquestions.txt","r")
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
if answer2 == "B":
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
if answer6 == "A":
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
if answer8 == "B":
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
if answer10 == "B":
    print ("correct")
    score = score + 1
else:
    print ("incorrect")
print ("Your end score was",score,"/ 10")
score = str(score)
file = open("quiz results.txt", "a")
file.write("\n" + username + "\n")
file.write(score)
file.close()




    
