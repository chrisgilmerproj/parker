#! /usr/local/bin/python

"""
Random Intervals

This exercise is to determine the interval above the given note.  You
will be presented with a scale and asked to give the interval of that note
to continue.
"""

import random

from parker.notes import Note
from parker.scales import circle_of_fifths
from parker.scales import circle_of_fourths

DIRECTIONS = [
    'up',
    # 'down',
]

INTERVALS = [
    # 'minor_second',
    # 'major_second',
    # 'minor_third',
    'major_third',
    # 'major_fourth',
    'perfect_fifth',
    # 'minor_sixth',
    # 'major_sixth',
    # 'minor_seventh',
    'major_seventh',
    # 'octave',
    # 'minor_ninth',
    'major_ninth',
    # 'minor_tenth',
    # 'major_tenth',
    'major_eleventh',
    # 'minor_thirteenth',
    'major_thirteenth',
]


def print_scale(scale):
    print("=" * 50)
    print("This exercise is for the scale: {}".format(scale))
    print("=" * 50)
    # random.shuffle(INTERVALS)
    for interval in INTERVALS:
        direction = random.choice(DIRECTIONS)
        interval_name = ' '.join(interval.split('_'))
        fn_name = '{}_{}'.format(interval, direction)
        new_note = getattr(scale.root, fn_name)()

        ans = raw_input('\nWhat is the {} {} from {}?\n\n'.format(
                        interval_name,
                        direction,
                        scale))

        try:
            n_ans = Note(ans).get_note_without_octave()
        except Exception:
            n_ans = ans
        if n_ans == str(new_note.get_note_without_octave()):
            print('Correct!\n')
        else:
            print('Incorrect! You wanted {}\n'.format(new_note))


def main():
    NUM_SCALES = 3

    fifths = circle_of_fifths()
    fourths = circle_of_fourths()

    circle = fifths + fourths
    circle = circle[:NUM_SCALES]

    while True:
        random.shuffle(circle)
        for scale in circle:
            print_scale(scale)

        print('{}'.format('=' * 30))
        print('{}'.format('=' * 30))
        print('CONGRATS. Ready for more? Press enter.')
        print('{}'.format('=' * 30))
        print('{}'.format('=' * 30))
        print('\n')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
