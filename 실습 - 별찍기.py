# print("몇 줄 별 만드실건가요?")
# j = int(input())
# for i in range(0, j):
#     print("*"*(i+1))
#
# print("몇 줄 역별 만드실건가요?")
# l = int(input())
# for k in range(l,0,-1):
#     print(" " * (l - k),end="")
#     print("*"*k)
#
#
# for i in range(1,6):
#     print("*"*i)
#
# print()
#
# for i in range(0,5):
#     print(" "*i,end="")
#     print("*"*(5-i))
#
# print()
#
# for i in range(0,5):
#
#     print(" "*(5-i),end="")
#     print("*"*(2*i+1))
#
# print()
#
# for i in range(0,5):
#     print("  "*4,end="")
#     print(" "*(4-i),end="")
#     print("★"*(i+1))
# for i in range(15,10,-1):
#     print(" "*(15-i),end="")
#     print("★"*i)
# for i in range(10,16):
#     print(" "*(15 - i),end="")
#     print("★"*i)
# for i in range(5,0,-1):
#     print("  " * 4, end="")
#     print(" "*(5-i),end="")
#     print("★"*i)
#

print("원하는 행 입력")
num=int(input())

for i in range(num,0,-1):
    print("*"*(i-1),end="")
    print(" "*(2*(num-i)+1),end="")
    print("*"*(i - 1))

for i in range(1,num):
    print("*"*(i),end="")
    print(" "*(2*(num-i)-1),end="")
    print("*"*i)