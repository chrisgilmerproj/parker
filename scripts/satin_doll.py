#! /usr/bin/python

from parker.progressions import Progression


PROGRESSIONS = [('D', ['ii7', 'V7', 'iii7', 'vi7']),
                ('D', ['II7', 'bII7', 'I7', 'IV7', 'iii7', 'vi7']),
                ('D', ['ii7', 'V7', 'iii7', 'vi7']),
                ('D', ['II7', 'bII7', 'I7', 'I7']),
                ('G', ['ii7', 'V7', 'I7', 'I7']),
                ('A', ['ii7', 'V7', 'v7', 'I7']),
                ('D', ['ii7', 'V7', 'iii7', 'vi7']),
                ('D', ['II7', 'bII7', 'I7', 'IV7', 'iii7', 'vi7']),
                ]


def main():
    last_ch_notes = set()
    last_sc_notes = set()
    for scale, phrase in PROGRESSIONS:
        p = Progression(scale)
        chord_list = p.from_list(phrase)
        print('-' * 80)
        print('Musical Phrase: {}'.format(phrase))
        print('Musical Chords: {}'.format([str(c) for c in chord_list]))
        print('-' * 80)
        print('')
        for ch in chord_list:
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

            print('{} - {}'.format(repr(ch), repr(sc)))
            print('Chord Notes: {}'.format(ch_notes))
            print('Common with last chord: {}'.format(common_notes_last_chord))
            print('Common with last scale: {}'.format(common_notes_last_scale))
            print('')


if __name__ == "__main__":
    main()
