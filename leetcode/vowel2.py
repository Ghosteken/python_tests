def vcount():
    cats = input('Enter your string: ')
    vowels = ['a', 'e', 'i', 'o', 'u']
    found_vowels = ''
    for i in cats.lower():
        if i in vowels:  
            found_vowels += i  
    print("Number of vowels:", len(found_vowels))

vcount()
