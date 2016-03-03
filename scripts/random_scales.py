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


def main():
    fifths = circle_of_fifths()
    fourths = circle_of_fourths()
    circle = fifths + fourths
    print('\n')

    while True:
        scale = random.choice(circle)
        print(scale.root.get_note_without_octave())
        raw_input('\nPress enter for notes\n')
        print([str(n.get_note_without_octave()) for n in scale.notes])
        raw_input('\nPress enter for next scale\n')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
