# an Array of unsorted weights, [5.02, 1.20, 8, 6 , 6]
# pack the objects to be >= 10 in each box, 
# how many boxes

def get_array_of_weights(list_of_weights):
    weight = 0
    number_of_boxes_needed = 0
    for item in list_of_weights:
        weight += item
        
        if weight <= 10 :
            
            continue
        else:
            number_of_boxes_needed += 1
            weight = item 
            
    return number_of_boxes_needed+1


list_of_weights = [5, 1, 8, 9, 6,3, 5]
print ( get_array_of_weights(list_of_weights))
