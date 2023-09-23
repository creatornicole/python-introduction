# Tell user if they earned more money than they spent
earned = int(input("How much money did you earn? "))
spent = int(input("How much money did you spend? "))
if earned > spent:
    print("Great! You earned more than you spent. Good job, keep it up!")
if earned == spent:
    print("Watch out, you spent as much money as you earned. Better keep it this.")
if earned < spent:
    print("You are in a deficit!")


# Register for Class
# Helps students to help them determine what Spanish class they should sign up for

# none if student has not taken Spanish classes, otherwise class number
experience_level = input("What's your current experience level in Spanish? "
    + "(none/101/102/201/202): ")
if experience_level == "none":
    recommendation = "101"
elif experience_level == "101":
    recommendation = "102"
elif experience_level == "102":
    recommendation = "201"
elif experience_level == "201":
    recommendation = "202"
elif experience_level == "202":
    recommendation = "advanced courses"
else:
    recommendation = "Input Error: Only none/101/102/201/202 accepted as input"
print("Based on your experience, you should take the Spanish " + recommendation + " next.")