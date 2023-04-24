name = "Thomas Howard Shelby"

size = len(name)
i = -1

# Iterate loop till the last character
while i < size - 1:
    i = i + 1
    # skip loop body if current character is space
    if name[i].isspace():
        continue
    print(name[i], end='.')

# Example 2:

b = input("Enter a Word: ")
for j in b :
    if (j != 'B'):
        continue
    else:
        print("B is found")
        break
    print("B is not Found in the name")

# Example 3:

count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        count += 2
        continue
    elif 5 < count < 9:
        break # abnormal exit if we get here
    print("count = ", count)

else: # while else
    print("Normal exit with", count)


# Example 4:

number = 0

for number in range(10):
    number = number + 1
    if number == 5:
        pass
    print("Number is " + str(number))
print("Out of the Loop")
