#! /usr/bin/python

from parker.chords import Chord


CHANGES = [['Em7', 'A7', 'F#m7', 'B7'],
           ['E7', 'Eb7', 'DM7', 'G7', 'F#m7', 'B7'],
           ['Em7', 'A7', 'F#m7', 'B7'],
           ['E7', 'Eb7', 'DM7', 'DM7'],
           ['Am7', 'D7', 'GM7', 'GM7'],
           ['Bm7', 'E7', 'Em7', 'A7'],
           ['Em7', 'A7', 'F#m7', 'B7'],
           ['E7', 'Eb7', 'DM7', 'G7', 'F#m7', 'B7'],
           ]

PROGRESSIONS = []


def main():
    last_ch_notes = set()
    last_sc_notes = set()
    for phrase in CHANGES:
        print('-' * 80)
        print('Musical Phrase: {}'.format(phrase))
        print('-' * 80)
        print('')
        for chord in phrase:
            ch = Chord(chord)
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
