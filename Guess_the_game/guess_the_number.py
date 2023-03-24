from random import randint


def get_number() -> int:
    """
    Get number from user,
    try until the user enter a valid value
    :rtype: int
    :return: int
    """
    while True:
        try:
            guess = int(input('Guess the number: '))
            return guess
        except ValueError:
            print("It's not a number!")


def guess_number():
    """
    check if the given number is equal to the number drawn
    until the given number is equal to the number drawn
    :rtype: int
    :return: int
    """
    draw = randint(1, 100)
    guess = None
    while guess != draw:
        guess = get_number()
        if guess < draw:
            print('Too small!')
        elif guess > draw:
            print('Too big!')
    print('You win!')


guess_number()
