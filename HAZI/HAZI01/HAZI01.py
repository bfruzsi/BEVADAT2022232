#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index


def subset(input_list,start_index,end_index):
    return input_list[start_index:end_index]

input_list = [1, 2, 3, 4, 7, 8, 12, 3, 5]
subset(input_list, 2, 6)

#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size


def every_nth(input_list,step_size):
    return input_list[0::step_size]

input_list = [1,2,3,4,5,6,7,8,9,10]
every_nth(input_list, 2)

#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list


def unique(input_list):
    my_set = set()
    for item in input_list:
        my_set.add(item)
    if my_set:
        return True
    else:
        return False

input_list = [1,2,2,7,8,9,8,10]
unique(input_list)

#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list


def flatten(input_list):
    flattened_list = [num for sublist in input_list for num in sublist]
    return flattened_list

input_list = [[1,2],[2,7,8],[9,8,10]]
flatten(input_list)

#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


def merge_lists(*args):
    new_list = []
    for item in args:
        new_list += item

    return new_list

input_list = [1,2,3,4]
input_list2 = [5,6,7]

merge_lists(input_list, input_list2)

#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list


def reverse_tuples(input_list):
    return [item[::-1] for item in input_list]

input_list = [(1,2), (3,5,6)]
reverse_tuples(input_list)


#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list


def remove_duplicates(input_list):
    another_set = set()
    for item in input_list:
        another_set.add(item)
    return list(another_set)

input_list = [5,6,7,7,8]
remove_duplicates(input_list)

#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list


def transpose(input_list):
    return [[x[i] for x in input_list] for i in range(len(input_list[0]))]

input_list = [(1, 2, 4), (3, 5, 6)]
transpose(input_list)


#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size


def split_into_chunks(input_list, chunk_size):
    split_lists = [input_list[x:x+chunk_size] for x in range(0, len(input_list), chunk_size)]

    return split_lists


input_list = [[1,2,3],[2,7,8],[9,8,10]]
split_into_chunks(input_list, 4)

#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict  


def merge_dicts(*dict):
    new_dict = {}
    for item in dict:
        new_dict.update(item)
    return new_dict


dict1 = {1: 2, 2:3}
dict2 = {3: 4, 4:5}
merge_dicts(dict1, dict2)


#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list


dict1 = {'even': [], 'odd': []}


def by_parity(input_list):
    for item in input_list:
        if item % 2 == 0:
            dict1['even'].append(item)
        else:
            dict1['odd'].append(item)

    return dict1


input_list = [5,6,7,7,8]
by_parity(input_list)

#Create a function that receives a dictionary like this: ,....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict


def mean_key_value(input_dict):
    for key, value in input_dict.items():
        input_dict[key] = sum(value) / len(value)
        
    return input_dict


input_dict = {"some_key":[1,2,3,4],"another_key":[1,4,5,4]}
mean_key_value(input_dict)



