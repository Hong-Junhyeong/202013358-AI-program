
# 7-1
import datetime

now = datetime.datetime.now()

if now.hour < 12:
    ampm = "오전"
    hour_12 = now.hour

else:
    ampm = "오후"
    hour_12 = now.hour if now.hour == 12 else now.hour - 12

print(f"오늘의 날짜: {now.year}년 {now.month}월 {now.day}일")
print(f"현재시간 : {ampm} {hour_12}시 {now.minute}분 {now.second}초")

# 7-2
from datetime import datetime

today = datetime(2026, 4, 16)
print(f"오늘은 {today.year}년 {today.month}월 {today.day}일입니다")

xmas =datetime(2026, 12, 25)
diff = xmas - today
print(f"2026년 크리스마스까지는 {diff.days}일 {diff.seconds // 3600}시간 남았습니다.")

new_year = datetime(2036, 1, 1)
diff2 = new_year - today
print(f"2036년 새해 까지는 {diff2.days}일 {diff2.seconds // 3600}시간 남았습니다.")

birthday = datetime(2027, 4, 15)
diff3 = birthday - today
print(f"2027년 생일까지는 {diff3.days}일 {diff3.seconds // 3600}시간 남았습니다.")


# 7-3
from datetime import datetime, timedelta

today = datetime.now()
thousand_days = today + timedelta(days=1000)
print(f"오늘부터 1000일 후의 날짜: {thousand_days.year}년 {thousand_days.month}월{thousand_days.day}일")

input_date = input("처음으로 사귄 연도와 월, 일을 입력하시오 : ").split()
year, month, day = map(int, input_date)

start_date = datetime(year, month, day)
hundred_days = start_date + timedelta(days=99)

print(f"100일 기념일은 : {hundred_days.year}년 {hundred_days.month}월 {hundred_days.day}일입니다.")


# 7-3
from datetime import datetime, timedelta

today = datetime.now()
thousand_days = today + timedelta(days=1000)
print(f"오늘부터 1000일 후의 날짜: {thousand_days.year}년 {thousand_days.month}월 {thousand_days.day}일")

input_date = input("처음으로 사귄 연도와 월, 일을 입력하시 : ").split()
year, month, day = map(int, input_date)

start_date = datetime(year, month, day)
hundred_days = start_date + timedelta(days=99)

print(f"100일 기념인은 : {hundred_days.year}년 {hundred_days.month}월 {hundred_days.day}일입니다.")

input_date = input("처음으로 사귄 연도와 월, 일을 입력하시오 : ").split()
year, month, day = map(int, input_date)

start_date = datetime(year, month, day)
hundred_days = strat_date + timedelta(days=99)

print(f"100일 기념일은 : {hundred_days.year}년 {hundred_days.month}월 {hundred_days.day}일입니다.")


# 7-4
import math

for i in range(2, 11):
    print(f"4**{i:2} = {math.pow(4, i):10.1f}")

print("-" * 30)

for degree in range(0, 181, 10):
    radian = math.radians(degree)
    print(f"{degree:3} degree = {radian:.3f} radian")

print("-" * 30)

for degree in range(0, 181, 10):
    radian = math.radians(degree)
    sin_value = math.sin(radian)
    print(f"sin({degree:3}) = {sin_value:.2f}")


# 7-5
import random

five_multiples = []
while len(five_multiples) < 3:
    num = random.randrange(0, 101, 5)
    if num not in five_multiples:
        five_multiples.append(num)

print("0에서 100이하의 정수 중에서 5의 배수")
print(five_multiples)

sample_list = random.sample(range(1, 11), 3)
print(f"1에서 10 사이의 임의의 정수 : {sample_list}")


# 7-7
import turtle

t = turtle.Turtle()
t.shape("turtle")

lengths = [100, 200]

for length in lengths:
    for _ in range(3):
        t.forward(length)
        t.left(120)

t.clear

lengths_3 = [100, 200, 300]

for length in lengths:
     for _ in range(3):
         t.forward(length)
         t.left(120)

t.penup
t.goto(-150, 0)
t.pendown()

for _ in range(4):
    t.forward(100)
    t.left(90)

turtle.done()


# 8-1
try:
    a = [10, 20, 30]
    print(a[3])
except Exception as e:
    print(f"오류 메시지: {e}")

try:
    n = int('20%')
except Exception as e:
    print(f"오류 메시지: {e}")

try:
    a = 100 + '200'
except Exception as e:
    print(f"오류 메시지: {e}")

# 8-2
try:
    result = 10*(30 / 0)
except ZeroDivisionError:
    print("오류: 0으로 나눌 수 없습니다.")


try:
    x = int(input('정수 x를 입력하세요: '))
except ValueError: 
    print("오류: 정수만 입력해야 합니다.")

import sys
try:
    f = open('myfile.txt')
    s = f.readline()
except FileNotFoundError:
    print("오류: 파일을 찾을 수 없습니다.")


# 8-3
a = [1, 2, 3, 4, 5]
korean_orders = ["첫 번째", "두 번째", "세 번째", "네 번째", "다섯 번째"]

try:
    user_input = input("a의 요소를 하나 선택하시오 : ")
    idx = int(user_input) - 1

    if 0 <= idx < len(a):
        print(f"{a[idx]} 은(는) {korean_orders[idx]} 요소입니다.")
    else:
        print("오류: 리스트의 범위를 벗어난 숫자입니다.")

except ValueError:
    print("오류 : 입력 값이 정수나 실수가 아님")



