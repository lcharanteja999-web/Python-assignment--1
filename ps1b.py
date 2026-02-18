#annual salary from user
annual_salary = float(input("Enter your starting annual salary: \n"))

#portion of salary to save 
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:\n "))

#cost of the dream house
house_cost = float(input("Enter the cost of your dream home: \n"))

#semi annual raise in percentage
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: \n"))


portion_down_payment = 0.25
annual_return = 0.04


down_payment = house_cost * portion_down_payment
current_savings = 0
months = 0

# keep saving until we reach the down payment
while current_savings < down_payment:

    monthly_salary = annual_salary / 12

    # add interest
    current_savings += current_savings * (annual_return / 12)

    # add savings from salary
    current_savings += monthly_salary * portion_saved

    months += 1 #counts number of months

    #  for every 6 months apply salary raise
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

# Output
print("Number of months:", months)

