def bank(sum_vklad, years):
    amount = sum_vklad
    interest_rate = 0.10

    for year in range(years):
        amount += amount * interest_rate
    
    return round(amount, 2)


sum_vklad = 1000 
years = 5   
result = bank(sum_vklad , years)
print(result)