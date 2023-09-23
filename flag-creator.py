"""
Guided Project 1 - Flag Creator
Goal: Write a program that can print out flags that resemble the U.S. flag
So far Covered Topics: variables, strings, math, string multiplication
"""

width = int(input("Flag Width: "))
height = int(input("Flag Height: "))

half_width = int(width/2)
half_height = int(height/2)

star_symbol = "#"
line_symbol = "-"

upper_row = (star_symbol * half_width) + (line_symbol * half_width) + "\n"
lower_row = (line_symbol * width) + "\n"

flag = (upper_row * int(height/2)) + (lower_row * int(height/2))

print(flag)