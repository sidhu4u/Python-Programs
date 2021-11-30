# pgm5. Python Program for compound interest


# Formula
# A = P(1 + \frac{r}{n})^{nt} OR CI = P( 1 + r/100)pow(n) - P
# A	=	final amount
# P	=	initial principal balance
# r	=	interest rate
# n	=	number of times interest applied per time period
# t	=	number of time periods elapsed
#


principle_balance = float(input("Principle Amount : "))
interest_rate = float(input("Interest Rate : "))
times_interest_applied = float(input("How many times Interest apllied : "))
time_period = float(input("Time Period : "))

power = times_interest_applied * time_period
final_amt = principle_balance * \
    ((1 + interest_rate/times_interest_applied) ** power)
compound_interest = principle_balance * \
    ((1 + (interest_rate/100)) ** times_interest_applied) - principle_balance
print('-----------------------')
print(
    f'Total Amount = \u20B9 {final_amt} \nCompound Interest = \u20B9 {compound_interest}')
print('-----------------------')
