#! /usr/local/bin/python

"""
Random Scales

This exercise is to pick random scales to play.  The scales come from the
Circle of Fourths and Circle of Fifths.  It will provide you with a scale
and should you need the notes it will also print those out for you to see.
"""

import random

from parker.scales import dorian_scales
from parker.scales import major_scales
from parker.scales import mixolydian_scales


def print_scale(scale):
    print(repr(scale))
    raw_input('')
    print([str(n.normalize()) for n in scale.notes])
    raw_input('')


def main():
    print('\n')

    scales = zip(major_scales(),
                 mixolydian_scales(),
                 dorian_scales())
    while True:
        random.shuffle(scales)
        for major, mixolydian, dorian in scales:
            print_scale(major)
            print_scale(mixolydian)
            print_scale(dorian)
            print('{}'.format('=' * 30))
            print('Press enter for next scale')
            print('{}'.format('=' * 30))
            raw_input('')

        print('\n{}\n'.format('=' * 30))
        print('\nCONGRATS. Ready for more? Press enter.\n')
        print('\n{}\n'.format('=' * 30))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
