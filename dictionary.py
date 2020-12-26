dic1 = {'color': 'green', 'points': 5}
print(dic1)

# copy()는 shallow copy, 아보니 copy 모듈에서 딥카피를 따로 가져다씀
dic2 = dic1.copy()

del dic1['points']
print(dic1)

# key가 존재하지 않는 값을 얻을려 한다면 에러, get() 메서드로 키본값을 반환하는 방법도 있음
print(dic2.get('babo', 'ㅇㅣ 바보야 진짜 아니야'))

# 기본 값을 안준다면?
print(dic2.get('babo')) # None 반환

# 그럼 조건문으로 확인해 보자
if dic2.get('babo') is None:
    print("없다 이눔")
else:
    print("있다요")

# ----------------------------------------------------------------------

# dictionary loop
user = {
    "userName": "jacob",
    "age": 29,
    "hobby": "study"
}

# key, value
for key, value in user.items():
    print(f"{key}, {value}")

# key / keys()를 안써도 사실 dictionary loop의 기본 동작이 키를 순회하는 것이라 괜찮음. 일단 명시적으로 써주는 걸로..!
for k in user.keys():
    print(f"key is {k.title()}")

# value
for v in user.values():
    print(f"value is {v}")

user2 = user.copy();
user2['displayName'] = 'jacob'
print(f"User2 is {user2}")

# set
for v in set(user2.values()):
    print(v)