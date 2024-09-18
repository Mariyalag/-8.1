
def add_everything_up(a, b):
    try:
        return str(round(a + b, 2))
    except TypeError:
        if isinstance(a, (int, float)) and isinstance(b, str):
            return str(a) + b
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return a + str(b)
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        #     return str(a) + str(b)
        # else:
        #     return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


# try:
#     i = 0
#     print(10 / i)
#     print('сделано')
# except ZeroDivisionError:
#     print('нельзя делить на ноль!')

# try:
#     truba = a + b
#     truba = 10/0
# except (ZeroDivisionError, NameError):
#     print('что-то пошло не так, но мы устояли')

# try:
#     a = 10/0
# except ZeroDivisionError as exc:
#     print('что-то пошло не так - {exc} но мы устояли')