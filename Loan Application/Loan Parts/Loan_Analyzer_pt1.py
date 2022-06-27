"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]



num_of_loans = len(loan_costs)
print(f"The number of loans is {num_of_loans}.")



total_of_loans = sum(loan_costs)
print(f"The total numbers of loans is {total_of_loans}.")


average_of_loans = total_of_loans / num_of_loans
print(f"The average loan amount is ${average_of_loans}.")