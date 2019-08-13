import math

# finding the value from investment
def investment_value(investment, growth_rate, num_of_compounds, years):

    # converts growth rate to a decimal
    growth_rate = growth_rate/100

    # exponential function equation
    value = investment * (1 + growth_rate/num_of_compounds) ** (num_of_compounds * years)

    # rounds value to nearest cent
    value = round(value, 2)

    msg = "Your current investment value is now: $" + str(value)
    print(msg)


# finding investment compounded continuously
def continuous_investment_value(investment, growth_rate, years):

    # converts growth rate to a decimal
    growth_rate = growth_rate/100

    # continuous compounded function equation
    value = investment * math.e ** (growth_rate * years)

    # rounds value to nearest cent
    value = round(value, 2)

    msg = "Your continuous investment value is now: $" + str(value)
    print(msg)


# solving for inflation
def inflation_calculation(inflation_cost, growth_rate, years):

    # converts growth rate to a decimal
    growth_rate = growth_rate/100

    # continuous compounded function equation
    value = inflation_cost * (1 + growth_rate) ** years

    # rounds value to nearest cent
    value = round(value, 2)

    msg = "The inflation value is: $" + str(value)
    print(msg)



# finding the value from investment
investment_value(5100, 5.3, 1, 6.5)

# finding investment compounded continuously
continuous_investment_value(9600, 3.1, 4)

# solving for inflation
inflation_calculation(131500, 2.5, 14)