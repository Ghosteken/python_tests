
# names = []
# for _ in range(3):
#     name = input(print("what is your name ?"))
#     names.append(name)
    
# for name in sorted(names):
#     print (f'your name is {name}')    


# check box,find what it is doing???
names = []
with open('names.txt') as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f'hello,{names}')        

