class ThisIsNotAnExampleException(Exception):
    pass

class TooLongExampleException(Exception):
    pass

class UnacceptableValueException(Exception):
    pass

class NotAnIntegerException(Exception):
    pass

class UnacceptableOperationException(Exception):
    pass


def make_separation(example):
    """Возвращает список элементов примера"""

    if len(example) == 3: return [i for i in example]
    else: return example.split()


def check_exceptions(list_of_example):
    """проверяет на наличие исключений из ТЗ"""
    
    if len(list_of_example) == 1: 
        raise ThisIsNotAnExampleException('Вы ввели число, а не пример')
    if len(list_of_example) > 3:
        raise TooLongExampleException('Вы ввели пример больше, чем из двух чисел')
    if (int(list_of_example[0]) > 10 or int(list_of_example[0]) < 1) or (int(list_of_example[2]) > 10 or int(list_of_example[2]) < 1):
        raise UnacceptableValueException('Одно из чисел больше 10 или меньше 1')
    try:
        int(list_of_example[0])
        int(list_of_example[2])
    except ValueError:
        raise NotAnIntegerException('Одно из чисел не является целым числом')
    if list_of_example[1] not in ('+','-','*','/'):	
        raise UnacceptableOperationException(f'Операция "{list_of_example[1]}" невозможна')


def figure_out(list_of_example):
    """Вычисляет результат примера"""

    if list_of_example[1] == '+': return int(list_of_example[0]) + int(list_of_example[2])
    elif list_of_example[1] == '-': return int(list_of_example[0]) - int(list_of_example[2])
    elif list_of_example[1] == '*': return int(list_of_example[0]) * int(list_of_example[2])
    elif list_of_example[1] == '/': return int(list_of_example[0]) // int(list_of_example[2])


def main(example = input('Введите пример: ')):
    list_of_example = make_separation(example)
    check_exceptions(list_of_example)
    print(f'Ответ: {figure_out(list_of_example)}')
    return figure_out(list_of_example)


if __name__ == '__main__':
    main()