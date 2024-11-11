
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

def soln():
    num = int(input("Enter a number: "))
    def factorial( num ):
        for i in range(num):
            if num > 0:
                return num * factorial(num - i)