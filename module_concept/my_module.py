print("Importing my_module")

def get_index(to_search, target):
    '''returns the index of the given value from the list'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return -1
