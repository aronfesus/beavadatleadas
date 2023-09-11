#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

def contains_odd(my_list):
    var = False
    for element in my_list:
        if element % 2 == 1:
            var = True
            break
    return var


#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list


def is_odd(my_list):
    return [ True if element % 2 == 1 else False for element in my_list ]


#Create a function that accpects 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

def element_wise_sum(list_1,list_2):
    return [ element_1 + element_2  for element_1,element_2 in zip(list_1,list_2)] 



#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

def dict_to_list(dictionary):
    return [ item for item in dictionary.items()]