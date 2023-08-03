def hello():
    pass #ther is now functionality as of now


# print(hello)
# print(hello())

def greetings():
    print("Hi, Welcome")

greetings()
greetings()

#function with a return statement

def wishing():
    return "Happy Birthday"

wishing()
a= wishing()
print(a)
#or 
print(wishing())

print(wishing().upper())

# prameterized function

def greet(greeting):
    return "%s Function."% greeting

#default parameter
def wish(occassion, name='nithu'):
    return f'Happy {occassion} {name}.'

print(greet("Hello"))
print(wish("anniversery"))
print(wish("Birthday","Punarvi"))

# args and kwargs

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses=['math', 'chemistry']
info={'name': 'Nitya', 'place': 'bangalore'}

student_info('math', 'chemistry',name='Nitya',place="bangalore")
student_info(courses,info)
student_info(*courses,**info)