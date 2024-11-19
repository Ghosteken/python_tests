def fib(n):
    fib_sec = []
    a , b = 0,1
    if n == 0:
        print('no seq found')
        exit()
    else:
        for _ in range(n):
            fib_sec.append(a)
            a,b = b,a+b
        print(fib_sec)
        
fib(5)        