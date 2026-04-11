
#6-1
capital_dic = { 'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}
print(capital_dic)


furits_dic = {'apple': 5000, 'banana': 4000, 'grape': 5300, 'melon': 6500}
print(furits_dic)

#6-2
person = {'이름': '홍길동', '나이': 26, '몸무게': 82}

person['특기'] = '분신술'
person['아버지'] = '홍판서'

del person['나이']

print(person)

#6-3
capital_dic = { 'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}

print('Korea' in capital_dic)     
print('China' in capital_dic)     
print('Indonesia' in capital_dic)     
print('Beijing' in capital_dic)

#6-4
fruits_dic = {'apple': 6000, 'banana': 5000, 'orange': 7000, 'melon': 3000}


print(f"2번 결과: {fruits_dic.keys()}")

print(f"3번 결과: {fruits_dic.values()}")

furits_dic.pop('apple')
print(f"4번 결과(apple 삭제 후): {fruits_dic}")

furits_dic.clear()
print(f"5번 결과(전체 삭제 후): {fruits_dic}")


#6-5
fruits_dic = {'apple': 6000, 'banana': 5000, 'orange': 7000, 'melon': 3000}

print(list(fruits_dic.keys()))

print(list(fruits_dic.values()))

print(f"fruits_dic 딕션너리의 항목의 개수: {len(fruits_dic)}")

if 'apple' in fruits_dic:
    print("apple is in fruits_dic.")
else:
    print("apple is not fruits_dic.")

if 'mango' in fruits_dic:
    print("mango is in fruits_dic.")
else:
    print("mango is not in fruits_dic.")


#6-6
the_day = (1919, 3 ,1)

year, month, day = the_day

print(f"{year}년 {month}월 {day}일은 삼일절입니다.")

my_list = [10, 20, 30]

my_tuple = tuple(my_list[::-1])

a, b, c =my_tuple

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


#6-7
person = ('홍길동', 2019001, 179)

person_list = list(person)

persion_list[1] = 2020003

person = tuple(person_list)

print(f"학번 변동 후 person = {person}")


#6-8
def square(x, y):
    return x**2, y**2

x = 10
y = 20
x_sq, y_sq = square(x, y)

print('{} 제곱 = {}, {} 제곱 = {}'.format(x, x_sq, y, y_sq))


#6-9
lst = ['apple', 'mango', 'banana']

s1 = set(lst)

print(s1)

greet = 'Good afternoon'

s2 = set(greet)

print(s2)


#6-10
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60, 70}

print(f"1) s1,s2 합집합: {s1 | s2}")
print(f"2) s1,s2 교집합 : {s1 & s2}")
print(f"3) s1,s2 차집합 : {s1 - s2}")
print(f"4) s1,s2 대칭 차집합  : {s1 ^ s2}")
print(f"5) s1.s2 부분 집합 여부 : {s1.issubset(s2)}")
print(f"6) s1,s2 상위집합 여부: {s1.issuperset(s2)}")
print(f"7) s1.isdisjoint(s2) : {s1.isdisjoint(s2)}")


#6-11
def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)}
    return res

A = {1, 2}
B = {'A', 'B', 'C'}

print(f"1) A X B = {product_set(A, B)}")

print(f"2) B X A = {product_set(B, A)}")
print(f"3) A X A = {product_set(A, A)}")
print(f"4) B X B = {product_set(B, B)}")


#6-12
def tuple_sum(tup):
    if isinstance(tup, int):
        return tup
    else:
        accum = 0
        for element in tup:
            accum += tuple_sum(element)
        return accum

def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)}
        return res

def exp(input_set, exponent):
    res = input_set
    for _ in range(exponent - 1):
        res = product_set(res, input_set)
    return res

dice = {1, 2, 3, 4, 5, 6}
three_dice = exp(dice, 3)

sum_10_over = [outcome for outcome in three_dice if tuple_sum(outcome) >= 10]
print(f"주사위를 세 번 던져 나온 눈의 합이 10 이상인 경우는 {len(sum_10_over)} 가지입니다.")

def prob_over(x):
    count = len([outcome for outcome in three_dice if tuple_sum(outcome) >= x])
    return (count / len(three_dice))*100

for i in range(3, 19):
    print(f"눈의 합으로 {i:2d} 이상을 얻을 확률 {prob_over(i):6.2f}%")















