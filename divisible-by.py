# Print out all numbers divisible by 7 between a starting value and ending value

starting_value = int(input("What value should we start at? "))
ending_value = int(input("What value should we end at? "))
divide_by = int(input("What number to check divisibility for? "))

current_number = starting_value
while current_number < ending_value:
    if current_number % divide_by == 0:
        print(current_number, "is divisible by", divide_by)
    current_number += 1
