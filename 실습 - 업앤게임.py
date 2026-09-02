# while문과 조건문을 활용해서 1부터 100까지의 숫자를
# 랜덤으로 받습니다.
# input을 통해서 입력한 값과 비교해서
# 나의 입력 값이 랜덤 값보다 작으면 '더 높게 입력하세요'
# 반대로 높다면 '더 작게 입력하세요'
# ==면 '정답입니다!' 게임이 종료되게 만들어주시면 됩니다.

import random #불러오기 라이브러리를 불러온다.


target = random.randint(1,100)
count = 1

while (True):
    print("추측해보세요!")
    guessnum = int(input())
    print()

    if target == guessnum:
        print(f"정답입니다! 값은 {target}이고, {count}번만에 맞추셨어요!")
        break

    elif target > guessnum:
        print("더 높게 입력하세요!")
        count+=1

    elif target < guessnum:
        print("더 작게 입력하세요!")
        count+=1