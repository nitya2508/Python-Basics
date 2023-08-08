import my_module #importing the module
# import my_module as mm # changing the name of the module
# from my_module import get_index #import function directly
# from my_module import get_index as gi
# from my_module import *
import sys

courses= ['Math','Physics','Chemistry','Biology']

index = my_module.get_index(courses, 'Chemistry')
print(index)

print(sys.path)