def insertion_sort(input_list):
    sorted_list = input_list.copy()  

    for i in range(1, len(sorted_list)):
        current = sorted_list[i]
        j = i - 1

        while j >= 0 and sorted_list[j] > current:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1

        sorted_list[j + 1] = current

    return sorted_list

list1 = [5, 1, 9, 3, 7, 2]
sorted_list = insertion_sort(list1)
print(sorted_list)
