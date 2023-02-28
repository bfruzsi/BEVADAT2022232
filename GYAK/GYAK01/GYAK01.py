#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list


def contains_odd(input_list):
    for item in input_list:
        if item % 2 == 1:
            return True
        return False

input_list = [2, 4, 3, 8, 2, 2]
contains_odd(input_list)


#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list


bool_list = []
def is_odd(input_list):
    for item in input_list:
        if item % 2 == 1:
            bool_list.append('True')
        else:
            bool_list.append('False')
    return bool_list   

input_list = [2, 1, 3, 6, 7, 12]   
is_odd(input_list)


#Create a function that accpects 2 lists of integers and returns their element wise sum. 
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2


sum_list = []
def element_wise_sum(input_list_1, input_list_2):
    return [x + y for x, y in zip(input_list_1, input_list_2)]

input_list_1 = [1, 2, 3, 4]
input_list_2 = [2, 4, 5, 6]

element_wise_sum(input_list_1, input_list_2)


#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict


def dict_to_list(input_dict):

    list = []
    for x,y in zip(input_dict.keys(), input_dict.values()):
        list.append((x,y))
    return list
    
input_dict = {"hello": "bello", "szevasz": "tavasz"}
dict_to_list(input_dict)

# %%



