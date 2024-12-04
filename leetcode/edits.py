# n = int(input('what is this: '))
# for i in range(n):
#     print(i)

class Solution:
    def arm_strong(self, number: int) -> int:
        digit = str(number)
        digits = len(digit)
        armstrong = (sum(int(digit) ** digits for digit in digits))
        if armstrong == number: return number
        
    num = input(int('number'))
    if arm_strong(num):
        print('Number is armstrong')
    else: print('Number is not armstrong')    