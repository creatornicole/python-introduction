"""
Application that allows user to see a summary of their 
annual expenses and savings.
"""

def calculate_taxes(annual_salary):
    if annual_salary >= 0 and annual_salary <= 10000:
        taxes = 5
    elif annual_salary >= 10001 and annual_salary <= 40000:
        taxes = 10
    elif annual_salary >= 40001 and annual_salary <= 80000:
        taxes = 15
    else:
        taxes = 20
    annual_taxes = (annual_salary / 100) * taxes
    return annual_taxes


def convert_to_currency_string(amount_of_money):
    currency_string = "NOT VALID, input must be of datatype float"
    if isinstance(amount_of_money, float):
        currency_string = "$ {:,.2f}\t".format(amount_of_money)
    return currency_string


def convert_to_percentage_string(percent):
    percentage_string = "NOT VALID, input must be of datatype float"
    if isinstance(percent, float):
        percentage_string = "{:.1f}%".format(percent)
    return percentage_string


def generate_table(annual_salary, annual_housing, annual_bills, annual_food, annual_travel, annual_taxes):
    extra = annual_salary - annual_housing - annual_bills - annual_food - annual_travel - annual_taxes
    
    annual_housing_formatted = convert_to_currency_string(annual_housing)
    annual_bills_formatted = convert_to_currency_string(annual_bills)
    annual_food_formatted = convert_to_currency_string(annual_food)
    annual_travel_formatted = convert_to_currency_string(annual_travel)
    annual_taxes_formatted = convert_to_currency_string(annual_taxes)
    extra_formatted = convert_to_currency_string(extra)

    percent_housing = get_percentage(annual_salary, annual_housing)
    percent_bills = get_percentage(annual_salary, annual_bills)
    percent_food = get_percentage(annual_salary, annual_food)
    percent_travel = get_percentage(annual_salary, annual_travel)
    percent_taxes = get_percentage(annual_salary, annual_taxes)
    percent_extra = get_percentage(annual_salary, extra)

    percent_housing_formatted = convert_to_percentage_string(percent_housing)
    percent_bills_formatted = convert_to_percentage_string(percent_bills)
    percent_food_formatted = convert_to_percentage_string(percent_food)
    percent_travel_formatted = convert_to_percentage_string(percent_travel)
    percent_taxes_formatted = convert_to_percentage_string(percent_taxes)
    percent_extra_formatted = convert_to_percentage_string(percent_extra)

    print("-" * 30)
    print("housing | ", annual_housing_formatted, " | ", percent_housing_formatted, " | ")
    print("  bills | ", annual_bills_formatted, " | ", percent_bills_formatted, " | ")
    print("   food | ", annual_food_formatted, " | ", percent_food_formatted, " | ")
    print(" travel | ", annual_travel_formatted, " | ", percent_travel_formatted, " | ")
    print("    tax | ", annual_taxes_formatted, " | ", percent_taxes_formatted, " | ")
    print("  extra | ", extra_formatted, " | ", percent_extra_formatted, " | ")
    print("-" * 30)


def calculate_monthly_to_annual_expenses(monthly_expenses):
    return monthly_expenses * 12


def caluclate_weekly_to_annual_expenses(weekly_expenses):
    # according to google search, 1 year = 52.1786 weeks
    return weekly_expenses * 52.1786


def get_percentage(total, part):
    ratio = total / part
    percentage = 100 / ratio
    return percentage



# MAIN
print(("-" * 37)+ "\n" + ("-" * 5) 
    + " FINANCIAL VISUALIZER U.S. " 
    + ("-" * 5) + "\n" + ("-" * 37))

annual_salary = input("What is your annual salary? ")
monthly_housing = input("How much do you spend for housing per month? ")
monthly_bills = input("What are your fixed expenses per month? ")
weekly_food = input("How much do you spend for food per week? ")
annual_travel = input("How much do you spend for travelling in one year? ")

if(annual_salary.isnumeric() and monthly_housing.isnumeric() and monthly_bills.isnumeric() 
    and weekly_food.isnumeric() and annual_travel.isnumeric()):
    annual_salary = float(annual_salary)
    monthly_housing = float(monthly_housing)
    monthly_bills = float(monthly_bills)
    weekly_food = float(weekly_food)
    annual_travel = float(annual_travel)

    annual_housing = calculate_monthly_to_annual_expenses(monthly_housing)
    annual_bills = calculate_monthly_to_annual_expenses(monthly_bills)
    annual_food = caluclate_weekly_to_annual_expenses(weekly_food)
    annual_taxes = calculate_taxes(annual_salary)

    generate_table(annual_salary, annual_housing, annual_bills, annual_food, annual_travel, annual_taxes)    
else:
    print("All input values have to be numbers.")
