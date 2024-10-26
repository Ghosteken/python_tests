# import csv

# students  = []

# with open('file.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({'name':row[0],'house':row[1]})
        

# for student in sorted(students, key= lambda student : student['name']):
#     print (f'{student['name']} is in {student['house']}')
    
    
# import csv 

# name = input(print("what is your name ? "))
# house = input(print("where do you live ? "))

# with open('file.csv', '+a') as file:
#     reader = csv.writer(file)
#     reader.writerow([name,house])
# print(reader)                


import csv 

name = input(print("what is your name ? "))
house = input(print("where do you live ? "))

with open('file.csv', '+a') as file:
    reader = csv.DictWriter(file,fieldnames=['name','home'])
    reader.writerow({'name': name,'house':house})
     