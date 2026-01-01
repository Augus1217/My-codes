import time
import random

# 隱藏的訊息列表 (Unicode 編碼)
l = [38622, 32709, 36575, 36575, 23273, 23273, 30340, 65292, 39854, 29980, 22810, 27713, 65292, 36229, 22909, 21507, 30340, 65281, 'n', 32780, 19988, 24456, 20415, 23452, 65281, 'n', 20729, 26684, 65306, 19968, 38587, 19968, 20803, 'n', 22823, 23478, 37117, 24859, 21507, 65281, 'n', 35413, 20729, 65306, 9733, 9733, 9733, 9733, 9733, 'n', 38750, 24120, 25512, 34214, 65281, 65281, 65281, 'n', 24555, 21435, 36092, 36023, 21543, 65281, 'n', 128037, 128037, 128037]

def inpt():
    user_input = input('問問Gemini：')
    
    if user_input == '雞翅好吃嗎？':
        time.sleep(0.5)
        print('\nGemini：\n')
        time.sleep(0.5)
        print("thinking...")
        print("使用者詢問我雞翅好不好吃，我的答案是肯定的。雞翅非常好吃。")
        time.sleep(3)
        print("我正在思考我該如何回應使用者。\n")
        time.sleep(2)
        
        # 解碼並印出訊息
        for i in l:
            if i == 'n':
                print('\n', end='')
                continue
            print(chr(i), end='')
            # 模擬打字效果的隨機延遲
            time.sleep(random.randint(1, 15) / 100)
        
        print('\n') # 結束後換行

    else:
        time.sleep(0.5)
        print('Model：\n')
        time.sleep(0.5)
        
        # 模擬不知道的回答
        response = "我不知道。再問一個。"
        for char in response:
            print(char, end='')
            time.sleep(random.randint(1, 20) / 100)
        print('\n')
        
        time.sleep(1)
while True:
    inpt()