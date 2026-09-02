# 실습 - 저축하기2
# for문 / 조건문 / break, continue 사용해서
# 달성금액과 일차 알려주기
# 매일 13,500원 저축한다.
# 16만원을 모으기 위해서 걸리는 일차는? (주말 제외)

# 방법 1 (단순히 % 나머지로 6,7일을 제외하기)


print("얼마 저금하시나요?")
saving = int(input())
print(f"{saving}원씩")
print()
target = 160000
total = 0
count = 0

for day in range(1, 100000):  # day는 일수/회차를 나타냄
    if day % 7 == 6 or day % 7 == 0:  # 토/일 제외
        continue

    total += saving
    count += 1

    if total >= target:
        break

print(f"{day}일차에 목표금액 {total}을 달성하셨어요!", end="")
print(f"(주말 {day-count}일 제외)")


# 방법2 인덱스를 통한 요일 인식
"""
print("얼마 저금하시나요?")
saving = int(input())

print("시작 요일도 입력해주세요 ex) 월,화,수,목,금,토,일")
start_day = input().strip()

weekdays = ["월", "화", "수", "목", "금", "토", "일"]
workday = [1, 1, 1, 1, 1, 0, 0]

target = 160000

start_index = weekdays.index(start_day)

money = 0
count = 0

while money < target:
    day_name = weekdays[start_index]
    count += 1

    if workday[start_index] == 1:
        money += saving
        print(f"{day_name}요일: {money}원 저축 완료")
    else:
        print(f"{day_name}요일: 쉬는 날")

    start_index = (start_index + 1) % 7

print(f"총 {count}일 걸려요.")
print(f"목표 금액 {target}원 달성! 마지막 저축일은 {weekdays[(start_index - 1) % 7]}요일입니다.")
"""

# 다른 방법? (AI 답변 - def함수사용)

"""
import math

WEEKDAYS = ["월", "화", "수", "목", "금", "토", "일"]
WORKDAYS = {0, 1, 2, 3, 4}  # 월~금

def calculate_saving(saving, target, start_day):
    if saving <= 0:
        raise ValueError("저축 금액은 0보다 커야 합니다.")

    if start_day not in WEEKDAYS:
        raise ValueError("요일은 월, 화, 수, 목, 금, 토, 일 중 하나여야 합니다.")

    start_index = WEEKDAYS.index(start_day)
    required_deposits = math.ceil(target / saving)

    total = 0
    deposit_count = 0
    calendar_days = 0
    current_index = start_index

    while deposit_count < required_deposits:
        calendar_days += 1

        if current_index in WORKDAYS:
            total += saving
            deposit_count += 1

        current_index = (current_index + 1) % 7

    last_saving_day = WEEKDAYS[(current_index - 1) % 7]

    return calendar_days, total, last_saving_day


saving = int(input("얼마 저금하시나요? "))
start_day = input("시작 요일을 입력해주세요 (월, 화, 수, 목, 금, 토, 일): ").strip()

target = 160000

try:
    days, total, last_day = calculate_saving(saving, target, start_day)

    print(f"{days}일 만에 목표 금액을 달성했어요.")
    print(f"저축 금액: {total}원")
    print(f"쉬는 날: {days - math.ceil(target / saving)}일")
    print(f"마지막 저축일: {last_day}요일")

except ValueError as error:
    print(error)

"""

# 메인 개념은 아무래도 정확도를 위해 index도입후 하는 방식인듯?
# 제일 핵심 개념은 index = (index + 1) % 7