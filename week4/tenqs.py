def countOnes(array):
    """ returns the number of adjacent ones in an array of 0 and 1
    for example 1010110111 will return 2 """
    counter = 0 
    one_counter = 0
    for number in array:
        if number == "1":
            counter+=1
        else:
            if counter>1:
                one_counter += 1
                counter = 0
            else:
                counter = 0
    if counter >1:
        one_counter += 1
    return(one_counter)


# print(countOnes("110110111111110"))





from typing import Tuple, List

def reversedRange(data: Tuple[List[int], int, int]) -> list:
    my_list, index1, index2 = data
    rev_list = my_list[index1:index2+1]
    rev_list = rev_list[::-1]
    new_list = []
    
    # for i in range(len(my_list)):
    #     if i < index1:
    #         new_list.append(my_list[i])
    #     elif i == index1 or i<= index2:
    #         new_list.append(rev_list)
    #     elif i> index2 and i<= len(my_list):
    #         new_list.append(my_list[i])
    new_list= my_list[0:index1] 
    for _ in rev_list:
        new_list.append(_)
    for _ in my_list[index2+1:]:
        new_list.append(_)
    return(new_list)
            
    
data=([0,1,2,3,4,5,6,7,8,9],2,5)
print(reversedRange(data))




            
            

