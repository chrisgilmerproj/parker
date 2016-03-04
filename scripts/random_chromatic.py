#! /usr/local/bin/python

"""
Random Chromatic

This exercise is to play a Chromatic scale starting at any note.
"""

from parker.scales import Chromatic


def main():
    scale = Chromatic('C')
    notes = scale.notes

    for note in notes:
        ch_notes = [n.generalize() for n in Chromatic(note).notes]
        raw_input('\n{}\n'.format(ch_notes))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
