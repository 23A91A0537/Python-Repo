def nearest_fibonacci(n):
    if n == 0:
        print(0)
        return


    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])


    lower = fib[-2]
    upper = fib[-1]


    if abs(lower - n) < abs(upper - n):
        print(lower)
    elif abs(lower - n) > abs(upper - n):
        print(upper)
    else:
        print(lower, upper)



n = int(input())
nearest_fibonacci(n)
