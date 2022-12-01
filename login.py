import json
from tkinter.tix import Tree
from fast_typing import Fastyping
from quiz import Questions

# class login:
check = False
quizgame = Questions
typingGame = Fastyping
global username
isfound = False
data=[]
global isagain, chooseGame, LOL
isagain = True
# LOL = True
chooseGame = 0

def register():
    with open('User_Data.txt', 'r') as f:
        data = f.read()
        data = data.split("\n")
        username = input('♡ Create Username ♡ :')
        f = open('User_Data.txt', 'a')
        f.write("\n" + username)
        f.close()
        print('→ Registered. Please Log-in ←')
        login()

def login():
    username = input('♡ Enter Username ♡ :')
    global check
    with open('User_Data.txt', 'r') as f:
        data = f.read()
        data = data.split("\n")
        if username in data:
            print(f"♫ Hello, {username} We glad that you're here! (っゝωò)っ wow ! * ✰")
            check = True
            return username
        else:
            print("Sorry. We could not find a user (。-`ω '-)")
            print('Please try agiain')
            check = False
        f.close()

def choices():
    print('✩ ✩ ✩  Welcome! ✩ ✩ ✩')
    print('⋆ 𝄞 Please choose Log-in or Register. ࿓')
    print('⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑ ⌑')
    choice = int(input('𓇬 ∙ For Register Type 1 and For Log-in Type 2 : ∙ 𓇬'))
    if choice == 1:
        register()
    elif choice == 2:
        while check == False:
            if check == False:
                username = login()
                return username
            elif check == True:
                break

def menu():
    print("-" * 25)
    print("✩ Quiz Game press '1' ✩")
    print("✩ Fast Typing Game press '2' ✩")
    print("✩ Leader board press '3' ✩")
    print("✩ Exit press '0' ✩")

def playAgain():
    LOL = True
    isagain = True
    while LOL:
        playnomore = input("༄ If you want to play again press ✮ Yes ✮ if not press ✮ No ✮ : ")
        if playnomore == "Yes":
            isagain = True
            LOL = False
            return isagain
        elif playnomore == "No":
            LOL = False
            isagain = False
            return isagain
        else:
            print("Enter Yes or No")
            continue

def showScoreQuizGame():
    with open('data.json','r') as sc:
        score = json.load(sc)
        for e in score:
            print(e['username'], e['score'], "point")
        # print(score)

def showScoreTypingTest():
    with open("data1.json", "r") as sc:
        usertime = json.load(sc)
        for i in usertime:
            print(i["username"], i["time"], "second")

def chooseScoreGame():
    print('✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴  ✴')
    print("Press '1' for Quizgame press '2' for TypingTest game")
    chooseGame = input("∙ ✧ ꙳ What game do you want to check score : ✔")
    if chooseGame == "1":
        showScoreQuizGame()
    elif chooseGame == "2":
        showScoreTypingTest()
    else:
        print("please enter number 1 or 2")
# ========================== main ============================== 
user = choices()
while isagain == True:
    menu()
    choose = int(input('Choose Your Fighter : '))
    if choose == 1:
        print('Welcome to Quiz Game!')
        print('♡ -> Answer tricky questions and test your knowlegde!')
        quizgame.game(user)
        isagain = playAgain()
    elif choose == 2:
        print('Welcome to Fast Typing Game')
        print('♡ -> Get those fingers flying across the keyboard faster as you can!')
        typingGame.gameTyping(user)
        isagain = playAgain()
    elif choose == 3:
        print("-" * 25)
        print('This is Leader board. Please check your score!')
        chooseScoreGame()
        isagain = playAgain()
    elif choose == 0:
        isagain = False
        break
    else:
        print('Sorry. Please choose again')