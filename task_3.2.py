#LAB 5-1
even_list = [2, 4, 6, 8, 10]
print("even_list =", even_list)

even_list = list(range(2, 11, 2))
print("even_list=", even_list)

nations = ['Korea', 'China', 'India', 'Nepal']
print("nations=", nations)

friends = ['길동', '철수', '은지', '유신', '도현']
print("friends=", frineds)

string = list('XYZ')
print("string=", string)


#LAB 5-2
prime_list = [2, 3, 5, 7]
print('prime_list의 첫 원소:', prime_list[0])

print('prime_list의 마지막 원소:', prime_list[3])

print('prime_list의 마지막 원소:', prime_list[-1])

nations = ['korea', 'China', 'Russia', 'Malaysia']
print('nations의 첫 원소:', nations[0])

print('nations의 마지막 원소:', nations[-1])

print('nations의 마지막 원소:', nations[len(nations)-1])


#LAB 5-3
print_list = [2, 3, 5, 7]
print('소수 목록:', print_list)

prime_list.append(11)
print('추가 후 소수 목록:', prime_list)

print('삭제 전 소수 목록:', prime_list)

print('삭제 후 소수 목록:', prime_list)

nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('국가 목록:', nations)

nations.append('Nepal')
print('추가 후 국가 목록:', nations)

if 'Japen' in nations:
    print('Japen 는(은) 국가 목록에 있습니다.')
else:
    print('Japen 는(은) 국가 목록에 없습니다.')

if 'Russia' in nations:
    print('Russia 는(은) 국가 목록에 있습니다.')
else:
    print('Runssia 는(은) 국가 목록에 없습니다.')


#LAB 5-4
print_list = [2, 3, 5, 7]
print('1에서 10까지의 소수:', prime_list)

print('최솟값:', min(print_list))
print('최댓값:', max(prime_list))
print('합계:', sum(prime_list))

print('평균:', sum(prime_list) / len(prime_list))

#LAB 5-5
a = [1, 2, 3]
b = [10, 20, 30]
a.append(b)
print(a) 

a = [1, 2, 3]
b = [10, 20, 30]
a.extend(b)
print(a)

nlist = list(range(1, 11))
print('nlist=', nlist)

nlist.insert(0, 0)
print('nlist=', nlist)

last_element = nlist.pop()
print('마지막 원소=', last_element)
print('nlist=', nlist)


#LAB 5-6
n = int(input('반복할 정수를 입력하시오:'))

base_list = [1, 2, 3]

print(base_list*n)



#LAB 5-7
n_list = list(range(15))
print('n_list=', n_list)

s_list1 = n_list[:5]
print('s_list1=', s_list1)

s_list2 = n_list[5:11]
print('s_list2 =', s_list2)

s_list3 = n_lsit[11:]
print('s_list3=', s_list3)

s_list4 = n_list[2:11:2]
print('s_list4=', s_list4)

s_list5 = n_list[10:5:-1]
print('s_list5=', s_list5)

s_list6 = n_list[10:1:-2]
print('s_list6=', s_list6)






