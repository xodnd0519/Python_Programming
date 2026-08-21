# 변수
a = 2
b = 3
print(a, end="")
print(b)
print(a, b, sep=",")
a = 2
b = 3

a = 2, b
print(a)

a, b = 2, 3
temp = a
a = b
b = temp
print(a, b, sep="+")
a, b = b, a
print(a, b, sep="+")

# 변수명 규칙 - C와 동일
# 문자, 숫자, 언더바만 가능
# 대소문자 구분
# 예약어 사용 불가
name2 = "pororo"
name_ = "crong"

이름 = "뽀로로"
print(이름)


student_name = "태웅"
