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
print(f"The Future Value is ${future_value} and there are {remaining_months} remaining months")


discount_rate = .20

present_value = future_value / (1 + discount_rate/12 ) ** remaining_months
print(f"The Present Value of the Loan is ${present_value:.2f}")


if future_value >= present_value:
    print(f"This is a good loan to buy at ${present_value:.2f}")
else:
    print(f"Do not buy this loan at {present_value}")