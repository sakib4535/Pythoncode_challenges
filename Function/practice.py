def multiply():
    result = 11.3 * 6
    return result

def is_palindrome(string):
    #backwards = [::-1]
    #return backward == string
    return string[::-1].casefold() == string.casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].casefold() == string.casefold()


word = input("Pleas Enter the Word: ")
#if is_palindrome(word):
if palindrome_sentence(word):
    print("Here is {} as Palindrome".format(word))
else:
    print("Go for this: {}".format(word))

tick =  multiply()
print(tick)

def multiply(x, y):
    result = x * y
    return result


answer = multiply(11.5, 8)
print(answer)

forty_two = multiply(6.7, 9.1)
print(forty_two)

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

