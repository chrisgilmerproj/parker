#! /usr/bin/python

from parker.progressions import Progression
from parker.scales import Major


# The Key is what needs to be changed to change everything in the song
# Progressions are tuples where the first half of the tuple is the distance
# from the main Key where 1 is ionic and the second half of the tuple is
# the phrase with the chord progressions.
KEY = 'D'
PROGRESSIONS = [(1, ['ii7', 'V7', 'iii7', 'vi7']),
                (1, ['II7', 'bII7', 'I7', 'IV7', 'iii7', 'vi7']),
                (1, ['ii7', 'V7', 'iii7', 'vi7']),
                (1, ['II7', 'bII7', 'I7', 'I7']),
                (4, ['ii7', 'V7', 'I7', 'I7']),
                (5, ['ii7', 'V7', 'v7', 'I7']),
                (1, ['ii7', 'V7', 'iii7', 'vi7']),
                (1, ['II7', 'bII7', 'I7', 'IV7', 'iii7', 'vi7']),
                ]


def main():
    last_ch_notes = set()
    last_sc_notes = set()
    song_key = Major(KEY)
    for scale_int, phrase in PROGRESSIONS:
        scale = song_key.notes[scale_int - 1]
        p = Progression(scale)
        chord_list = p.from_list(phrase)
        print('-' * 80)
        print('Musical Key: {}'.format(scale))
        print('Musical Phrase: {}'.format(phrase))
        print('Musical Chords: {}'.format([str(c) for c in chord_list]))
        print('-' * 80)
        print('')
        for prog, ch in zip(phrase, chord_list):
            ch_notes = [n.normalize() for n in ch.notes]
            sc = ch.get_scale()

            # Find notes common to the previous phrase
            ch_notes = [n.normalize(use_sharps=True) for n in ch.notes]
            sc_notes = [n.normalize(use_sharps=True) for n in sc.notes]
            common_notes_last_chord = list(set(ch_notes) & last_ch_notes)
            common_notes_last_chord.sort()
            common_notes_last_scale = list(set(sc_notes) & last_sc_notes)
            common_notes_last_scale.sort()
            last_ch_notes = set(ch_notes)
            last_sc_notes = set(sc_notes)

            print('{}'.format(prog))
            print('{}: {}'.format(repr(ch), ch_notes))
            print('{}: {}'.format(repr(sc), sc_notes))
            print('Common with last chord: {}'.format(common_notes_last_chord))
            print('Common with last scale: {}'.format(common_notes_last_scale))
            print('')


if __name__ == "__main__":
    main()
