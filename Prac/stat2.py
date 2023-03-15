""""Find the Variance and Standard Deviation of a list of numbers"""

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N

    return mean

def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []

    for num in numbers:
        diff.append(num-mean) ##each value substracted by centralized mean value to find the diff
    return diff

def calculate_variance(numbers):
    diff = find_differences(numbers)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2) # it means xi - x(mean) square

    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / len(numbers)
    return variance

if __name__ == "__main__":
    donations = [12,3,13,14,312,52,3,1,32,213,123,123,3121,33,21,3,213,12]
    variance = calculate_variance(donations)
    print("The variance of the list of numbers is {0}".format(variance))

    std = variance**0.5
    print('The standard deviation of the list of numbers is {0}'.format(std))

#####################################################

"""Correlation Analysis """

def find_corr_x_y(x,y):
    n = len(x)

    prod = []
    for xi, yi in zip(x,y):
        prod.append(xi*yi)

    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2

    x_square = []
    for xi in x:
        x_square.append(xi**2)
    x_square_sum = sum(x_square)

    y_square = []
    for yi in y:
        y_square.append(yi**2)

    y_square_sum = sum(y_square)

    #Using Formula to calculate correlation

    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator

    return correlation

if __name__ == "__main__":

    list1 = [21,14,56,21,12,46,89]
    list2 = [21,23,56,78,90,64,32]

    print(find_corr_x_y(list1,list2))
