def vcount():
    cats = input('Enter your string: ')
    vowels = ['a', 'e', 'i', 'o', 'u']
    found_vowels = ''
    for i in cats.lower():  # Use .lower() for case-insensitivity
        if i in vowels:  # Check if the character is a vowel
            found_vowels += i  # Add the vowel to the found_vowels string
    print("Number of vowels:", len(found_vowels))

vcount()
