def sum_and_sub(a, b):
    sum_result = a + b
    sub_result = a - b
    return sum_result, sub_result

a = int(input())
b = int(input())
result_sum, result_sub = sum_and_sub(a, b)
print(f"Сумма: {result_sum}, Разность: {result_sub}")