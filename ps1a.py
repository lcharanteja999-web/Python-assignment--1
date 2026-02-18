# take annual salary from user
annual_salary = float(input("Enter your annual salary: "))

#portion of salary to save
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

#cost of dream house
house_cost = float(input("Enter the cost of your dream home: "))


down_payment = 0.25 * house_cost
monthly_salary = annual_salary / 12
monthly_return = 0.04 / 12


current_savings = 0.0
months = 0

# keep saving until we reach the down payment
while current_savings < down_payment:

    # money earned from interest
    interest = current_savings * monthly_return
    
    # money saved from salary
    saving = monthly_salary * portion_saved
    
    # update savings
    current_savings = current_savings + interest + saving

    months += 1        #counting number of months
# output
print("Number of months:", months)
