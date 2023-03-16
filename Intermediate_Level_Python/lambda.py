def func(x):
    func2 = lambda x: x + 5
    return x+5

print(func(2))

#Alternative

def func(x):
    func2 = lambda x: x + 5

    return func2(x) + 90

func3 = lambda x,y: x + y
print(func3(5,5))

print(func(2))

# Example

a = [32,21,43,32,54,65,76,24,52]

newList = list(filter(lambda x: x%2==0,a))
print(newList)
