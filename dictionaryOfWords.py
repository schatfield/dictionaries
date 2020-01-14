"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["cold"] = "to need a sweater"
word_definitions["hot"] = "to need to get out of the sweater"
word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Sad"] = "The feeling of students when they are learning Python"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

print(word_definitions["cold"])
print(word_definitions["hot"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

# for (key, value) in animal.items():
    # print(f"{key}: {value}")

for word in word_definitions:
    print(f"The definition of {word} is {word_definitions[word]}")
    print()