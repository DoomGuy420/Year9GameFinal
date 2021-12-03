from logging import fatal
from art import *
from random import *

from art.art_param import DESCRIPTION
import textgamelib
from playsound import playsound

homescreenart = text2art("Brave", font="asdfsasdfsasdfdsseeebdfdfhaerdhfjfgjf")
print(homescreenart)
textgamelib.printDivider("-", 40)
input("Welcome to Brave, a text based game. \nYou might be familiar with Jabari from the book Jabari Jumps. \nIn this game you will be playing as Jabari's son. \nBefore you can get to the game, you have to go through the tutorial and learn the ropes. \nHere we go! Press enter to start the game.")
textgamelib.printDivider("-", 40)
gameScore = 0
while gameScore == 0:
    chapter0art = text2art("Chapter 0", font="bulbhead")
    print(chapter0art)
    print("Wake up, it's time to get out of bed.")
    getUpTutorial = input("Try getting up by typing 'Get Up'\n")
    tutorialScore = 0
    while tutorialScore == 0:
        if "get up" in getUpTutorial.lower():
            print("You got up")
            tutorialScore += 1
        else:
            print("I can't really understand you try again.")
            getUpTutorial = input("Try getting up by typing 'Get Up'\n")
    textgamelib.printDivider("-", 40)
    input("Good job, the way you play this game is simple, you just have to type your actions with specifications \nafter. \nWe'll continue showing you how to do things. \nPress enter to continue.")
    textgamelib.printDivider("-", 40)
    pickUpTutorial = input("It's almost time for school. \nYour bag is by the door, pick up your bag and exit the door. \n")
    while tutorialScore == 1:
        if "pick up" in pickUpTutorial.lower() and ("backpack" in pickUpTutorial.lower() or "bag" in pickUpTutorial.lower()):
            print("You picked up your bag")
            tutorialScore += 1
        elif "pick up" in pickUpTutorial.lower():
            print("I don't understand what you are trying to pick up")
            pickUpTutorial = input("Try typing 'Pick Up Bag'\n")
        else:
            print("I don't understand what you are trying to do")
            pickUpTutorial = input("Try typing 'Pick Up Bag'\n")
    textgamelib.printDivider("-", 40)
    input("This will be an important action as you will need to pick up certain items in the game. \nThe next action will also be very important. \nIt's the 'go' action which will allow you to walk and travel to other places. \nWe'll talk later about other actions.\nPress enter to continue.")
    textgamelib.printDivider("-", 40)
    goTutorial = input("Time to go out of your room and eat breakfast.\n")
    while tutorialScore == 2:
        if "go out of room" in goTutorial.lower() or "exit room" in goTutorial.lower():
            print('You exited your room.')
            tutorialScore += 1
        elif "go" in goTutorial.lower():
            print("I can't really understand where you want to go")
            goTutorial = input("Try typing 'Go out of room'\n")
        else:
            print("I don't know what you are trying to do")
            goTutorial = input("Try typing 'Go out of room'\n")
    textgamelib.printDivider("-", 40)
    print("You exit your room to be greeted by your dad, Jabari.")
    print("Jabari: Good Morning son, almost time for school here's a bowl of cereal for breakfast.")
    eatTutorial = input("Time to eat your cereal for breakfast.\n")
    while tutorialScore == 3:
        if "eat" in eatTutorial.lower() and ("cereal" in eatTutorial.lower() or "breakfast" in eatTutorial.lower()):
            print("You ate your cereal, it tasted good.")
            tutorialScore += 1
        elif "eat" in eatTutorial.lower():
            print("What are you trying to eat")
            eatTutorial = input("Try typing 'Eat Breakfast'\n")
        else:
            print("I can't tell what you are trying to do.")
            eatTutorial = input("Try typing 'Eat Breakfast'\n")
    textgamelib.printDivider("-", 40)
    print("Jabari: It's time to head to school son. Have a good day!")
    print("You exit your house.")
    goTutorial2 = input("Where would you like to go?\n")
    while tutorialScore == 4:
        if "go to school" in goTutorial2.lower() or "school" in goTutorial2.lower():
            print("You walk to school.")
            tutorialScore += 1
        elif "go" in goTutorial2:
            print("I can't understand where you want to go at the moment")
        else:
            print("I can't tell what you want to do.")
            goTutorial2 = input("Try typing 'Go to school'\n")
    print("You arrive at school to see your friend Jimmy at the front door waiting for you. \nJimmy: Hey how are you doing? \nYou: I'm doing good, school going to be boring though. \nJimmy: It's not that bad. \nThe bell rings signifyng that classes are startng. \nYou and Jimmy rush to class and get there right on time.")
    input("After a day of work and classes at school, you return home to eat with your father Jabari. \nYou then finish your homework and go to bed.\nPress enter to continue.")
    textgamelib.printDivider("-", 40)
    endingArt = text2art("End of Tutorial", font="bulbhead")
    print(endingArt)
    textgamelib.printDivider("-", 40)
    gameScore += 1
