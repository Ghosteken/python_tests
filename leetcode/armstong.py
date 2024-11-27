def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)  
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)  # Calculate the Armstrong sum
    return armstrong_sum == number  # Check if the sum equals the original number

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")







# def is_armstrong(number):
#     return number == sum(int(digit) ** len(str(number)) for digit in str(number))

# num = int(input("Enter a number: "))
# print(f"{num} is an Armstrong number." if is_armstrong(num) else f"{num} is not an Armstrong number.")
