st1 = "1234"
st2 = "HelloPython"
st3 = "Hello Python"
st4 = "홍길동"
st5 = "1234abcd"

# 문자열이 숫자만으로 구성되었는지 검사
print(st1, st1.isdigit())
print(st2, st2.isdigit())
print('-' * 20)
# 문자열이 알파벳(문자)만으로 구성되었는지 검사
print(st1, st1.isalpha())
print(st2, st2.isalpha())
print(st3, st3.isalpha())
print(st4, st4.isalpha())
print('-' * 20)
# 문자열이 숫자나 알파벳으로 구성되었는지 검사
print(st1, st1.isalnum())
print(st2, st2.isalnum())
print(st3, st3.isalnum())
print(st4, st4.isalnum())
print(st5, st5.isalnum())
print('-' * 20)
# 문자열이 소문자인지 검사
print(st1, st1.islower())
print(st2.lower(), st2.lower().islower())
print(st3, st3.islower())
print(st4, st4.islower())
print(st5, st5.islower())
print('-' * 20)
# 문자열이 대문자인지 검사
print(st1, st1.isupper())
print(st2.upper(), st2.upper().isupper())
print(st3, st3.isupper())
print(st4, st4.isupper())
print(st5, st5.isupper())
print('-' * 20)
# 문자열이 공백문자인지 검사
st6 = '     '
print(st4, st4.isspace())
print(st6, st6.isspace())
print('-' * 20)
# 단어의 첫글자가 대문자인지 검사
print(st1, st1.istitle())
print(st2, st2.istitle())
print(st3, st3.istitle())
print(st4, st4.istitle())
print(st5, st5.istitle())
print('-' * 20)
# 한글로만 구성되어있는 지 검사 : 정규표현식 사용
import re
p = re.compile('[ㄱ-ㅎㅏ-ㅣ가-힣]')

if p.match('python') : print('한글입니다.')
else : print('한글이 아닙니다.')
print('-' * 20)

if p.match(st4) : print('한글입니다.')
else : print('한글이 아닙니다.')
print('-' * 20)







