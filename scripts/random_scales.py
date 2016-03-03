#! /usr/local/bin/python

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
