income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses:"))

savings = income - expenses #monthly savings
print(f'Your monthly savings are ${savings}.')

rate = 0.05 #simple annual interest rate is 5%
projected_savings = savings * 12 + (savings * 12 * 0.05)
print(f'Projected savings after one year, with interest, is: ${projected_savings:.0f}.')
