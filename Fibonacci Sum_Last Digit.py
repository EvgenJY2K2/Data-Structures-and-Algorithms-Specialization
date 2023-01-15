def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for i in range((n + 2) % 60):
        previous, current = current, (previous + current) % 10

    return 9 if previous == 0 else previous - 1


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
