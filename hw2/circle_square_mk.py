import random
import math

def circle_square_mk(r, n):
    count_inside = 0
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if math.sqrt(x**2 + y**2) <= r:
            count_inside += 1
    square_estimation = (2 * r)**2 * (count_inside / n)
    return square_estimation

if __name__ == '__main__':
    r = int(input())
    n = int(input())
    estimated_square = circle_square_mk(r, n)
    actual_square = math.pi * r**2

    print("Оценка: ", estimated_square)
    print("Площадь: ", actual_square)
    print("Погрешность: ", abs(actual_square - estimated_square))

# Чем больше эксперементов, тем меньше погрешность 