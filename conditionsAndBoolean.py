language = 'Python'

if language=='Java':
    print("Language is Java")
elif language == 'Python':
    print("Language is Python")
else:
    print("No match")

#and, or, not

user = 'admin'
logged_in =False

if user == 'admin' and logged_in:
    print('Admin Page')
else:
    print('Bad creds')

if user == 'admin' or logged_in:
    print('Admin Page')
else:
    print('Bad creds')

if not logged_in:
    print('plz log in')
else:
    print('logged in')

# difference betwee == and is

a = [1,2,3]
b = [1,2,3]

print(a == b) # compares the values
print(a is b) # ans is false as these are 2 diff objects in memory - it compares id

print(id(a))
print(id(b))

# let us make the id same

c=a

print(a is c) #same object in memory

# what all conditions python eveluates to false

# condition = False
# condition = None
#condition = 10 #evaluated to true
# condition = 0 #evaluated to false
# empty sequences like '', (), [] are evaluated to false
# empty mapping that is dictionary ={} evaluates to false
condition=''

if condition:
    print('condition is true')
else:
    print('condition is false')

    


