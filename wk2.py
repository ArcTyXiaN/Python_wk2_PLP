#append
my_list= []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert
my_list.insert(1, 15)
#extend
list_b=[50 , 60, 70]
my_list.extend(list_b)
print(my_list)
#remove
del my_list[-1]
print(my_list)
#sort
my_list.sort()
print(my_list)
#indexing
index_30 = my_list.index(30)
print(index_30)