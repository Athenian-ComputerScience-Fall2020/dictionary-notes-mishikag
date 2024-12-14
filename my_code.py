# Use this to take notes on the Edpuzzle video. Try each example rather than just watching it - you will get much more out of it!
#  key: unique identifier where we can find the data
#  value: the data

student = {'name':'john', 'age': 25, 'courses':['math','CompSci']}

#add it to student
#student['phone'] = '555-5555'
#student['name'] = 'jane'

#student.update ({'name': 'jane', 'age': 26, 'phone': '555-5555'})

#print(student.get('name'))
#print(student.get('phone', 'Not Found'))

#print(student.get('phone'))
# key error^^

#delete at specific value

#del student['age']

#2nd way
#age = student.pop ('age')
#print(student)
#print(age)


#how many keys?
print(len(student))
#want to see the keys
print(student.keys())
#want to see the values
print(student.values())
#want to see keys and values
print(student.items())

#want to loop through all keys
for key in student:
    print(key)

#want to loop through all keys and values
for key, value in student.items():
    print(key, value)




