# This program calculates either the total gain from the investment or the monthly bond repayments.
# The formulas needed for calculations require a math module to be imported.
import math

# First program output shows two types of calculation that can be performed.
print("investment  -  to calculate the amount of interest you'll earn on your investment")
print("bond        -  to calculate the amount you'll have to pay on a home loan\n")

# Then the user is asked which type of financial product they whant to calculate.
product = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n")

# The user's input is changed to lowercase and compared to the expected values.
# As long as there's no match the program will continue to ask for the valid input.
while (product.lower() not in ['investment', 'bond']):
    product = input("Please enter either 'investment' or 'bond':\n")

# If the 'investment' option is chosen, the user is asked for the additional parameters.
if (product.lower() == 'investment'):

    # Deposit amount and investment term, which should be the whole numbers, are stored as integers.
    deposit = int(input("\nEnter the amount of the deposit (as a whole number):\n"))
    inv_term = int(input("Enter the length of investment in years (as a whole number):\n"))
    
    # Investment rate, which is likely to be a decimal, is stored as a float.
    inv_rate = float(input("Enter the interest rate as a percentage, but without % sign (ex: 3.5 if interest rate is 3.5%):\n"))
    
    # The interest type input is changed to lowercase and compared to the expected values.
    # As long as there's no match the program will continue to ask for the valid input.
    interest = input("Which type of interest is it? Enter 'simple' or 'compound':\n")
    while (interest.lower() not in ['simple', 'compound']):
        interest = input("Please enter either 'simple' or 'compound':\n")

    # Depending on the chosen type of interest, the appropriate calculation is performed and its result displayed.
    # Since the result is a float, the round() function is used to display it with only two decimal places.
    if (interest.lower() == 'simple'):
        amount = deposit * (1 + inv_rate/100 * inv_term) # calculation for the simple interest type
        print(f"\nWith £{deposit} deposit after {inv_term} years at {inv_rate} % interest rate you will get back £{round(amount, 2)}.")
    
    elif (interest.lower() == 'compound'):
        amount = deposit * math.pow((1 + inv_rate/100), inv_term) # calculation for the compound interest type
        print(f"\nWith £{deposit} deposit after {inv_term} years at {inv_rate} % interest rate you will get back £{round(amount, 2)}.")

# If the 'bond' option is chosen, the user is asked for the additional parameters.
elif (product.lower() == 'bond'):
    
    # House value and bond term, which should be the whole numbers, are stored as integers.
    house_value = int(input("\nEnter the present value of your house (as a whole number):\n"))
    bond_term = int(input("Enter the term of the bond in months (as a whole number):\n"))
    
    # Investment rate, which is likely to be a decimal, is stored as a float.
    bond_rate = float(input("Enter the ANNUAL interest rate as a percentage, but without % sign\n(ex: 7.5 if the annual interest rate is 7.5%):\n"))

    # The appropriate calculation for bond repayment is performed and its result displayed.
    # As before, the round() function is used to display it with only two decimal places.
    repayment = (bond_rate/1200 * house_value)/(1 - (1 + bond_rate/1200)**(-bond_term))
    print(f"\nYour monthly repayment amount will be £{round(repayment, 2)}.")