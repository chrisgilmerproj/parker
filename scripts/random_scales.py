#! /usr/local/bin/python

"""
Random Scales

This exercise is to pick random scales to play.  The scales come from the
Circle of Fourths and Circle of Fifths.  It will provide you with a scale
and should you need the notes it will also print those out for you to see.
"""

import random

from parker.scales import circle_of_fifths
from parker.scales import circle_of_fourths


def print_scale(scale):
    print(scale.root.get_note_without_octave())
    raw_input('\nPress enter for notes\n')
    print([str(n.get_note_without_octave()) for n in scale.notes])
    raw_input('\nPress enter for next scale\n')


def main():
    fifths = circle_of_fifths()
    fourths = circle_of_fourths()
    circle = fifths + fourths
    print('\n')

    while True:
        random.shuffle(circle)
        for scale in circle:
            print_scale(scale)

        print('\n{}\n'.format('=' * 30))
        print('\nCONGRATS. Ready for more? Press enter.\n')
        print('\n{}\n'.format('=' * 30))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
