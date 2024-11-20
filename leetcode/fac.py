# def soln():
#     num = int(input("Enter a number: "))
    
#     def factorial(n):
#         # Base case for recursion
#         if n == 0 or n == 1:
#             return 1
#         else:
#             # Recursive case
#             return n * factorial(n - 1)
    
#     # Call the factorial function and print the result
#     result = factorial(num)
#     print(f"The factorial of {num} is {result}")

def factorial(n):
    # Base case for recursion
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)