import csv
from dataclasses import fields
from pathlib import Path

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file

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