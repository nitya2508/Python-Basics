# tuples are immutable

courses = ("History", "Physics", "Maths", "chemestry")

print(courses)  

print(len(courses))

print(courses.index('History'))

for index,item in enumerate(courses):
    print(index, item)