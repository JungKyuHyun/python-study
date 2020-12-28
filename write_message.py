"""
'w' 쓰기 모드
'r' 읽기 모드
'a' 이어 붙이기 모드
'r+' 읽고 쓰기 모드
"""
filename = 'text_files/write_test.txt'

with open(filename, 'w', encoding='utf-8') as file_object:
    try:
        file_object.write("Jacob JJang\n")
        file_object.write("한글도 쓸려면 또?\n")
    except FileExistsError:
        print('w 모드에서는 나올리가 없을테지만..')
    else:
        print('파일 쓰기 성공')
