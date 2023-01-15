def Pisano_Period(m):
    previous, current = 0, 1

    for i in range(0, m * m):
        previous, current \
        = current, (previous + current) % m
        
        if (previous == 0 and current == 1):
            return i + 1

def Fibonacci_Modulo(n, m):
    pisano_period = Pisano_Period(m)
    n = n % pisano_period
     
    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current \
        = current, previous + current
         
    return (current % m)

def main():
    #take the number of value to compute and the modulo
    nth_value, modulo = map(int, input().split())

    #print the modulo for the given inputs
    print(Fibonacci_Modulo(nth_value, modulo))

main()
