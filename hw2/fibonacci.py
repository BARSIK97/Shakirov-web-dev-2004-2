cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n): 
    # return a list of fibonacci numbers
    fib = [0, 1]
    while len(fib) < n:
        next = fib[-1] + fib[-2]
        fib.append(next)
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
