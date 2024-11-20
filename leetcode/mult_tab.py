#Convert Decimal to Binary: Write a function to convert a decimal number to its binary equivalent.
#Write a Python Program to Display the multiplication Table.

def multiplication_table():
    for i in range(1,10):
        for j in range(1,10):
            print(f"{i} x {j} = {i*j}")
            
            
def decimal_to_binary():
    decimal_num = int(input("Enter a decimal number: "))
    binary_num = bin(decimal_num)[2:]
    print(f"The binary equivalent of {decimal_num} is {binary_num}")
                