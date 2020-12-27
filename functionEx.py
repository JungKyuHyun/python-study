def greet():
    print("안녕")


greet()


# 위치형 매개변수(순서 중요)
def greet1(name, age):
    print(f"이름은 {name.title()}, 나이는 {age}살이구나 안녕!")


greet1('jacob', 29)

# 키워드 매개변수(순서 중요하지 않음)
greet1(age=29, name='jacob')


# 기본값


def greet2(name='jacob', age=29):
    print(f"이름은 {name.title()}, 나이는 {age}살이구나 안녕!")


greet2()
greet2('kyu', 30)


# 딕셔너리 반환

def build_person(f_name, l_name):
    """사람에 관한 정보 디셔너리 반환"""
    person = {'first': f_name, 'last': l_name}
    return person


developer = build_person('Jung', 'Kyu')
print(developer)

a = [1, 2, 3, 4, 5]

def print_a(list):
    new_a = list[:] # 추가 책에서는 리스트 복사를 권하지 않음.
    # 리스트를 복사하는 시간과 메모리가 많이 소모된다고 됨. 리스트가 클수록 체감 된다는? 음?
    b = []
    while new_a:
        cur = new_a.pop()
        print(f"print {cur}")
        b.append(cur)


print_a(a)
# print(a) # [] wow..


# 매개변수를 임의의 숫자만큼 전달

def make_list(*argument):
    print(argument)

make_list(1,2,3,4,5,6,78,'ekek')

# 보편적으로 args 라고 씀
def make_tuple(a, *args):
    print(f"a={a}, {args}")

make_tuple('jacob', 1,2,3,4,5,6,7,9)


# 임의의 키워드 매개변수 사용(일반적으로 kwargs라고 씀)

def build_profile(first, last, **kwargs):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만들기"""
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs

profile = build_profile('jung', 'kyuhyun', age = 29)
print(profile)