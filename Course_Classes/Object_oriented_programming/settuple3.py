my_tuple = (1, 'hello', 5.6789, [4,5,6,7])

# USe Index Method to find the index of a variable in the tuple
index = my_tuple.index('hello')
print(f"The index of hello inside the tuple is {index}")

# Use a user-defined function to find the length of the tuple
def tuple_length(tup):
    return len(tup)

# print tuple and using the function
print(f"The tuple is {my_tuple}")
print(f"The length of the tuple is {tuple_length(my_tuple)}")

# USe slicing Method to access he parts of the tuple
slice1 = my_tuple[1:]
slice2 = my_tuple[0:2]
print(f"The Slice from index 1 to the end is {slice1}")
print(f"The slice from index 0 to 1 is {slice2}")
