import random

ranking = []

while(True):
    print()
    print("원하는 메뉴를 눌러주세요!")
    print("1. 게임 시작 / 2. 랭킹 보기 / 3. 게임 종료")
    status = int(input())
    print()

    if status == 1:
        print("게임 시작!")

        target = random.randint(1, 100)
        count = 1

        while(True):
            print("추측해보세요!")
            guessnum = int(input())
            print()

            if target == guessnum:
                print(f"정답입니다! 값은 {target}이고, {count}번 만에 맞추셨어요!")
                ranking.append(count)
                break

            elif target > guessnum:
                print("더 높게 입력하세요!")
                count += 1

            elif target < guessnum:
                print("더 작게 입력하세요!")
                count += 1

    if status == 2:
        print("랭킹 보기")

        ranking.sort()

        if len(ranking) == 0:
            print("아직 기록이 없습니다.")
        else:
            rank = 1

            for i in range(len(ranking)):
                if i == 0 or ranking[i] != ranking[i - 1]:
                    people = ranking.count(ranking[i])
                    print(f"{rank}위 : {ranking[i]}번 ({people}명)")
                    rank += 1


    if status == 3:
        print("게임 종료")
        break