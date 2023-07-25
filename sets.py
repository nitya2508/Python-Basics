# sets are ordered and doesn't have duplicates

courses = {"History", "Physics", "Maths", "chemestry"}
art_courses = {"History", "Physics", "art", "design"}
print(courses)

print('Maths' in courses)

print(courses.intersection(art_courses))

print(courses.difference(art_courses))

print(art_courses.difference(courses))

print(courses.union(art_courses))


#empty lists
empty_list=[]
empty_list=list()

#empty tuple
empty_tuple=()
empty_tuple=tuple()

#empty sets
empty_set={} #This is not a set, It is a dictionary
empty_set=set()