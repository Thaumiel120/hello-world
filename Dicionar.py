student={'name':'Victor', 'age':25, 'courses':['Math','Quantum']}
# key error print(student['phone'])
student['phone']='8127571534'
student['name']='Paola'
print(student.get('phone','Not found'))
print(student)


student.update({'name':'ana','age':26,'phone':555555})
print(student)

del student['age']
print(student)

number=student.pop('phone')
print(student)
print(number)

student2={'name':'Nakoru', 'age':22, 'courses':['Math','Quantum']}
print(len(student2))
print(student2.keys())
print(student2.values())
print(student2.items())

for key, value in student2.items():
    print(key,value)

