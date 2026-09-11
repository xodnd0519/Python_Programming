# for i in iterable객체

for i in range(2, 5):
    print(i, end=" ")
print()
print()

a = range(5)
print(a.start, a.step, a.stop)
print()


for i in range(1, 10, 2):
    print(i, end=" ")
print()
print()
for i in range(5, 0, -1):
    print(i, end=" ")

print()

tot = 0
for i in range(1, 11):
    tot += i

print(f"sum = {tot}")

# 구구단 출력
# 2 * 1 = 2 2 * 2 = 4 .. 2 * 9 = 18
# 9 * 1 = 9 9 * 2 = 18 .. 9 * 9 = 81

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j:<5d}", end=" ")
    print()
