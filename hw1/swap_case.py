def swap_case(s):
    swapped = ''
    for char in s:
        if char.islower():
            swapped += char.upper()
        else:
            swapped += char.lower()
    return swapped
s = input()
result = swap_case(s)
print(result)