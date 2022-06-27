# coding: utf-8
import csv
from dataclasses import fields
from pathlib import Path

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
print(f"The total number of loans is: {num_of_loans}.")



total_of_loans = sum(loan_costs)
print(f"The total of the loans is: {total_of_loans}.")


average_of_loans = total_of_loans / num_of_loans
print(f"The average loan amount is: ${average_of_loans}.")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.


"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}



future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The Future Value of the loan is ${future_value} and there are {remaining_months} remaining months.")



discount_rate = .20

present_value = future_value / (1 + discount_rate/12 ) ** remaining_months
print(f"The Present Value of the Loan is ${present_value:.2f}.")




if present_value >= loan.get("loan_price"):
    print(f"This is a good loan to buy at ${present_value:.2f}.")
else:
    print(f"Do not buy this loan at {present_value}.")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}



def calculate_present_value(future_value, annual_discount_rate, remaining_months):
    return (future_value / (1 + annual_discount_rate/12 ) ** remaining_months)

remaining_months = new_loan.get("remaining_months") 
loan_price = new_loan.get("loan_price")
future_value = new_loan.get("future_value")


annual_discount_rate = .2

#Present Value Calculation Using Calculation Option #1
present_value = calculate_present_value(future_value, annual_discount_rate, remaining_months)

#Present Value Calculation Using Calculation Option #2
present_value2 = calculate_present_value(new_loan["future_value"],annual_discount_rate,new_loan["remaining_months"])

print(f"The present value of the loan is: {present_value:.2f} using Calculation Option #1.")
print(f"The present value of the loan is: {present_value:.2f} using Calculation Option #2.")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]



inexpensive_loans = []



for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)


print(inexpensive_loans)

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""


# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")


with open(output_path, 'w', newline='') as csvfile:
    output_writer = csv.writer(csvfile)

    output_writer.writerow(header)

    for row in inexpensive_loans:
        output_writer.writerow(row.values())

