n, m = map(int, input().split())
array = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
happiness = 0
for num in array:
    if num in set_A:
        happiness += 1
    elif num in set_B:
        happiness -= 1
print(happiness)