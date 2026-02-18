# take starting salary as input
starting_salary = float(input("Enter the starting salary: "))

  # cost of the dream house
house_cost = 1000000   

# 25% down payment required
down_payment = house_cost * 0.25 

# 4% annual return on savings
annual_return = 0.04   

 # 7% raise every 6 months
semi_annual_raise = 0.07 

  # total months to save 3 years
months = 36                         


current_savings = 0
salary = starting_salary

for m in range(1, months + 1):
    # add monthly investment return
    current_savings += current_savings * annual_return / 12
    
    # add full monthly salary 
    current_savings += salary / 12
    
    # apply semi annual raise every 6 months
    if m % 6 == 0:
        salary += salary * semi_annual_raise

# if even saving 100% is not enough print not possible
if current_savings < down_payment - 100:
    print("It is not possible to pay the down payment in three years.")

else:
  
    low = 0                  # lowest possible saving rate 
    high = 10000             # highest possible saving rate 
    steps = 0                # count number of bisection steps
    best_rate = 0            # store final best rate

    while True:
        steps += 1

        mid = (low + high) // 2
        rate = mid / 10000   # convert to decimal 

        current_savings = 0
        salary = starting_salary
 

        for m in range(1, months + 1):
            current_savings += current_savings * annual_return / 12
            current_savings += (salary / 12) * rate

            if m % 6 == 0:
                salary += salary * semi_annual_raise

        # check if within $100
        if (current_savings >= down_payment - 100) and (current_savings <= down_payment + 100):
            best_rate = rate
            break

        # too low increase rate
        elif current_savings < down_payment:
            low = mid

        # too high decrease rate
        else:
            high = mid

#output
    print(f"Best savings rate: {best_rate:.4f}")
    print("Steps in bisection search:", steps)