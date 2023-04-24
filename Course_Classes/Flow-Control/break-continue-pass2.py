"""
# Problem: Find the smallest positive integer that is evenly divisible by all numbers from 1 to 10

If the number is divisible by all numbers from 1 to 10, the code prints the answer using the "print" statement
and terminates the while loop using the "break" statement.
"""

num = 1 # Initializing start

# Loop until the naswer is found
while True:
    # check if the current number is divisible by all numbers from 1 to 10
    for i in range(1,11):
        if num % i != 0:
            # If the number is not divisible, move on the next one
            break
    else:
        # If the number is divisible by all numbers from 1 to 10, we have found the answer
        print("The smallest positive integer")
        break

    # If the number is not divisible by all numbers from 1 to 10, try next one
    num += 1
    continue

print("This line will not be printed")