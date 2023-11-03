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
# print(reversedRange(data))



def reversedBinaryInteger(x:int)-> list:
    my_list=[]
    while x >= 1 :
        my_list.append(x%2)
        x = x //  2
# print(reversedBinaryInteger(10))



from typing import List

# def gcd( array :list)-> int:
    
#     array = sorted(array, reverse = False)
#     gcd = 0
#     list_of_gcds = []
#     list_of_gcd = []
#     for i in range (array[0]):
#         devide_remaining  = number % i
#         if  devide_remaining  == 0:
#             list_of_gcd.append(i)
#     list_of_gcd = list_of_gcd[::-1]
#     list_of_gcds = []
    
#     for item in list_of_gcds:
#         for number in array[1:]:
#             if number % item != 0:
#                 gcd = 1
#                 break
#             else:
#                 gcd = item

#         (gcd([6,12,30,5])) 


# array = [5,6,4,12]
# array = sorted(array , reverse = False)


# print(array)
# array_dict = {}
# for item in array:
#     array_dict[item] = []
    
# for value in array:
#     for i in range(2,value+1):
#         if value % i == 0:
#             array_dict[value].append(i)
# largest_common = set()
# for values in array_dict.values():
#     if not largest_common:
#         largest_common= set(values)
        
#     else:
#         largest_common= largest_common.intersection(set(values))
        
# print(list(largest_common))



    



