# list is a collection of data

courses = ["History", "Physics", "Maths", "chemestry"]

print(courses)
print(len(courses))

print(courses[0])

#negative indexing
print(courses[-1])

# range
print(courses[0:])
print(courses[0:2])
print(courses[:3])

# adding to list
courses.append('art')
print(courses)
# insert to specific location
courses.insert(2, 'science')
print(courses)

# insert and append add the new list to the existing list

courses_2 = ["Biology", "Geograpy"]
# courses.insert(0,courses_2)
# print(courses)
# courses.insert(3,courses_2)
# print(courses)

# extent to add multiple values to the list
courses.extend(courses_2)
print(courses)

#remove

courses.remove('Physics')
print(courses)

# pop to rmove the last value
courses.pop()
print(courses)

# pop returns a popped value

popped =courses.pop()
print(popped)

# reverse a list
courses.reverse()
print(courses)

# sort a list - default ascending order

nums = [2,3,1,8,4,5]

courses.sort()
print("sorted :",courses)
nums.sort()
print(nums)

# sort in descending order
courses.sort(reverse=True)
print("sorted :",courses)
nums.sort(reverse=True)
print(nums)

# sort alters the existing list instead use SORTED not to alter the original list

sorted_list = sorted(courses)
print(sorted_list)

# min
print(min(nums))
#max
print(max(nums))
#sum
print(sum(nums))

#index
print(courses.index('art'))


# check if a value is in list

print('art' in courses)
print('Biology' in courses)

# loop through using for loop

for item in courses:
    print(item)

#enumerate gives the index and the items

for index, cours in enumerate(courses):
    print(index, cours)

# if you dont want index value to start from 0 then specify the start index
for index, cours in enumerate(courses, start=1):
    print(index, cours)

#convert a list to string and strin to list

courses_str = ', '.join(courses)
print(courses_str)
new_list = courses_str.split(', ')
print(new_list)