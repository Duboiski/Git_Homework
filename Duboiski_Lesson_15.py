def fib(n):
    f1, f2 = 1,1

    a = []
    a.append(f1)
    a.append(f2)
    for i in range(n):
        f1 ,f2 = f2 ,f1 + f2
        # a.append(f1)
        a.append(f2)
        fib(i)
    return a

print(fib(10))