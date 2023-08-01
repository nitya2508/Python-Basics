num= [1,2,3,4,5]

# break and continue statements

for i in num:
    if i == 3:
        print("found")
        break
    print(i)

for i in num:
    if i == 3:
        continue
    print(i)

# nested for loop

# for i in num:
#     for char in 'abc':
#         print (i, char)

# range method

# for i in range(10):
#     print(i)

# specify the start in range

for i in range(2,10):
    print(i)

# while loop
n = 50
while n<60:
    if n == 55:
        break
    print(f'inside while {n}')
    n+=1


x = 10

while x in range(8,20):
    print("in range")
    x+=1
