#9 - 1
 # a)100 b)20000 c)2.0_trudiv는 소수점 까지 계산합니다.
 # a) 40 (pop()은 리스트의 마지막 요소를 꺼내고 그 값을 반환합니다.)
 # 2) keys(), 5) get()

print(dir(int))
print(dir(list))


#9 - 2
# 1. 용어 정의
# a) 객체 지향 프로그래밍 (Object-Oriented Programming, OOP) 데이터(속성)와 그 데이터를 처리하는 함수(메소드)를 하나의 '객체'라는 단위로 묶어서 프로그램을 구성하는 방식입니다. 현실 세계의 사물을 모델링하여 코드를 짜기 때문에 재사용성과 유지보수가 뛰어납니다.

# b) 절차적 프로그래밍 (Procedural Programming) 프로그램을 위에서 아래로 순차적인 '절차'나 명령의 흐름으로 파악하는 방식입니다. 실행 순서가 중요하며, 데이터와 함수가 분리되어 있어 프로그램 규모가 커지면 관리가 복잡해질 수 있습니다.

# c) 그래픽 사용자 인터페이스 (Graphical User Interface, GUI) 사용자가 컴퓨터와 상호작용할 때, 텍스트 명령어가 아닌 아이콘, 버튼, 메뉴 등 그래픽 요소를 사용하는 환경을 말합니다. (예: 윈도우 바탕화면, 스마트폰 앱 화면 등)

# 2. 객체 지향 프로그래밍 기법과 절차적 프로그래밍 기법의 차이점: 절차적 프로그래밍이 "요리 레시피(순서)"라면, 객체 지향 프로그래밍은 "요리사, 재료, 도구(역할 중심)"들의 협력


#9 - 3
# a) 클래스 (Class): 객체를 만들기 위한 '설계도' 혹은 '틀'입니다. b) 객체 (Object): 클래스라는 설계도를 바탕으로 실제로 구현된 '모든 대상'을 의미합니다. c) 인스턴스 (Instance): 특정 클래스로부터 만들어진 '구체적인 실체'를 강조할 때 쓰는 표현입니다. d) 클래스의 속성 (Attribute / Property): 객체가 가지고 있는 '상태'나 '데이터'를 의미합니다. 클래스 내부에 변수로 선언됩니다. e) 클래스의 동작 (Method): 객체가 수행할 수 있는 '기능'이나 '행위'를 의미합니다. 클래스 내부에 함수로 정의됩니다.



#9 - 4
class Dog :
    def bark(self) :
        print("멍멍~~")

## 메인 코드 부분 ##
# Dog 클래스의 인스턴스를 생성하고 my_dog 변수로 참조합니다.
my_dog = Dog()

# 생성된 인스턴스의 bark() 메소드를 호출합니다.
my_dog.bark()




#9 - 5
## 클래스 선언 부분 ##
class Dog :
    def __init__(self, name) :
        self.name = name
    
    def bark(self) :
        print("멍멍~~")

my_dog = Dog('Jindo')

my_dog.bark()



#9 - 6
class Dog :
    def __init__(self, name) :
        self.name = name
    
    def __str__(self) :
        return "Dog(name = " + self.name + ")"

my_dog = Dog('Jindo')
print('my_dog의 정보 :', my_dog)


#9 - 7
n = 100
m = 100

if n is m :
    print('n is m')
else :
    print('n is not m')


#9 - 8
class Vector :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def __mul__(self, other) :
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other) :
        return Vector(self.x / other.x, self.y / other.y)

    def __neg__(self) :
        return Vector(-self.x, -self.y)

    def __str__(self) :
        return "({}, {})".format(self.x, self.y)

v1 = Vector(30, 40)
v2 = Vector(10, 20)

print("v1 * v2 =", v1 * v2)
print("v1 / v2 =", v1 / v2)
print("-v1 =", -v1)


#9 - 9
import math

class Vector :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def magnitude(self) :
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, other) : return self.magnitude() > other.magnitude()
    def __ge__(self, other) : return self.magnitude() >= other.magnitude()
    def __lt__(self, other) : return self.magnitude() < other.magnitude()
    def __le__(self, other) : return self.magnitude() <= other.magnitude()

v1 = Vector(30, 40)
v2 = Vector(10, 20)

print("v1 > v2 =", v1 > v2)
print("v1 >= v2 =", v1 >= v2)
print("v1 < v2 =", v1 < v2)
print("v1 <= v2 =", v1 <= v2)


#9 - 10
class Rect :
    def __init__(self, width, height) :
        self.width = width
        self.height = height

r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['width'])

class RectPrivate :
    def __init__(self, width, height) :
        self.__width = width
        self.__height = height

r2 = RectPrivate(100, 200)
print(r2.__dict__)
print(r2.__dict__['_RectPrivate__width'])
