import random
def list_generator():
    """generates random(1-10) digit-length list including random numbers(1-100)

    Returns:
        list: list of numbers 1-100 in the length of 1-10 
    """
    return ([random.randint(1,100) for _ in range(random.randint(1,10))])

def selection_sort(input_list):
    """sort the given list by selection algorithm

    Args:
        input_list (list): unsorted
    Return:
        returns sorted list
    """
    min=0
    current=0
    for i in range(len(input_list)):
        min = i
        for j in range(i+1,len(input_list)):
            if input_list[j]<input_list[min]:
                min = j
        input_list[i],input_list[min] = input_list[min],input_list[i]

        
    return(input_list)
                
list1= list_generator()
print(list1)
print(selection_sort(list1))