# 반복문: while문, for문

i = 1
while i < 11:
    print(i, end=" ")
    i += 1
    if i == 6:
        break
else:
    print("END")

print()
nums = [1, 3, 5, 7, 9]

target = 2
i = 0
while i < len(nums):
    if nums[i] == target:
        print(f"{target} found")
        break
    i += 1
else:
    print(f"{target} notfound")

i = 1
tot = 0
while i <= 10:
    tot += i
    i += 1
else:
    print(tot)
