# List, Tuple, Set

languages = ["C", "C++", "Python", "Java", "Ruby", "C#", "Text Script", "Fortran"]
numbers = [23,34,65,7778,533,21,334,32,456,231,123,890,333,89,65]
print(type(languages))

for i, index in enumerate(languages):
    print(i,index)

for j in range(len(numbers)):
    print(j)

print("The len of the language list is : ", len(languages))

# Lets set a user defined functions for both integer and text values
def language_length(languages):
    lengths = {}
    for language in languages:
        lengths[language] = len(language)
    return lengths

# Use the function to get a dictionary of language lengths and
language_length_dict = language_length(languages)
print("Language lengths:", language_length_dict)

large_numbers = [num for num in numbers if num > 100]
print("Large Numbers: ", large_numbers)

# Use a Lambda function to sort the languages list by length
sorted_languages = sorted(languages, key=lambda x: len(x))
print("sorted languages: ", sorted_languages)

# Use the zip function to iterate over both lists simultaneously and print their value
for lang, num in zip(languages, numbers):
    print(f"{lang}: {num}")

# Use a list comprehension to filter the numbers list for values greater than 100

list1 = ["S1", "Simple", "S2", "is", "S3", "better", "S4", "than", "S5", "complex"]
pro_len = ["C", "C++", "Python", "Java"]


# Set will only print for one time and won't repeat same words and objects.
word_list2 = ["simple", "is", "better", "than", "complex"]
print(type(word_list2))
