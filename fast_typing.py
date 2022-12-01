from ast import Global
import imp
import random
import string
import time
import json
import math
from typing import List

class Fastyping:

    def gameTyping(username):
        scoretime = []
        # sctime = []
        randomfruits = ""
        usertime = float
        global user_out
        user_out = True
        global fruits
        fruits = []
        mylist = ["tomato", "banana", "cherry", "papaya", "melon", "watermelon", "coconut", "lime", "orange", "blackberry"]
        x = 0
        while user_out == True:
            with open('data1.json',mode='r', encoding='utf8') as f:
                scoretime += json.load(f)


            fruits = random.sample(mylist,5)
            num = len(fruits)
            i=0
            while i < num:
                randomfruits += fruits[i]+ " "
                i += 1

            print("---------------------------------------------------------------------------")
            print("\t\t " + randomfruits)
            print()
            start = time.time()
            input1 = input("     Write the words shown above! :")
            end = time.time()
            if "".join(input1.split()) == "".join(randomfruits.split()):
                usertime = (" ---{:.2f} seconds---".format(end-start))
                user_time_double = round(end-start,3)
                # sctime.append(user_time_double)
                print("\t\t\t=results and time spent=")
                print("\t\t\t      [correct]")
                print("\t\t\t "+usertime)
                # print(type(scoretime[usertime]))
                user_want_to_play = input("you want to play : P/ you want to exit : Q  :")
                if(user_want_to_play == "P" or user_want_to_play == "p"):
                    user_out = True
                    randomfruits = ""
                    with open('data1.json',mode='w', encoding='utf8') as f:
                        # scoretime['usertime'] = user_time_double
                        scoretime.append({"username":username, "time": user_time_double})
                        f.write(json.dumps(scoretime))
                    x += 1
                else :
                    x += 1
                    user_out = False  
                    with open('data1.json',mode='w', encoding='utf8') as f:
                        scoretime.append({"username":username, "time": user_time_double})
                        f.write(json.dumps(scoretime))
            
            else :
                print("\t\t\t    [incorrect]")
                user_want_to_play = input("you want to play : P/ you want to exit : Q")
                if(user_want_to_play == "P" or user_want_to_play == "p"):
                    user_out = True
                    randomfruits = ""
                    with open('data1.json',mode='w', encoding='utf8') as f:
                        scoretime.append({"username":username, "time": user_time_double})
                        f.write(json.dumps(scoretime))
                    x += 1
                else :
                    user_out = False
                    with open('data1.json',mode='w', encoding='utf8') as f:
                        scoretime.append({"username":username, "time": user_time_double})
                        f.write(json.dumps(scoretime))
                    x += 1

            print("---------------------------------------------------------------------------")

        # user = "fluke"
        # with open('data.json','r') as sc:
        #     usertimel = json.load(sc)
        #     print(usertime)
        #     for i in range(len(usertime)):
        #         if user == usertime[i]['username']:
        #             usertime[i]['usertime']+=usertime
        #     else:
        #         usertime_new = 0
        #         usertime_data = {'username':user,'usertime':usertime_new}
        #         usertimel.append(usertime_data)
        # with open('data.json','w') as sc:
        #     # data = json.dumps(sc)
        #     # data['score'] = score
        #     dt = json.dumps(usertimel,indent=4)
        #     sc.write(dt)
        # user = "fluke"
        # with open('data.json','r') as sc:
        #     usertimel = json.load(sc)
        #     print(usertime)
        #     for i in range(len(usertime)):
        #         if user == usertime[i]['username']:
        #             usertime[i]['usertime']+=usertime
        #     else:
        #         usertime_new = 0
        #         usertime_data = {'username':user,'usertime':usertime_new}
        #         usertimel.append(usertime_data)
        # with open('data.json','w') as sc:
        #     # data = json.dumps(sc)
        #     # data['score'] = score
        #     dt = json.dumps(usertimel,indent=4)
        #     sc.write(dt)

        # x = { "name":"John", "age":30, "city":"New York"}
        # scoreDict = {"fScore" : score}
        # print("Your score",scoreDict) #9
        # f = open("data.json", "r")
        # f.append(scoreDict)
        # # json.dump()
        # # json.load(["score"])
        # f.close
