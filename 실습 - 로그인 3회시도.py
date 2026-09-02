# 실습 - 로그인 3회시도
# 반복문 / 조건문 / break / 논리연산자 / 연산
# ID와 PASSWORD 입력한다.
# 로그인 성공 시, 로그인이 성공했습니다!
# 실패 - 1회 실패하셨습니다. (2회남았습니다.)
# 실패 - 3회 실패하셨습니다. 계정이 정지되었습니다 - 고객센터에 문의해주시기 바랍니다.

# 실습 - 로그인 3회시도만들기2
# 기능 2개 추가해보기

for i in range(1,4):
    id = input("아이디를 입력해주세요 ")
    if (id != "admin"):
        print("존재하지 않는 아이디입니다. 다시 로그인 해주세요")
        break

    password = input("비밀번호를 입력해주세요 ")

    if(id == "admin" and password == "1234"):
        print()
        print("**로그인이 성공했습니다!**")
        print()


        while (True):
            print("원하는 메뉴번호를 선택해주세요!")
            print("1. 내정보 보기 / 2. 비밀번호 변경 / 3. 로그아웃")
            print()
            menuselect = int(input())
            if menuselect == 1:
                print(f"내 아이디는 : {id}입니다.")
                print(f"내 비밀번호는 : {password}입니다.")
                if(password != "1234"):
                    break
                print()

            elif menuselect == 2:
                print("현재 비밀번호를 입력해주세요!")
                nowpw = input()
                if (nowpw == "1234"):
                    print("변경하실 비밀번호를 입력하세요!")
                    newpw = input()
                    password = newpw
                    continue

                elif (nowpw != "1234"):
                    print("비밀번호 오류! 처음부터 다시 입력하세요!")
                    continue

            elif menuselect == 3:
                print("로그아웃 합니다.")
                break

        break

    if(id == "admin" and password != "1234"):
        if (i==3):
            print("계정이 정지되었습니다. - 고객센터로 문의해주시기 바랍니다.")
        else:
            print(f"비밀번호 입력 {i}회 실패하셨습니다. ({3 - i}회 남았습니다)")

