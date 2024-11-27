# Find the Largest Element in a List: Write a program that finds the largest number in a list.

def find_largest(numbers):
    if not numbers:  # Check if the list is empty
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [10, 25, 47, 3, 99, 18]
largest_number = find_largest(numbers)
print("The largest number is:", largest_number)
