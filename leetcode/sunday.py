# Count Vowels in a String: Create a program that counts the number of vowels in a string.
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