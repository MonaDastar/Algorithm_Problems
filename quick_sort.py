def quick_sort(list):
    """Sorts an unsorted Array of numbers

    Args:
        list (list): unsorted list

    Returns:
        list: sorted list
    """
    
    if len(list) <= 1:
        return list
    
    
    pivot = list[len(list)//2]
    left = [x for x in list if x<pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    
    return quick_sort(left)+middle+quick_sort(right)

list = [5,8,9,7,3,50,60,52,6,50]
print(quick_sort(list))