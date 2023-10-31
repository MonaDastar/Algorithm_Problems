from typing import Dict,List 
def knapsack():
            
    items = {
        "guitar" :(1000, 25000),
        
        "DVD player":(1500, 1000),
        
        "wrist watch" :(100, 10000),
        
        "golden ring":(10,3000),
    }

    print(f" items are: {items}")
    print("______________________________________________________________")
    limitation = 300
    bag_weight = 0
    bag_value = 0
    left_amount=0
    value_portion=0
    ratio = [(name,value/weight) for name, (weight,value) in items.items()]
    sorted_ratio = sorted(ratio , key= lambda x:x[1], reverse = True)
    print(f"sorted ratio:{sorted_ratio}")
    print("______________________________________________________________")
    item_name=[]
    items_in_the_bag=0
    for item in sorted_ratio:
        item_name.append(item[0])
    dict_sorted_ratio = {key:value for key,value in sorted_ratio}
    # while bag_weight <= limitation:
    for name in item_name:
        if (bag_weight + items[name][0]) <= limitation:
            
            bag_weight += items[name][0]
            bag_value += items[name][1]
            items_in_the_bag +=1
            print(f"item added: {name},:{items[name][0]} grams, ${items[name][1]},  bag_weight :{bag_weight} gram, bag_value:${bag_value}")
            
        else:
            left_amount = limitation - bag_weight
            value_portion = left_amount * (dict_sorted_ratio[name]) # left_amount X next item ratio (value/weight)
            bag_value +=  value_portion
            bag_weight += left_amount
            items_in_the_bag += 1
            print(f"item added: {name},:{items[name][0]} grams, ${items[name][1]},  bag_weight :{bag_weight} gram, bag_value:${bag_value}")


    print(f"the bag worths $ {bag_value} and weights {bag_weight} grams, and it is consists of {items_in_the_bag}")

knapsack()