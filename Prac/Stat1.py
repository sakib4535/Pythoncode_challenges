"""Calculating the Mean Value"""

def mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N

    return mean
if __name__ == "__main__":
    donations = [100, 50, 21, 56, 141,21, 31,67,788,46,89,90,55]
    mean = mean(donations)
    N = len(donations) # For printing purpose
    print("mean Donation over last {0} days wis {1}".format(N, mean))

#################################################3

"""Finding Median Value"""

def median(numbers):
    N =len(numbers)
    numbers.sort()

    if N % 2 == 0:
        m1 = N/2
        m2 = (N/2) + 1

        m1 = int(m1) - 1 # - 1 used because index position of python begins with '0'
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        m = int(m) - 1
        median = numbers[m]
    return median

if __name__ == "__main__":
    donations = [120, 34, 41, 67, 56, 513,212,41,2,41,21]
    N = len(donations)
    median = median(donations)

print("You {0} days counted {1} median value".format(N, median))

################################################3

"""Finding Mode"""

from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

if __name__ == "__main__":
    scores = [4,2,2,6,7,9,0,8,6,7,8,4,2,1,6,8,0]
    mode = calculate_mode(scores)

    print("The mode of the list of numbers is :{0}".format(mode))

################################

"""What if two or many numbers occur as mode?"""
"""Calculating the mode when the list of numbers may have multiple modes"""

from collections import Counter

def calculate_mode(numbers):

    c = Counter(numbers)
    num_freq = c.most_common()
    max_count = num_freq[0][1] # inside tuple we will go for second elements contains the frequency

    modes = []
    for num in num_freq:
        if num[1] == max_count:
            modes.append(num[0])

    return modes

if __name__ == "__main__":
    scores = [32,9, 43, 56,9, 12, 12, 18, 9, 18, 32]
    modes = calculate_mode(scores)
    print("the modes of the list of numbers are: ")
    for mode in modes:
        print(mode)

###################################

"""Creating Frequency Table"""

from collections import Counter

def freq_table(numbers):
    table = Counter(numbers)
    print('Number\tFrequency')
    for number in table.most_common():
        print("{0}\t{1}".format(number[0], number[1]))

if __name__ == "__main__":
    scores = [7,6,4,2,6,7,4,2,1,1,3,4,5,7,8,9,5,4,2,4,2]
    freq_table(scores)

"""We Want to Sort the Frequency List"""

from collections import Counter

def freq_table(numbers):
    table = Counter(numbers)
    num_freq = table.most_common()
    num_freq.sort()

    print("Number\tFrequency")
    for number in num_freq:
        print("{0}\t{1}".format(number[0], number[1]))

if __name__ == "__main__":
    scores = [3,4,5,6,7,8,9,0,2,3,4,5,6,7,8,9,0]
    freq_table(scores)

"""finding the range in a list of numbers"""

def find_range(numbers):

    lowest = min(numbers)
    highest = max(numbers)
    r = highest - lowest

    return lowest, highest, r

if __name__ == "__main__":
    donations = [13,523,14,6,47,323,545,23,445,321,134,435,]
    lowest, highest, r = find_range(donations)
    print("Lowest: {0} and Highest: {1} Range: {2}".format(lowest, highest, r))
