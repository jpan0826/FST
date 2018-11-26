# Ju Pan

from fst import FST
import string, sys


def letters_to_numbers():
    """
	Returns an FST that converts letters to numbers as specified by
	the soundex algorithm
	"""

    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.add_state('next')
    f1.add_state('1')
    f1.add_state('2')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.initial_state = 'start'

    # Set all the final states
    f1.set_final('next')
    f1.set_final('1')
    f1.set_final('2')
    f1.set_final('3')
    f1.set_final('4')
    f1.set_final('5')
    f1.set_final('6')

    for letter in string.ascii_lowercase:
        f1.add_arc('start', 'next', letter, letter)

        if letter in ['a', 'e', 'h', 'i', 'o', 'u', 'w', 'y']:
            f1.add_arc('next', 'next', letter, '')
            f1.add_arc('1', 'next', letter, '')
            f1.add_arc('2', 'next', letter, '')
            f1.add_arc('3', 'next', letter, '')
            f1.add_arc('4', 'next', letter, '')
            f1.add_arc('5', 'next', letter, '')
            f1.add_arc('6', 'next', letter, '')

        elif letter in ['b', 'f', 'p', 'v']:
            f1.add_arc('next', '1', letter, '1')
            f1.add_arc('1', '1', letter, '')
            f1.add_arc('2', '1', letter, '1')
            f1.add_arc('3', '1', letter, '1')
            f1.add_arc('4', '1', letter, '1')
            f1.add_arc('5', '1', letter, '1')
            f1.add_arc('6', '1', letter, '1')

        elif letter in ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']:
            f1.add_arc('next', '2', letter, '2')
            f1.add_arc('2', '2', letter, '')
            f1.add_arc('1', '2', letter, '2')
            f1.add_arc('3', '2', letter, '2')
            f1.add_arc('4', '2', letter, '2')
            f1.add_arc('5', '2', letter, '2')
            f1.add_arc('6', '2', letter, '2')

        elif letter in ['d', 't']:
            f1.add_arc('next', '3', letter, '3')
            f1.add_arc('3', '3', letter, '')
            f1.add_arc('1', '3', letter, '3')
            f1.add_arc('2', '3', letter, '3')
            f1.add_arc('4', '3', letter, '3')
            f1.add_arc('5', '3', letter, '3')
            f1.add_arc('6', '3', letter, '3')

        elif letter in ['l']:
            f1.add_arc('next', '4', letter, '4')
            f1.add_arc('4', '4', letter, '')
            f1.add_arc('1', '4', letter, '4')
            f1.add_arc('2', '4', letter, '4')
            f1.add_arc('3', '4', letter, '4')
            f1.add_arc('5', '4', letter, '4')
            f1.add_arc('6', '4', letter, '4')


        elif letter in ['m', 'n']:
            f1.add_arc('next', '5', letter, '5')
            f1.add_arc('5', '5', letter, '')
            f1.add_arc('1', '5', letter, '5')
            f1.add_arc('2', '5', letter, '5')
            f1.add_arc('3', '5', letter, '5')
            f1.add_arc('4', '5', letter, '5')
            f1.add_arc('6', '5', letter, '5')

        else:
            f1.add_arc('next', '6', letter, '6')
            f1.add_arc('6', '6', letter, '')
            f1.add_arc('1', '6', letter, '6')
            f1.add_arc('2', '6', letter, '6')
            f1.add_arc('3', '6', letter, '6')
            f1.add_arc('4', '6', letter, '6')
            f1.add_arc('5', '6', letter, '6')

    return f1


def truncate_to_three_digits():
    """
	Create an FST that will truncate a soundex string to three digits
	"""

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    f2.add_state('5')
    f2.initial_state = '1'
    f2.set_final('5')
    f2.set_final('4')
    f2.set_final('3')

    for letter in string.ascii_letters:
        f2.add_arc('1', '2', letter, letter)
    for num in string.digits:
        f2.add_arc('1', '3', num, num)
        f2.add_arc('2', '3', num, num)
        f2.add_arc('3', '4', num, num)
        f2.add_arc('4', '5', num, num)
        f2.add_arc('5', '5', num, '')

    return f2


def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('2')
    f3.add_state('3')
    f3.add_state('4')
    f3.add_state('5')
    f3.add_state('6')
    f3.add_state('7')
    f3.add_state('8')

    f3.initial_state = '1'
    f3.set_final('5')
    f3.set_final('8')

    for letter in string.ascii_letters:
        f3.add_arc('1', '2', letter, letter)

    for num in string.digits:
        f3.add_arc('1', '3', num, num)
        f3.add_arc('2', '3', num, num)
        f3.add_arc('3', '4', num, num)
        f3.add_arc('4', '5', num, num)

    f3.add_arc('2', '6', '', '0')
    f3.add_arc('3', '7', '', '0')
    f3.add_arc('4', '8', '', '0')
    f3.add_arc('6', '7', '', '0')
    f3.add_arc('7', '8', '', '0')

    return f3


def soundex_convert(name_string):
    """Combine the three FSTs above and use it to convert a name into a Soundex"""

    from fsmutils import compose
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()
    output = compose(name_string, f1, f2, f3)
    return ''.join(output[0])

    #pass

if __name__ == '__main__':

    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, soundex_convert(tuple(user_input))))

    f1.transduce(user_input)
