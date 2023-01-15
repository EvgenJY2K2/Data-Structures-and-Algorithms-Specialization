FibArray = [0, 1]
def fibonacci(n):

    if n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci(input_n))
