my_list=[1,2,3,4,5]
print("Original List:",my_list)
my_list.append(6)
print("After appending 6:",my_list)
my_list.remove(6)
print("After removing 6:",my_list)
my_list.pop(2)
print("After popping index 2:",my_list)
 
my_dict={"name":"Shreya","age":19}
print("Original dictionary:",my_dict)
my_dict["city"]="Chennai"
print("After adding city:",my_dict)
del my_dict["age"]
print("After removing age:",my_dict)
my_dict.clear()
print("After clearing:",my_dict)

my_set={1,2,3,4,5}
print("Original set:",my_set)
my_set.add(6)
print("After adding 6:",my_set)
my_set.remove(6)
print("After removing 6:",my_set)
my_set.clear()
print("After clearing:",my_set)
