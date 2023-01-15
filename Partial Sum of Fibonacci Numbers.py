#Remainder function
def fib(var):

    f0, f1 = 0, 1

    #base case
    if var == 0:
        return 0
    if var == 1:
        return 1

    else:

        rem = var % 60

        if rem == 0:
            return 0

        for i in range(2, rem + 3):
            f = (f0 + f1) % 60
            f0 = f1
            f1 = f

        s = f1 - 1
        return s

        
#Main code
if __name__ == '__main__':

    m, n = map(int, input().split())

    final = fib(n)-fib(m-1)

    print(final % 10)
