from random import randint
from random import shuffle


def get_one_number() -> int:
    """
    Get number from user
    :return: int
    """
    while True:
        try:
            number = int(input('enter a number: '))
            break
        except ValueError:
            print("It's not a number!")
    return number


def get_numbers():
    '''
    get from user 6 different numbers between 1 and 49
    :rtype: list
    :return: list
    '''
    result_list = []
    while len(result_list) < 6:
        number = get_one_number()
        if number in result_list:
            print('number already entered')
        elif 0 < number <= 49:
            result_list.append(number)
        else:
            print('number out of range 1 - 49!')
    return result_list


def show_numbers(numbers: list):
    '''
    Print given numbers as str
    :param numbers:
    :return: str
    '''
    print(", ".join(str(number) for number in sorted(numbers)))


def draw():
    numbers = list(range(1, 50))
    shuffle(numbers)
    return numbers[:6]


def final():
    '''
    main function
    '''
    user_numbers = get_numbers()
    print('Your numbers:')
    show_numbers(user_numbers)
    draw_ = draw()
    print('Lotto numbers:')
    show_numbers(draw_)
    hits = []
    for i in user_numbers:
        if i in draw_:
            hits += [i]
    show_numbers(hits)
    print(f'You have {len(hits)} hits')


final()
