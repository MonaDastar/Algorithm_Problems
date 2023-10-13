import random
def list_generator():
    """generates random(1-10) digit-length list including random numbers(1-100)

    Returns:
        list: list of numbers 1-100 in the length of 1-10 
    """
    return ([random.randint(1,100) for _ in range(random.randint(1,10))])



def merge_sorted_list(list1,list2):
    list3 = []
    j=0
    k=0
    while(j<len(list1) and k <len(list2)):
        if list1[j]<list2[k]:
            list3.append(list1[j])
            j+=1
        else:
            list3.append(list2[k])
            k+=1
            
    if(j<len(list1)):
        for _ in range(j,len(list1)):
            list3.append(list1[_])
    elif(k<len(list2)):
        for _ in range(k,len(list2)):
            list3.append(list2[_])
            
    return(list3)


def split_lists_in_halves(input_list):
    """splits the lists in halves

    Args:
        input_list (list): list of unsorted numbers
    Returns:
        first_half(list): sublist1
        second_half(list): sublist2
    """
    mid = len(input_list)//2
    first_half = input_list[:mid]
    second_half = input_list[mid:]
    
    return(first_half,second_half)

def merge_sort(input_list):
    """
    Sorts a list of comparable elements using the merge sort algorithm.

    Merge sort is a divide-and-conquer sorting algorithm. It recursively divides
    the input list into smaller halves, sorts those halves, and then merges them
    back together to produce a single sorted list.

    Args:
        input_list (list): The list to be sorted.

    Returns:
        list: A new list containing the elements of the input list in sorted order.

    Example:
        >>> input_list = [38, 27, 43, 3, 9, 82, 10]
        >>> merge_sort(input_list)
        [3, 9, 10, 27, 38, 43, 82]

    Note:
        This function preserves the original list and returns a new sorted list.
    """
    if len(input_list) <= 1:
        return input_list

    # Split the input_list into two halves
    first_half,second_half= split_lists_in_halves(input_list)
    
    # Recursively call merge_sort on both halves
    sorted_first_half = merge_sort(first_half)
    sorted_second_half = merge_sort(second_half)
    
    # Merge the two sorted halves using your merge function
    merged_sorted_list= merge_sorted_list(sorted_first_half,sorted_second_half)
    return merged_sorted_list


input_list = list_generator()
print(input_list)
print("**************")
l1,l2= split_lists_in_halves(input_list=input_list)
print(l1,l2)
#print(merge_sort(input_list))
print(merge_sort(input_list=input_list))