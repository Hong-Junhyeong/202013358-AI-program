game_score = 800
if game_score >1000:
    print('당신의 고수입니다')


num_a, num_b = 300, 300
if num_a == num_b:
    print('두값이 일치합니다')




n = int(input('정수를 입력하세요 : '))
print('n=', n)

if n % 2 == 0:
      print(n, '은(는) 짝수입니다')


x = int(input('정수를 입력하세요 : '))
print('x=', x)

if x > 0:
    print(x, '은(는) 자연수입니다')




game_score = int(input('게임점수를 입력하시오 : '))
print('game_score =', game_score)

if game_score >= 1000:
    print('고수입니다.')
eles:
    print('입문자입니다.')


num_a = int(input('한 정수를 입력하시오 : '))
num_b = int(input('다른 정수를 입력하시오 : '))

if num_a == num_b:
    print('두 값이 일치합니다.')
else:
    print('두 값이 일치하지 않습니다.')


# 1) 성인 여부 확인
is_adult = int(input('당신은 성인인가요(성인이면 1, 미성년자면 0): '))

if is_adult == 0:
    print('당신은 미성년자입니다.')
else:
    # 2) 성인일 경우(1 입력) 결혼 여부 확인
    is_married = int(print('결혼을 하셨나요(기혼이면 1, 미혼이면 0): '))

    if is_married == 1:
        print('당신은 결혼한 성인입니다.')
    else:
        print('당신은 결혼하지 않은 성인입니다.')




num = 2
# 빈칸에 들어갈 코드
print(num > 1 and num < 10)


# (1) age = 10인 경
age = 10
if age > 10 and age < 19:
    print('청소년입니다.')




# 사용자로부터 정수 입력을 받습니다
speed = int(input('자동차의 속도를 입력하세요(단위 : km/h):'))

if speed >=100:
    print('고속')
elif speed >=60:
    # 100 미만인 값들 중에서 60 이상인 경우만 여기로 들어옵니다
    print('중속')
else:
    # 60 미만인 모든 경우
    print('저속')






