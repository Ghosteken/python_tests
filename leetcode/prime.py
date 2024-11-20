
def prime():
    prime_numbers = []
    for num in range(1, 10):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    print(prime_numbers)

prime()



# def add(a, b):
#    print (a + b)

# add(1,2)

    