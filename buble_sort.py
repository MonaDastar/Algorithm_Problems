import random
def list_generator():
    """generates random(1-10) digit-length list including random numbers(1-100)

    Returns:
        list: list of numbers 1-100 in the length of 1-10 
    """
    return ([random.randint(1,30) for _ in range(random.randint(1,10))])

def bubble_sort(input_list):
    """sort with bubble sort algorithm

    Args:
        input_list (list): unsorted list of numbers
    Return:
        input_list(list): sorted list 
    """
    for i in range (len(input_list)):
        for j in range (0,len(input_list)-i-1):
            if(input_list[j]>input_list[j+1]):
                input_list[j],input_list[j+1]=input_list[j+1],input_list[j]
        
    return(input_list)
list1=list_generator()
print(list1)
print("***********")
print(bubble_sort(list1))