"""
Simple Interest = (P * T * R)/100
P -> Principal Amount
T -> Time Duration
R -> Rate of Interest
"""

principal_amount = float(input("Enter the principal amount: "))
time_duration = float(input("Enter the time duration: "))
rate_of_interest = float(input("Enter the rate of interest: "))

simple_interest = (principal_amount * time_duration * rate_of_interest)/100
print("The simple interest calculation is ", simple_interest)