monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - monthly_expenses #monthly savings
print(f'Your monthly savings are ${monthly_savings:.0f}.')

rate = 0.05 #simple annual interest rate is 5%
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f'Projected savings after one year, with interest, is: ${projected_savings:.0f}.')
