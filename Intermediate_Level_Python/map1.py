li = [2,4,5,6,7,8,9]

def func(x):
    return x**x

newlist = []
for x in li:
    newlist.append(func(x))

print(newlist)

# Alternative Method

print(list(map(func, li)))

# Second alternative

print([func(x) for x in li if x%2==0])