while gameScore == 1:
    chapter1art = text2art("Chapter 1", font="bulbhead")
    print(chapter1art)
    textgamelib.printDivider("-", 40)
    wakeUp = 0
    while wakeUp == 0:
        playsound('alarmclockbeeping.mp3', block=False)
        getUpChapter1 = input("Time to get up\n")
        if "get up" in getUpChapter1.lower():
            wakeUp += 1
            print("You Got up")
        else:
            getUpChapter1 = input("It's time to get up")
    textgamelib.printDivider("-", 40)
    print("You wake up and look at the time. It's 8:30.....\n8:30?!?!?! \nThat's half an hour after your school started.\nYou got up, rushed to brush your teeth, picked up your bag and headed to the living room to quickly get breakfast. \nAs you headed into the living room, you realized that the lights weren't on. \nThe lights were usually on so you decided to find the switch.")
    textgamelib.printDivider("-", 40)
    chapter1Challenge = input("Objective: Find The Light Switch\n")
    findLights = 0
    while findLights == 0:
        if "go" in chapter1Challenge.lower() and "light switch" in chapter1Challenge.lower() or "find" in chapter1Challenge.lower() and "light switch" in chapter1Challenge.lower():
            print("You walk towards the light switch")
            findLights += 1
        elif "go out of living room" in chapter1Challenge.lower():
            print("You can't really see well.")
            chapter1Challenge = input("Try finding the light switch\n")
        elif "go" in chapter1Challenge.lower() and "to room" in chapter1Challenge.lower():
            print("You have to get to school but first you need to turn on the lights. \nSomething might be in the house.")
            chapter1Challenge = input("Try finding the light switch\n")
        else:
            print("I can't really understand what you are trying to do")
            chapter1Challenge = input("Try finding to light switch\n")
    textgamelib.printDivider("-", 40)
    chapter1Challenge = input("Try turning on the light switch\n")
    turnOnLights = 0
    while turnOnLights == 0:
        if "turn on" in chapter1Challenge.lower() and ("lights" in chapter1Challenge.lower() or "light" in chapter1Challenge.lower() or "light switch" in chapter1Challenge.lower()):
            playsound('lightswitchclick.mp3')
            print("Nothing happened")
            turnOnLights += 1
        elif "turn on" in chapter1Challenge.lower():
            print("What are you trying to turn on?")
            chapter1Challenge = input("Try turning on the light switch\n")
        else:
            print("I can't really tell what you are tring to do.")
            chapter1Challenge = input("Try turning on the light switch\n")
    textgamelib.printDivider("-", 40)
    print("???: Oh there you are son\nYou turn around to see your father Jabari standing behind you.\nJabari: There's a really bad storm outside, flooding in a bunch of areas. The school is closed for today.\nYou were a bit happy because there would be no school but flooding was bad. \nYou were wondering what you would do.\nJabari: Since it's still a school day, you should do some practice with your math and english. Luckily, the thing that you are \nstudying in english is a book about me so you shouldn't have too much problem with that.")
    input("Time to study a bit of math. Get 3 questions right to move on. \nPress enter to start.")
    mathScore = 0
    while mathScore < 3:
        num1 = randint(1,100)
        num2 = randint(1,100)
        print("What is ", num1, "+ ", num2)
        answer1 = input()
        while not answer1.isnumeric():
            answer1 = input("Please type a number\n")
        answer1 = int(answer1)
        if answer1 == num1 + num2:
            print("Correct!")
            mathScore += 1
        else:
            print("Sorry, that's not right.")
        textgamelib.printDivider("-", 40)
    print("Jabari: Good Job! Since it's a special day out of school, we'll stop for today. It's time to look at the book Jabari Jumps!")
    englishScore = 0
    while englishScore == 0:
        englishQuiz = input("What was Jabari scared of?\n")
        if ("jumping off" in englishQuiz.lower() and "diving board" in englishQuiz.lower()) or "jumping" in englishQuiz.lower() or "heights" in englishQuiz.lower:
            print("That is correct")
            englishScore += 1
        else:
            print("That is not correct, try again.") 
    while englishScore == 1:
        englishQuiz = input("Who helped Jabari face his fear?\n")
        if "dad" in englishQuiz.lower() or "father" in englishQuiz.lower():
            print("That is correct")
            englishScore += 1
        else:
            print("That is not correct, try again.")
    while englishScore == 2:
        englishQuiz = input("What did we learn about in Jabari Jumps?\n")
        if "bravery" in englishQuiz.lower() or "to be brave" in englishQuiz.lower() or "overcome your fears" in englishQuiz.lower():
            print("That is correct")
            englishScore += 1
        else:
            print("That is not correct, try again.")    
    textgamelib.printDivider("-", 40)
    print("Jabari: Good Job Son. It's nice to know that you know about me from my book. It's time to take a break and have fun. It's a day off, let's use it well!")
    textgamelib.printDivider("-", 40)
    chapter1EndingArt = text2art("End Of Chapter 1", font="bulbhead")
    print(chapter1EndingArt)
    textgamelib.printDivider("-", 40)
    gameScore += 1
