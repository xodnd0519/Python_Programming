# 문자열
# "", ''
a = "python"
print(a, type(a))
b = "python"

# I'll be back
print("I'll be back")
print("I'll be back")

multiline = """

Life is short
You need Python

"""
print(multiline)


def func():
    """이 함수는 테스트 용입니다"""
    print(3)
    pass


print(func.__doc__)
print(func())

print("Hello" + " python")
print("""Hello
""" * 10)


name = "pororo"
age = 23
print(f"이름: {name} 나이: {age}")
print(f"내년 나이: {age + 1}")
print(f"{name.upper()}")

pi = 3.141592
print(f"{pi:.3f}")


num = 123456789
print(f"{num:,}")
print(f"{num:<15d}")
print(f"{num:15d}")
