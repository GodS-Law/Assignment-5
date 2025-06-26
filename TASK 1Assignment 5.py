#This a dictionary containing all the names and marks of the students.
Dict_Students = {'Alice':85, 'Kalu':36, 'Batman':99}

#To get the input from the user
find = str(input('Enter the student\'s name: '))

#Capitalize the inputed name.
cap_find = find.capitalize()

#to check if the student data is in the dictionary or not. if yes then show the result if no then prints the student not foud
if cap_find in Dict_Students:
    print(f'{cap_find}\'s marks: {Dict_Students[cap_find]}')
else:
    print('Student not found.')