# cur = 1;
# while cur <= 5:
#     print(cur)
#     cur += 1
#
prompt = f"\n 1을 입력해 아니면 계속 반복된다. \n입력값:";
#
# msg = ''
# while msg != '1':
#     msg = input(prompt)
#     print(msg)
#
# print('잘했어 라이코스!')

isActive = True
while isActive:
    msg = input(prompt)
    if msg == '1':
        isActive = False
        print('잘했어 라이코스!')
        break;
    print(msg)
