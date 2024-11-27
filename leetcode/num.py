# Write a Python Program to Check if a Number is Positive, Negative or Zero.
def check(number):
    if number > 0:
        print('The number is positive')
    elif number < 0:
        print('The number is negative')
    elif number == 0:
        print('This is 0')
    else:
        return None

check(-54)

def armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    armstrong_str = sum(int(digit) ** num_digits for digit in digits)
    return number == armstrong_str              

numb = int(input('Number:'))
if armstrong(numb):
    print(f'{numb} is an Armstrong number')
else:
    print(f'{numb} is not an Armstrong number')
        
#2
def largest_num(number):
    if not number:
        return None
    largest = number[0]
    for num in number:
        if num > largest:
            largest = num
    return largest

numbers = [10, 25, 47, 3, 99, 18]
largest_number = largest_num(numbers)
print('The largest number is:', largest_number)
        