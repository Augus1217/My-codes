# @title 1: chatgpt!?
def inpt():
    if input('問問Gemini：')=='雞翅好吃嗎？':
        print('\n')
        return 0
    else:
        time.sleep(0.5)
        print('Chatgpt的回應：\n')
        time.sleep(0.5)
        print('我',end='')
        time.sleep(random.randint(1,20)/100)
        print('不',end='')
        time.sleep(random.randint(1,20)/100)
        print('知',end='')
        time.sleep(random.randint(1,20)/100)
        print('道',end='')
        time.sleep(random.randint(1,20)/100)
        print('。\n',end='')
        time.sleep(random.randint(1,20)/100)
        print('再',end='')
        time.sleep(random.randint(1,20)/100)
        print('問',end='')
        time.sleep(random.randint(1,20)/100)
        print('一',end='')
        time.sleep(random.randint(1,20)/100)
        print('個',end='')
        time.sleep(random.randint(1,20)/100)
        print('。\n')
        time.sleep(1)
        inpt()
import time
import random
inpt()
l=[38622,32709,36575,36575,23273,23273,30340,65292,39854,29980,22810,27713,65292,36229,22909,21507,30340,65281,'n',32780,19988,24456,20415,23452,65281,'n',20729,26684,65306,19968,38587,19968,20803,'n',22823,23478,37117,24859,21507,65281,'n',35413,20729,65306,9733,9733,9733,9733,9733,'n',38750,24120,25512,34214,65281,65281,65281,'n',24555,21435,36092,36023,21543,65281,'n',128037,128037,128037,]
time.sleep(0.5)
print('Gemini的回應：\n')
time.sleep(0.5)
for i in l:
    if i=='n':
        print('\n',end='')
        continue
    print(chr(i),end='')
    time.sleep(random.randint(1,20)/100)