# Домашнее задание по уроку "Try и Except".
# Задание "Программистам всё можно"

def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:  # as tper:
        return str(a) + str(b)
    # finally:
    #     print('сложили числа и строки')


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
