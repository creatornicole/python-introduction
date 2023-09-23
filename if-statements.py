# Tell user if they earned more money than they spent
earned = int(input("How much money did you earn? "))
spent = int(input("How much money did you spend? "))
if earned > spent:
    print("Great! You earned more than you spent. Good job, keep it up!")
if earned == spent:
    print("Watch out, you spent as much money as you earned. Better keep it this.")
if earned < spent:
    print("You are in a deficit!")