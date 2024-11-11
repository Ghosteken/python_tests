def palindrome():
    word = input('what is your word?')
    rev = word[::-1]
    if word == rev:
        print('this is a palindrome word')
    else:
        print('this is not a palindrome word')    
palindrome()        
        