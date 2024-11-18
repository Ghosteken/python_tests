
# Find Factorial: Write a function to find the factorial of a number using recursion.
# Write a Python Program to Check Prime Number.

def count():
    word = input('What is your word')
    new_word = 0
    vols = ['a','e','i','o','u']
    for _  in word.lower():
        if _ in vols:
            new_word += 1
    print (new_word)    
        
count()        

def prime():
    number = int(input('Number: '))
    Flag = False
    if number == 1:
        print(f"{number} is not a prime number")
    elif number > 1:
        for i in range(2, number):
            if  number % i == 0:
                 
                Flag = True 
                break
            
    if Flag:
        print(f' {number} is not a prime number')
    else:
        print(f'{number} is a prime number') 