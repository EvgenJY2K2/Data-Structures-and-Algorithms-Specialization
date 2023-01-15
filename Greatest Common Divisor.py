def GCD(num1, num2):

    rem = num1 % num2

    if rem == 0:
        return num2
    else:
        return GCD(num2, rem)

#Driver code
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(GCD(a, b))
