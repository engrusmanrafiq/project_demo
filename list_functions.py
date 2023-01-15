list1 = [12, 15, 18, 45, 88, 45, 13]
list1.sort()
print(list1, 'List1 has been sorted')

list2 = ['usman', 'irfan', 'touseef', 'haider', 'zeeshan']
list2.reverse()
print(list2, 'List2 has been reversed')

list3 = []
list3.copy(list2)
print(list3, 'list3 has been copied by the elements of list2')

index_value = list2[1:3]
print('nex indexed values are', index_value)