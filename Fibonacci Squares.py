def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    n = n % 60
    f0, f1 = 0, 1 

    for i in range(2, n + 2):
        f0, f1 = f1, (f0 + f1)
    return (f0 * f1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
