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
    return future_value / (1 + annual_discount_rate/12 ) ** remaining_months

#Check Formula
#pv = 1000 / (1 +.2/12 ) ** 12
#print(round(pv, 2))

remaining_months = new_loan.get("remaining_months") 
loan_price = new_loan.get("loan_price")
future_value = new_loan.get("future_value")


annual_discount_rate = .2

#Present Value Calculation Using Calculation Option #1
present_value = calculate_present_value(future_value, annual_discount_rate, remaining_months)

#Present Value Calculation Using Calculation Option #2
present_value2 = calculate_present_value(new_loan["future_value"],annual_discount_rate,new_loan["remaining_months"])

print(f"The present value of the loan is: {present_value:.2f} using Calculation Option #1")
print(f"The present value of the loan is: {present_value:.2f} using Calculation Option #2")