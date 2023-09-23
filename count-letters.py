# Program counts how many uppercase and lowercase letters are in the string
input_string = input("Type some text and press ENTER "
    + "we will count the letters for you.\n")

uppercase_count = 0
lowercase_count = 0

for index in range(0, len(input_string)):
    character = input_string[index]
    if character.isupper():
        uppercase_count += 1
    elif character.islower():
        lowercase_count += 1

print("Number of Uppercase Letters:", uppercase_count)
print("Number of Lowercase Letters:", lowercase_count)

