employee= {'name':'Nitya','employee_id':10, 'email':'nitya@gmail.com','skills':['python','Angular']}

print(employee)
print(employee['skills'])

# keys can be steings, numbers.
# if u try to access a key that doesn't exist the it throws "key error"
# instead use get method to access

print(employee.get('name'))
# can set default values to the non existing keys
print(employee.get('phone',"doesnot exists"))

#add a new key value pair to the dict
employee['phone']='9876543210'
print(employee.get('phone',"doesnot exists"))

#update dict
employee['name']="Nithan"
print(employee.get('name'))

# to perform multiple changes like add and update the dict in 1 go then use update method which accepts a dict as argument

employee.update({"name":'nn','skills':['Python','Angular','JS'],'address':'Bangalore'})

print(employee)

# to delete a pair from dict

del employee['phone']
print(employee)

# to delete a pair and return the deleted value use pop

address = employee.pop('address')

print(employee)
print(address)

#print the length of dict

print(len(employee))

# print only keys, only values or the pair
print(employee.keys())
print(employee.values())
print(employee.items())

# loop through dict

for key in employee:
    print(key) # prints only keys

# for key, value in employee:
#     print(key,value) #gives error

for k, v in employee.items():
    print(k,v) # prints key value pairs