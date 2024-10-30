def vcount():
    cats = input('Enter your string: ')
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    # Loop through each character in the input string
    for i in cats.lower():  # Use .lower() to make it case-insensitive
        if i in vowels:  # Check if the character is a vowel
            count += 1
    print("Number of vowels:", count)
vcount()
