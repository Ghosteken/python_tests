def string_rev():
    word = input('Enter your string: ')
    reversed_word = word[::-1]  
    print(reversed_word)

string_rev()


def string_rev():
    word = input('Enter your string: ')
    reversed_word = ''
    
    # Loop from the last index to the first index
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]  # Add each character to the result string
    
    print(reversed_word)

string_rev()