while gameScore == 2:
    chapter2Art = text2art("Chapter 2", font="bulbhead")
    print(chapter2Art)
    textgamelib.printDivider("-", 40)
    print("It's currently the afternoon and your dad Jabari is preparing a gas stove so that he could cook lunch.\nJabari: Hey son, could you do me a favour? I need you to open the windows in the kitchen, the living room, and the dining room. I need this so that we are safe to cook the food. Could you do that for me?")
    input("Objective: Open the windows in the living room, the kitchen and the dining room. \nYou are in the kitchen. \nType 'Where am I' to find out where you are. \nThe kitchen can only go to the dining room.\nPress enter to start.")
    textgamelib.printDivider("-", 40)
    roomList = ["Kitchen", "Dining Room", "Living Room", "Your Bedroom", "Closet"]
    room = 0
    kitchenWindowOpen = False
    diningWindowOpen = False
    livingWindowOpen = False
    while kitchenWindowOpen == False or diningWindowOpen == False or livingWindowOpen == False:
        whichRoom = (roomList[room])
        if whichRoom == (roomList[0]):
            openWindows = input("What would you like to do? \nType 'go out' to leave the kitchen. \nType 'open window' to open the windows.\n")
            if "open" in openWindows.lower() and ("windows" in openWindows.lower() or "window" in openWindows.lower()) and kitchenWindowOpen == False:
                kitchenWindowOpen = True
                print("You opened the window in the kitchen")
                textgamelib.printDivider("-", 40)
            elif "open" in openWindows.lower() and ("windows" in openWindows.lower() or "window" in openWindows.lower()) and kitchenWindowOpen == True:
                print("The window is already open")
                textgamelib.printDivider("-", 40)
            elif "go out" in openWindows.lower() or "exit" in openWindows.lower():
                room += 1
                whichRoom = (roomList[room])
                print("You entered the", whichRoom)
                textgamelib.printDivider("-", 40)
            elif "where am i" in openWindows.lower():
                print("The", whichRoom)
                textgamelib.printDivider("-", 40)
            else:
                print("I can't really understand what you want to do.")
                textgamelib.printDivider("-", 40)
        if whichRoom == (roomList[1]):
            openWindows = input("What would you like to do?\nYou can choose where to go by typing 'Go to'\n")
            if "open" in openWindows.lower() and ("windows" in openWindows.lower() or "window" in openWindows.lower()) and diningWindowOpen == False:
                diningWindowOpen = True
                print("You opened the window in the dining room.")
                textgamelib.printDivider("-", 40)
            elif "open" in openWindows.lower() and "windows" in openWindows.lower() and diningWindowOpen == True:
                print("The window is already open")
                textgamelib.printDivider("-", 40)
            elif "go to" in openWindows.lower():
                whereGo = input("Where would you like to go? The Kitchen, the living room, your bedroom or the closet?\n")
                if "kitchen" in whereGo.lower():
                    room -= 1
                    print("You entered the kitchen.")
                    textgamelib.printDivider("-", 40)
                elif "living room" in whereGo.lower():
                    room += 1
                    print("You entered the living room.")
                    textgamelib.printDivider("-", 40)
                elif "bedroom" in whereGo.lower():
                    room += 2
                    print("You enter your bedroom but remember that you need to open the windows, you go back to the dining room.")
                    textgamelib.printDivider("-", 40)
                    room -= 2
                elif "closet" in whereGo.lower():
                    room += 3
                    print("You check out the closet but remember you ned to open the windows, you head back out to the dining \nroom.")
                    textgamelib.printDivider("-", 40)
                    room -= 3
                else:
                    print("I don't understand where you want to go.")
                    textgamelib.printDivider("-", 40)
            elif "where am i" in openWindows.lower():
                print("The", whichRoom)
                textgamelib.printDivider("-", 40)
            else:
                print("I can't really understand what you want to do.")
                textgamelib.printDivider("-", 40)
        if whichRoom == (roomList[2]):
            openWindows = input("What would you like to do? \nType 'go out' to leave the living room. \nType 'open window' to open the windows.\n")
            if "open" in openWindows.lower() and ("windows" in openWindows.lower() or "window" in openWindows.lower()) and livingWindowOpen == False:
                livingWindowOpen = True
                print("You opened the window in the living room.")
                textgamelib.printDivider("-", 40)
            elif "open" in openWindows.lower() and ("windows" in openWindows.lower() or "window" in openWindows.lower()) and livingWindowOpen == True:
                print("The window is already open")
                textgamelib.printDivider("-", 40)
            elif "go out" in openWindows.lower() or "exit" in openWindows.lower():
                room -= 1
                whichRoom = (roomList[room])
                print("You entered the", whichRoom)
                textgamelib.printDivider("-", 40)
            elif "where am i" in openWindows.lower():
                print("The", whichRoom)
                textgamelib.printDivider("-", 40)
            else:
                print("I can't really understand what you want to do.")
                textgamelib.printDivider("-", 40)
    print("You head back to the kitchen where you see your father.\nJabari: Thanks son. I'm just going to start getting the stove ready. Could you head to the basement to get some beef?\nYou wanted to help but the basement was really dark and scary.")
    basementGo = input("Do you want to go to the basement to get food for your dad? \nYes or No?\n")
    if "yes" in basementGo.lower():
        print("Jabari: Thanks so much, I know you are scared of the basement but it will help me cook more efficiently.")
    if "no" in basementGo.lower():
        print("Jabari: I understand that it is really scary and I know you don't want to go but it would be great if you went.")
    print("In the end, your dad convinced you to go to the basement. \nYou were scared of the dark but it was only to get some beef. \nIt would be quick and easy to help your dad cook. \nNothing's down there that will scare you...Right?")
    textgamelib.printDivider("-", 40)
    chapter2EndingArt = text2art("End Of Chapter 2", font="bulbhead")
    print(chapter2EndingArt)
    textgamelib.printDivider("-", 40)
    gameScore += 1
