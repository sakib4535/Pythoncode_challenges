# Print Name 5 times

def print_name(name, n):
    if n == 0:
        return
    print(name)
    print_name(name, n-1) # This will decrease 1 step backward to print 5 times

print_name("John", 5)


# uses recursion to print numbers from 1 to a given number n linearly

def print_linear(n):
    if n==1:
        print(n)
        return
    print_linear(n-1)
    print(n)

print_linear(5)

# print from N to 1 which is Reverse Format

def print_reverse(n):
    if n==1:
        return
    print(n)
    print_reverse(n-1)

print_reverse(5)

# Use 'Backtracking' to print numbers from 1 to a given number N linearly
print("_____________________________________________________________________________________")
def print_linear_backtrack(n, i=1):

    """
    print_linear_backtrack is a recursive function that takes two arguments:
    n, which is the number to print up to, and i, which is the current number being printed.

    If i is not greater than n, the function prints i and then calls itself with n
    as the first argument and i+1 as the second argument. This continues until i reaches n.
    """
    if i > n:
        return
    print(i)
    print_linear_backtrack(n, i+1)

print_linear_backtrack(5)
