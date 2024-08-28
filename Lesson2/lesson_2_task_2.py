def is_year_leap(num):
    return num % 4 == 0
num = 2024
print(f'год:{num}:{is_year_leap(num)}')