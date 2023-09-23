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