
### Первый вариант
# def is_year_leap(n):
#
#     if n % 4 == 0:
#         print(f"Год {n}: True")
#     else:
#         print(f"Год {n}: False")
#
# is_year_leap(2023)

### Второй вариант
def is_year_leap(n):

    print(f"Год {n}: {n % 4 == 0}")

is_year_leap(2024)