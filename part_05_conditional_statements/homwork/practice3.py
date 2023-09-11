# Get the salary as input from the user
salary = float(input("Enter your salary in NIS: "))

# Check if the salary is 20000 NIS or more
if salary >= 20000:
    # Calculate the tax amount (13% of the salary)
    tax = 0.13 * salary

    # Calculate the net salary after tax deduction
    net_salary = salary - tax

    # Print the net salary after tax deduction
    print(f"Net salary after a 13% tax deduction: {net_salary} NIS")
else:
    # If the salary is less than 20000 NIS, no tax is deducted
    print(f"Salary without tax deduction: {salary} NIS")
