st1 = "He likes apples, she likes too"
print(st1)
print('-' * 20)

# 문자열에서 특정 문자열의 개수 구하기
print(st1.count('like'))
print('-' * 20)
# 문자열의 왼쪽에서 오른쪽으로 검색 : find
print(st1.find('like'))
print(st1.find('like', st1.find('like')+1))
print(st1.find('love'))
print('-' * 20)
# 문자열의 오른쪽에서 왼쪽으로 검색
print(st1.rfind('like'))
print(st1.rfind('love'))
print('-' * 20)
# 문자열의 왼쪽에서 오른쪽으로 검색 : index
# => 없는 단어는 에러발생
print(st1.index('like'))
print(st1.index('like', st1.index('like')+1))
try :
    print(st1.index('love'))  # 에러
except :
    print("단어가 없습니다.")
print('-' * 20)
# 문자열의 오른쪽에서 왼쪽으로 검색
print(st1.rindex('like'))
print('-' * 20)
# 시작되는 단어인지 검사
print(st1.startswith('likes'))
print(st1.startswith('likes', 3))
print('-' * 20)
# 끝나는 단어인지 검사
print(st1.endswith('likes'))
print(st1.endswith('likes', 0, 26))
print('-' * 20)
# 포함되어 있는지 검사 : in
print('like' in st1)
print('love' in st1)
print('-' * 20)
# 포함되어 있지 않은지 검사 : not in
print('like' not in st1)
print('love' not in st1)
print('-' * 20)
