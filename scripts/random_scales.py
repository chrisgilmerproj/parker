#! /usr/local/bin/python

"""
Random Scales

This exercise is to pick random scales to play.  The scales come from the
Circle of Fourths and Circle of Fifths.  It will provide you with a scale
and should you need the notes it will also print those out for you to see.
"""

import argparse
import random

from parker.scales import dorian_scales
from parker.scales import major_scales
from parker.scales import minor_scales
from parker.scales import minor_blues_scales
from parker.scales import minor_pentatonic_scales
from parker.scales import mixolydian_scales


def print_scale(scale):
    print(repr(scale))
    raw_input('')
    print([str(n.normalize()) for n in scale.notes])
    raw_input('')


def main(args):
    print('\n')

    major_scale_list = zip(major_scales(),
                           mixolydian_scales(),
                           dorian_scales())

    minor_scale_list = zip(minor_scales(),
                           minor_pentatonic_scales(),
                           minor_blues_scales())

    scale_list = None
    if args.major:
        scale_list = major_scale_list
    elif args.minor:
        scale_list = minor_scale_list

    if scale_list is None:
        scale_list = major_scale_list

    while True:
        random.shuffle(scale_list)
        for scales in scale_list:
            for scale in scales:
                print_scale(scale)
            print('{}'.format('=' * 30))
            print('Press enter for next scale')
            print('{}'.format('=' * 30))
            raw_input('')

        print('{}'.format('=' * 30))
        print('CONGRATS. Ready for more? Press enter.')
        print('{}'.format('=' * 30))
        raw_input('')


if __name__ == "__main__":
    description = 'Practice Major or Minor Scale Sets.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-M', '--major', action='store_true',
                        help='play with major scales')
    parser.add_argument('-m', '--minor', action='store_true',
                        help='play with minor scales')
    args = parser.parse_args()

    try:
        main(args)
    except KeyboardInterrupt:
        pass
