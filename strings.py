message = 'Hello world'
print(message)
print(len(message))
print(message[2])
print(message[0:5]) #message[:5] is also same when u start from starting index
print(message[6:])

#string methods
print(message.lower())
print(message.count('l'))
print(message.find('l'))
print(message.find('world'))
print(message.find('universe'))

new_message = message.replace('world', 'universe') #replace method returns a value
print(new_message)

#concatinating string
greeting = "Hello"
name = "Nitya"
greet_msg=greeting+' '+name+'. welcome'
print(greet_msg)

#formatted string
greet_message='{} {}. welcome'.format(greeting, name)
print(greet_message)

#f strings
f_string_message= f'{greeting} {name}, welcome'
print(f_string_message)

#dir gives the list of all the methods associated with the variable
print(dir(name))

#help provides the description of the methods associated with the class and arguments they take
#print(help(str)) # need to pass class as a parameter to the help method

print(help(str.lower))
