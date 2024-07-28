import random

answer = random.randint(1,5)

correct = False

count = 1

while correct != True: 
    userAns = input(" Pick The Num from 1-5 ")
    if int(userAns) == answer: 
        correct = True
        print(count)
        break
    else:
        count+=1
        print("wrong")