import json


class Questions:
    global score
    def game(username):

        questions = {
            "เนื้ออะไรกินแล้วปลอดภัยที่สุด?":['a.หอย', 'b.หมู', 'c.วัว', 'd.จระเข้','a'],
            "อะไรทเพื่อวัด?":['a.พระสงฆ์', 'b.ไม้บรรทัด', 'c.เจ้าอาวาส', 'd.โยม', 'b'],
            "ประตูกลัวอะไร":['a.ไฟ', 'b.หน้าต่าง', 'c.เลื่อย', 'd.ต้นไม้', 'a'],
            "เทียนอะไรเอ่ยกลิ่นแรง??":["a.เทียนหอม","b.เทียนไข","c.เทียนรุ","d.เทียนต้ม", 'c'],
            "พญานาคอยู่ที่ไหน?":['a.น้ำโขง', 'b.น้ำสิงค์','c.น้ำเต้าฮู้','d.กล่องไม้ขีด', 'd'], 
            "คนเราต้องกินอะไรทุกวัน(ห้ามตอบกินน้ำ)":['a.กํ้านิน','b.ข้าว','c.อากาศ','d.ลูกปืน','a']
        } # 1
        scorel = 0 # 2
        for question_number,question in enumerate(questions): # 3
            print ("Question",question_number+1) # 4
            print (question)

            for options in questions[question][:-1]: # 5
                print (options)
            user_choice = input("Make your choice : ")

            if user_choice == questions[question][-1]: # 6
                print ("ถั่วต้มแล้วค้าบบ! ( ͡♥ 3 ͡♥)")
                if question_number+1 == 1:
                    scorel += 10 #7 here's the relevant part of the question
                # else:
                #     print()
                elif question_number+1 == 2:
                    scorel += 10 #7 here's the relevant part of the question
                    
                elif question_number+1 == 3:
                    scorel += 10 #7 here's the relevant part of the question
            
                    
                elif question_number+1 == 4:
                    scorel += 10 #7 here's the relevant part of the question
            
                elif question_number+1 == 5:
                    scorel += 10 #7 here's the relevant part of the question
                
                elif question_number+1 == 6:
                    scorel += 10 #7 here's the relevant part of the question
            
            else: # 8
                print ("ว้ายยยยผิด! (○ﾟεﾟ○)")

                if question_number+1 == 1:
                    print("เฉลย =======>  หอย (เพราะ หอย มี อย.)")
                # else:
                #     print()
                elif question_number+1 == 2:
                    print("เฉลย =======> ไม้บรรทัด")
                    
                elif question_number+1 == 3:
                    print("เฉลย =======> กลัวไฟ เพราะมีประตูหนีไฟ")
            
                    
                elif question_number+1 == 4:
                    print("เฉลย =======> เทียนรุ ทุเรียน")
            
                elif question_number+1 == 5:
                    print("เฉลย =======> กล่องไม้ขีด อยู่ข้างกล่องไม้ขีด")
                
                elif question_number+1 == 6:
                    print("เฉลย =======> ก้ำนิน ผวน = กินน้ำ")
            
            print("------------------------")
        user = username
        with open('data.json','r') as sc:
            score = json.load(sc)
            for i in range(len(score)):
                if user == score[i]['username']:
                    score[i]['score']+=10
            else:
                score_new = scorel
                score_data = {'username':user,'score':score_new}
                score.append(score_data)
        with open('data.json','w') as sc:
            # data = json.dumps(sc)
            # data['score'] = score
            dt = json.dumps(score,indent=4)
            sc.write(dt)
        with open('data.json','r') as sc:
            score = json.load(sc)
            print(score)

    # x = { "name":"John", "age":30, "city":"New York"}
    # scoreDict = {"fScore" : score}
    # print("Your score",scoreDict) #9
    # f = open("data.json", "r")
    # f.append(scoreDict)
    # # json.dump()
    # # json.load(["score"])
    # f.close

                
            

