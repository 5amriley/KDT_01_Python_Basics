
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in nums:
    print(n, end='_' if n not in (5, 10) else '\n')
print("END")
