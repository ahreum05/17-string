st1 = "He likes apples, she likes too"
print(st1)
print('-' * 20)

# 문자열 분리
# => 문자를 설정하지 않으면, 공백문자 기준으로 분리
st2 = st1.split() # 리스트
print(st2)
print('-' * 20)

st2 = st1.split(' ', 2) # 리스트
print(st2)
print('-' * 20)

st2 = st1.split(',') # 리스트
print(st2)
print('-' * 20)
# 오른쪽부터 분리
st2 = st1.rsplit() # 리스트
print(st2)
print('-' * 20)

st2 = st1.rsplit(' ', 2) # 공백으로 2개만 분리
print(st2)
print('-' * 20)

# 라인으로 분리
st3 = '''\
첫번째줄
두번째줄
세번째줄'''
st2 = st3.splitlines() # 리스트
print(st2)
print('-' * 20)

# 리스트의 문자열들을 특정문자로 결합
st4 = ['첫번째줄', '두번째줄', '세번째줄']
st2 = ":".join(st4)
print(st2)
print('-' * 20)


