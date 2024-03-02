import sys

def my_sum_argv(*args):
    return sum(args)

numbers = [float(num) for num in sys.argv[1:]]

result = my_sum_argv(*numbers)
print(result)