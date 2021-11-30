# pgm4. Python Program for simple interest

principle_amount = int(input("Principle Amount : "))
interest_rate = int(input("Rate of Interest : "))
time_period = int(input("Time period : "))

Simple_interest = (principle_amount * interest_rate * time_period)/100

# '\u20B9' is unicode character for Indian Rupee Symbol
print("Simple_interest = \u20B9", Simple_interest)
