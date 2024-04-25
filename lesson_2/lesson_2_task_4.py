### Первый вариант
# def fizz_buzz(x):
#     for n in list(range(1, x + 1)):
#         if n % 3 == 0 and n % 5 == 0:
#             print(f"{n} FizzBuzz")
#         elif n % 3 == 0:
#             print(f"{n} Fizz")
#         elif n % 5 == 0:
#             print(f"{n} Buzz")
#         else:
#             print(n)
#
# fizz_buzz(17)

### Второй вариант
def fizz_buzz(x):
    for n in list(range(1, x + 1)):
        str = ""
        if n % 3 == 0:
            str = str + "fizz"
        if n % 5 == 0:
            str = str + "buzz"
        if not str:
            print(n)
        else:
            print(str)
fizz_buzz(17)