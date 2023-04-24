# Create a tuple of three variables
my_tuple = (10, "hello", 3.14)
second_var = my_tuple[1]
print("Second variable: ", second_var)

def tuple_sum(my_tuple):
    if all(isinstance(x, (int, float)) for x in my_tuple):
        return sum(my_tuple)
    else:
        raise TypeError("Input tuple must contain only numbers.")

print("Tuple Sum: ", tuple_sum(my_tuple))
new_tuple = ("apple", 5)

# unpack the tuple into two separate variables
fruit, quantity = new_tuple
print("Fruit: ", fruit)
print("Quantity: ", quantity)

# Use a user-defined function to get the length of the tuple
def tuple_length(my_tuple):
    return len(my_tuple)

# print the tuple and its length using the function
print("Tuple:", my_tuple)
print("Tuple length:", tuple_length(my_tuple))
