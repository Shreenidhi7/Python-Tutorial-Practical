"""
Compound Interest =
P -> Principal Amount
T -> Time Duration
R -> Rate of Interest

Amount = P [ 1 + R/100] ** T
Compound Interest = A - P

"""

principal_amount = float(input("Enter the principal amount: "))
time_duration = float(input("Enter the time duration: "))
rate_of_interest = float(input("Enter the rate of interest: "))

# Amount Calculation
# amount1 = principal_amount * (1 + rate_of_interest / 100) ** time_duration
amount2 = principal_amount * pow((1 + rate_of_interest / 100), time_duration)
# print("The amount is:", amount1)

print("Amount Calculation")
print("The amount is:", amount2)
print("The amount is rounded to 2 digits:", round(amount2, 2))

# Compound Interest Calculation
compoundInterest = amount2 - principal_amount
compoundInterest_rounded = round(amount2, 2) - principal_amount
print("Compound Interest Calculation")
print("The compound interest is:", compoundInterest)
print("The compound interest is:", compoundInterest_rounded)

