set1 = set(["apple", "banana", "cherry", "orange"])

set1.add("Lemon")
set1.remove('orange')

def set_length(set_name):
    return len(set_name)
print("Set: ", set1)
print("Set length: ", set_length(set1)) # Here we apply the function

#######################################################
########################################################

tuple1 = ("apple", "banana", "cherry")
list1 = list(tuple1)
list1.append("orange")
tuple2 = tuple(list1)
subset_tuple = tuple2[1:3]

def tuple_length(tuple_name):
    return len(tuple_name)

print("Tuple:", tuple2)
print("Tuple Subset: ", subset_tuple)
print("tuple length:", tuple_length(tuple2))
print("Tuple subset length:", tuple_length(subset_tuple))
