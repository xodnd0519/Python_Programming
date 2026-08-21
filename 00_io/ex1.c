
a = input()
print(a)
print(type(a))

a = input()
a = int(a)
print(a, type(a))

a = int(input())
print(a + 1, type(a))

a = float(input())
print(a, type(a))

a = int(input())
b = int(input())
print(a)
print(b)

a = input().split()
print(a, type(a))

# map 함수, 리스트

a, b, c = map(int, input().split())
print(a, b, c)

a = list(map(int, input().split()))
print(a, type(a))
