name,family,age,nationality=("Mona","Dastar",35,"Iranian")
travel_id = [('Iran',98),('USA',110),('Canada',112),('England',265)]
# for passp in sorted(travel_id):
    
    # print('%s/%s'% passp) #The % formatting operator understands tuples and treats each item as a separate
                          #field.
    
# for country,_ in travel_id: #The for loop knows how to retrieve the items of a tuple separately—this is called
#                             #“unpacking.” Here we are not interested in the second item, so we assign it to _, a
#     print(country)                        #dummy variable.
    
list1 = [1,2,3,4,5]
list1.extend(travel_id)
list1.extend(name)
# print (list1)


t = (20,8)
# print(t)

a,b = divmod(*t)
# print(a,b)

a,b,*rest = range(5)#Using * to Grab Excess Items
print(a,b,rest)#0,1,[2,3,4]
a,b,*rest = range(2)
print(a,b,rest)#0,1,[]
a,*body,c,d=range(5)
print(a,body,c,d) #0,[1,2],3,4

# Example 2-8. Unpacking nested tuples to access the longitude
metro_areas=[
    ('Tokyo','JP',3.4,(18.2,57.6)),
    ('Teh','Iran',5.2,(55.2,66.8))
]
for name,_,_,(lan,lon)in metro_areas:
        
    if lon>10:
        
        print(name,(lan,lon))
        