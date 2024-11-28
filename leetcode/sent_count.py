def sent_count(c):
    arr = c.split(' ')
    return len(arr)

print(sent_count('This is a test sentence.'))  

# Write a Python Program to Find Armstrong Number in an Interval.
def armstr_number():
    lower = 100
    upper = 1000
    for num in range(lower, upper):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if sum == num:
            print(num)    
             
            
            
  
armstr_number()            

# Explanation:
# Define the range: The lower and upper variables define the range to check for Armstrong numbers (100 to 1000 in this case).
# Loop through the range: Use a for loop to iterate through each number in the range.
# Count the digits: Use len(str(num)) to determine the number of digits in the current number.
# Calculate the Armstrong sum:
# Extract the last digit of the number using temp % 10.
# Raise it to the power of the number of digits and add it to sum.
# Remove the last digit using temp //= 10.
# Check Armstrong condition: Compare sum with the original number (num). If they match, print the number.