while gameScore == 3:
    chapter3Art = text2art("Chapter 3", font="bulbhead")
    print(chapter3Art)
    textgamelib.printDivider("-", 40)
    print("You enter the basement to much of your discomfort. \nWhile you did agree to get the beef, you were still scared. \nYour dad said that the beef was in the top shelf of the fridge in the room left of the staircase.")
    input("Objective: Find the beef and get back upstairs. \nThere is a door ahead and a door to the left. \nType 'go to' choose which door to enter.\nPress enter to start.")
    textgamelib.printDivider("-", 40)
    gotBeef = False
    basementRoomList = ["Entrance", "Fridge Room", "Room Forward"]
    basementRoom = 0
    whichRoom = (basementRoomList[basementRoom])
    fridgeOpen = False
    while gotBeef == False:
        whichRoom = (basementRoomList[basementRoom])
        while whichRoom == (basementRoomList[0]):
            actionGetBeef = input("What would you like to do?\n")
            if "go to" in actionGetBeef.lower():
                whichDoor = input("Which door would you like to enter? \nLeft or Forward?\n")
                if "left" in whichDoor.lower():
                    print("You open and enter the left door. \nIt's pretty dark so you can't really see but you can try inspecting the room to see what's in it.")
                    textgamelib.printDivider("-", 40)
                    whichRoom = (basementRoomList[1])
                elif "forward" in whichDoor.lower():
                    input("You open and enter the door in front of you. \nIt's pretty dark here so you can't see well but if you inspect the room you might find some things. Something smells and you thought you heard some growling. \nYou left the room just to be safe.\nPress enter to continue.")
                    textgamelib.printDivider("-", 40)
                else:
                    print("I can't really understand where you want to go")
                    textgamelib.printDivider("-", 40)
            elif "where am i" in actionGetBeef.lower():
                print("You are in a small room with two doors to choose from. \nOne is to your left and one is to your right. Behind you is the staircase leading back upstairs.")
                textgamelib.printDivider("-", 40)
            else:
                print("You've either printed an unavailible action or something that I can't understand.\nPlease try again.")
        while whichRoom == (basementRoomList[1]):
            actionGetBeef = input("What would you like to do? \nTo leave the room type 'go out'. \nTo inspect the room type 'inspect'.\n")
            if "inspect" in actionGetBeef.lower():
                input("The room is fairly cold. \nYou look further to see that it is because of a refridgerator in the room. \nThis might be the refridgerator that the beef is in. \nIf you open the fridge you can see what's in it. \nYou heard a faint growling coming from the other room so you'd better leave quickly. \nTrying opening the fridge.\nPress enter to continue.")
                textgamelib.printDivider("-", 40)
            elif "go out" in actionGetBeef.lower() or "exit" in actionGetBeef.lower():
                print("You leave the room")
                textgamelib.printDivider("-", 40)
                basementRoom -= 1
            elif "open" in actionGetBeef.lower() and ("fridge" in actionGetBeef.lower() or "refrigerator" in actionGetBeef.lower()):
                input("You open the fridge. \nThere is some meat, vegetables and fruit in the fridge. \nYou see the beef that your dad wanted you to get. \nYou should take it and go back up. Your dad might be waiting. \nThe growling is getting clearer so you'd want to get out before you find out what's making it. \nTry typing 'Get beef' now.\nPress enter to continue.")
                textgamelib.printDivider("-", 40)
                fridgeOpen = True
            elif "get beef" in actionGetBeef.lower() and fridgeOpen == True:
                whichRoom = (basementRoomList[0])
                gotBeef = True
                print("You got the beef and left the room")
                textgamelib.printDivider("-", 40)
            elif "get beef" in actionGetBeef.lower() and fridgeOpen == False:
                print("You don't see the beef. \nTry opening the fridge.")
                textgamelib.printDivider("-", 40)
            else:
                print("You've either printed an unavailible action or something that I can't understand.\nPlease try again.")
    print("As you were about to walk up with the beef you heard growling coming from the other room. \nYou turned to see a really big dog, almost half as tall as you were. \nYou knew that none of your neighbours had dogs so this one was not going to be friendly. \nIt's sharp teeth were showing and you were very scared.")
    decisionMade = False
    while decisionMade == False:
        dogDescision = input("Will you run away or call for help?\n")
        if "run away" in dogDescision.lower():
            print("You run upstairs to your dad.\nJabari: What's wrong son?\nYou: There's a huge dog in the basement!\nJabari: That's not good. Let's check it out.\nBoth of you carefully head downstairs and check on the dog. \nThe dog sees your dad and the dog starts to calm down.\nJabari: This is one of the new nieghbour's dog. You should know that dogs can smell your fears so that you should always be brave when you are with a dog.")
            decisionMade = True
        if "call for help" in dogDescision.lower():
            print("You yell for help. \nYou stand your ground while inching away from it. \nYour dad rushed down.\nJabari: What's wrong?\nYou: There's a dog here. It's big and scary. \nYour dad sees the dog.\nJabari: This is one of the new nieghbour's dog. It's good that you were brave. You should know that dogs can smell your fears so that you should always be brave when you are with a dog.")
            decisionMade = True
        else:
            print("I can't understand what you want to do. \nYou should choose quickly the dog is scary.")
    input("You wait with the dog for the neighbours. \nYou got used to the dog and learned to be brave when you are with it. \nThe flooding eventually stopped and the neighbours came to pick it up. \nYou returned to your normal life, but with the experience of bravery and the tale of the blackout.\nPress enter to end the game.")
    textgamelib.printDivider("-", 40)
    chapter3EndingArt = text2art("End Of Chapter 3", font="bulbhead")
    print(chapter3EndingArt)
    textgamelib.printDivider("-", 40)
    gameScore += 1
while gameScore == 4:
    endingArt = text2art("Thanks For Playing", font="small")
    print(endingArt)
    gameScore += 1