from sympy import FiniteSet


def probability(space, event):
    return len(event)/len(space)

def check_prime(number):
    if number != 1:
        for factor in range(2,number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

if __name__ == "__main__":
    space = FiniteSet(*range(2, 21))
    prime = []
    for num in space:
        if check_prime(num):
            prime.append(num)
        event = FiniteSet(*prime)
        p = probability(space, event)

        print("Sample space: {0}".format(space))
        print('Event: {0}'.format(event))
        print("Probability of rolling a prime: {0:.5f}".format(p))


