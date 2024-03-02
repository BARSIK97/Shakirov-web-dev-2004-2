def my_sum(*args):
    return sum(args)

user_input = input("Введите числа через пробел: ")
numbers = [float(num) for num in user_input.split()]

result = my_sum(*numbers)
print(result)