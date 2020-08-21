from random import sample


class DryError(Exception):
    pass


class OtherThanSixError(Exception):
    pass


class OutOfBoundsError(Exception):
    pass


def get_number():
    """Get 6 different numbers between 1 and 49.

    :rtype: list
    :return: list with 6 sorted numbers provide by user
    """
    while True:
        welcome = 'Check Lotto numbers, separate numbers with spaces: '
        user_input = input(welcome).split()
        try:
            user_input = [int(i) for i in user_input]
            if len(set(user_input)) != len(user_input):
                raise DryError
            if len(user_input) != 6:
                raise OtherThanSixError
            for n in user_input:
                if n not in range(1, 50):
                    raise OutOfBoundsError
        except ValueError:
            print("Enter your numbers as numerals, try again")
            continue
        except DryError:
            print("Don't repeat yourself, try again")
            continue
        except OtherThanSixError:
            print("Enter exactly 6 numbers, try again")
            continue
        except OutOfBoundsError:
            print("Each number must be in the range 1 to 49!")
            continue
        user_input.sort()
        return user_input


def drawing_numbers():
    """ Draws 6 unique, random numbers.

    :rtype list
    :return: sorted list with 6 random numbers
    """
    drawn_nums = sample((range(1, 50)), 6)
    drawn_nums.sort()
    return drawn_nums


def lotto():
    """Main function of the program"""
    user_nums = get_number()
    rnd_nums = drawing_numbers()
    print('You entered:', ' '.join(str(i) for i in user_nums))
    print('Lotto results:', ' '.join(str(i) for i in rnd_nums))
    hit = len(set(user_nums) & set(rnd_nums))
    if hit >= 3:
        print('You won!, hit {} numbers'.format(hit))
    else:
        print('You lost, hit {} numbers'.format(hit))


if __name__ == '__main__':
    lotto()
