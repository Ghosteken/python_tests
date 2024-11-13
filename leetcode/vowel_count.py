def vcount():
    cats = input('Enter your string: ')
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in cats.lower():  
        if i in vowels:  
            count += 1
    print("Number of vowels:", count)
vcount()
