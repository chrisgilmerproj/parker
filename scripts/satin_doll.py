#! /usr/bin/python

from parker.chords import Chord
from parker.scales import Dorian
from parker.scales import Ionian
from parker.scales import Mixolydian


CHANGES = [['Em7', 'A7', 'F#m7', 'B7'],
           ['E7', 'Eb7', 'DM7', 'G7', 'F#m7', 'B7'],
           ['Em7', 'A7', 'F#m7', 'B7'],
           ['E7', 'Eb7', 'DM7', 'DM7'],
           ['Am7', 'D7', 'GM7', 'GM7'],
           ['Bm7', 'E7', 'Em7', 'A7'],
           ['Em7', 'A7', 'F#m7', 'B7'],
           ['E7', 'Eb7', 'DM7', 'G7', 'F#m7', 'B7'],
           ]


def main():
    last_notes = set()
    for phrase in CHANGES:
        print(phrase)
        print('')
        for chord in phrase:
            print(chord)
            ch = Chord(chord)
            ch_notes = [n.normalize() for n in ch.notes]
            print(ch_notes)
            print(ch.get_octave_construction())
            ch_cls = Ionian
            if 'm7' == chord[1:]:
                ch_cls = Dorian
            elif 'M7' == chord[1:]:
                ch_cls = Ionian
            elif '7' == chord[1:]:
                ch_cls = Mixolydian
            sc = ch_cls(ch.root)
            print(ch_cls.__name__)
            # print(sc.notes)

            # Find notes common to the previous phrase
            gen_notes = [n.normalize() for n in sc.notes]
            print(sorted(list(set(gen_notes) & last_notes)))
            print(sorted(list(set(gen_notes) & set(ch_notes))))
            last_notes = set(gen_notes)
            print('')
        print('')


if __name__ == "__main__":
    main()
