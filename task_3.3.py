#LAB 3-6
for i in range(5):
    print(i, 'Hello, python!')


for i in range(5):
    print(i)

#LAB 3-7
list1 = list(range(1, 101))
print("1번:", list1)

list2 = list(range(2, 101, 2))
print("2번:", list2)

list3 = list(range(1, 101, 2))
print("3번:", list3)

list4 = list(range(-99, 0))
print("4번:", list4)


#LAB 3-8
sum1 = 0
for i in range(1, 101):
    sum1 += i
print("1번 (1~100 합계):", sum1)

sum2 = 0
for i in range(0, 101, 2):
    sum2 += i
print("2번 (1~100 짝수 합):", sum2)


sum3 = 0
for i in range(1, 101, 2):
    sum3 += i
print("3번 (1~100 홀수 합):", sum3)


#LAB 3-9
for i in range(7):
    #공백을 출력하는 안쪽 루프(첫 줄은 6칸, 마지막 줄은 0칸)
    for j in range(6 - i):
        print(" ", end="")

    #공백 출력 후 '#'을 찍고 출을 바꿉니다.
    print("#")









