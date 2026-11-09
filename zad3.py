a, b, c = map(int, input().split())

nums = [a, b, c]
nums.sort()
ans_1 = nums[1]

print(f"Способ 1 (Сортировка): {ans_1}")

ans_2 = a + b + c - min(a, b, c) - max(a, b, c)

print(f"Способ 2 (Математика): {ans_2}")

if (a <= b <= c) or (c <= b <= a):
    ans_3 = b
elif (b <= a <= c) or (c <= a <= b):
    ans_3 = a
else:
    ans_3 = c

print(f"Способ 3 (Условия): {ans_3}")