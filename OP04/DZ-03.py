def bank(a, years):
    interest_rate = 0.10  # 10%
    total_amount = a

    for year in range(years):
        total_amount += total_amount * interest_rate

    return total_amount

initial_deposit = 1000
investment_years = 5
result = bank(initial_deposit, investment_years)
print(result)