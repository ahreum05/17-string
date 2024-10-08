st1 = "     He likes apples, she likes too     "
print(st1)
print('-' * 20)

# 좌우 공백문자 제거
st2 = st1.strip()
print('ttt' + st2 + 'ttt')
print('-' * 20)
# 오른쪽 공백문자 제거
st2 = st1.rstrip()
print('ttt' + st2 + 'ttt')
print('-' * 20)
# 왼쪽 공백문자 제거
st2 = st1.lstrip()
print('ttt' + st2 + 'ttt')
print('-' * 20)
# 문자열 바꾸기
st2 = st1.replace("like", 'love')
print(st2)
print('-' * 20)

st2 = st1.replace(" ", '')
print(st2)
print('-' * 20)




