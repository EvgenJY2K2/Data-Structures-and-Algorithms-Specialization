#KEY:The last digit is always the sum of the last digits of the previous two numbers. 
Fibl = (0, 1)
def fibonacci_last_digit(n):
    if n in Fibl:
        return n

    previous, current = Fibl

    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
