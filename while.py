# while문

# 조건이 맞을때까지 실행
# while 문을 조건이 True인 동안 계속 반복
# 반복 멈추고 싶다. False로 만들기

# for i in range(5):
#     print(i+1) # 1 2 3 4 5

i = 0 #초기값
while i < 5: #True 1. 강제종료 2.False
    print(i+1) # 0 + 1
    i += 1

i = 0 #초기값
while i < 5:
    i += 1
    print(i+1)


num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)