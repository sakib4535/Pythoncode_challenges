# Example

id = 0

for i in range(10):
    id += 1
    if id == 7:
        break
    print("Id number is " + str(id))
print("Please other ids are not allowed.")


# Example: Nested 'brea' Loops

for i in range(500):
    print(i, end='___')
    if i >= 390:
        break
print("Completed.")

for val in "Dhaka University is not Harvard University HAHAHA":
    if val == "i":
        break
    print(val)
print("The End")

# Example 3:

name = input("Enter your Name: ")
for j in name:
    if (j=="S", 's'):
        print("I got 'S/s' in your Name")
        break
    else:
        print("'S/s' is not found Bro")

name = "Sakib Imtiaz"

size = len(name)
k = 0
# Iterate loop till the last char

while k < size:
    if name[k].isspace():
        break
    print(name[k], end="--")
    k = k + 1

# Example 4:

for a in range(1,21):
    print("Multiplication Table: ", a)
    for b in range(1,21):
        if a > 10 and b > 10:
            break
        print(a*b, end=' ')
    print('')

# Example 5:

for val1 in "Iteration":
    if val == 'i':
        continue
    print(val1)
print("The End")