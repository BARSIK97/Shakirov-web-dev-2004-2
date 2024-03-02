import time

# Рекурсивная функция 
def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n-1)

# Итерационная функция 
def fact_it(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

# Замер времени выполнения рекурсивной функции
start_time_rec = time.time()
print(fact_rec(50))
end_time_rec = time.time()
print("Время решения рекурсивной функцией: ", end_time_rec - start_time_rec)

# Замер времени выполнения итерационной функции
start_time_it = time.time()
print(fact_it(50))
end_time_it = time.time()
print("Время решения итерационной функцией: ", end_time_it - start_time_it)