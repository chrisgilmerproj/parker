

from .chords import Chord
from .scales import Major


class Progression(object):

    def __init__(self, scale):
        self.scale = Major(scale)

    def _get_chord(self, lookup, extension=''):
        """
        Get chord for progression from a lookup index number.

        The extension helps determine the format.
        """
        note = self.scale.notes[lookup]
        ch_str = '{}{}'.format(note.generalize(), extension)
        return Chord(ch_str)

    def I(self):
        return self._get_chord(0, 'M')

    def II(self):
        return self._get_chord(1, 'M')

    def III(self):
        return self._get_chord(2, 'M')

    def IV(self):
        return self._get_chord(3, 'M')

    def V(self):
        return self._get_chord(4, 'M')

    def VI(self):
        return self._get_chord(5, 'M')

    def VII(self):
        return self._get_chord(6, 'dim')

    def I7(self):
        return self._get_chord(0, 'M7')

    def II7(self):
        return self._get_chord(1, 'M7')

    def III7(self):
        return self._get_chord(2, 'M7')

    def IV7(self):
        return self._get_chord(3, 'M7')

    def V7(self):
        return self._get_chord(4, 'M7')

    def VI7(self):
        return self._get_chord(5, 'M7')

    def VII7(self):
        return self._get_chord(6, 'dim7')

    def i(self):
        return self._get_chord(0, 'm')

    def ii(self):
        return self._get_chord(1, 'm')

    def iii(self):
        return self._get_chord(2, 'm')

    def iv(self):
        return self._get_chord(3, 'm')

    def v(self):
        return self._get_chord(4, 'm')

    def vi(self):
        return self._get_chord(5, 'm')

    def vii(self):
        return self._get_chord(6, 'dim')

    def i7(self):
        return self._get_chord(0, 'm7')

    def ii7(self):
        return self._get_chord(1, 'm7')

    def iii7(self):
        return self._get_chord(2, 'm7')

    def iv7(self):
        return self._get_chord(3, 'm7')

    def v7(self):
        return self._get_chord(4, 'm7')

    def vi7(self):
        return self._get_chord(5, 'm7')

    def vii7(self):
        return self._get_chord(6, 'dim7')

    def standard_triads(self):
        return {'I': self.I(),
                'ii': self.ii(),
                'iii': self.iii(),
                'IV': self.IV(),
                'V': self.V(),
                'vi': self.vi(),
                'vii': self.vii(),
                }

    def standard_sevenths(self):
        return {'I7': self.I7(),
                'ii7': self.ii7(),
                'iii7': self.iii7(),
                'IV7': self.IV7(),
                'V7': self.V7(),
                'vi7': self.vi7(),
                'vii7': self.vii7(),
                }

    def all_progressions(self):
        return {'I': self.I(),
                'II': self.II(),
                'III': self.III(),
                'IV': self.IV(),
                'V': self.V(),
                'VI': self.VI(),
                'VII': self.VII(),
                'I7': self.I7(),
                'II7': self.II7(),
                'III7': self.III7(),
                'IV7': self.IV7(),
                'V7': self.V7(),
                'VI7': self.VI7(),
                'VII7': self.VII7(),
                'i': self.i(),
                'ii': self.ii(),
                'iii': self.iii(),
                'iv': self.iv(),
                'v': self.v(),
                'vi': self.vi(),
                'vii': self.vii(),
                'i7': self.i7(),
                'ii7': self.ii7(),
                'iii7': self.iii7(),
                'iv7': self.iv7(),
                'v7': self.v7(),
                'vi7': self.vi7(),
                'vii7': self.vii7(),
                }

    def from_string(self, progression):
        return getattr(self, progression)()

    def from_list(self, progression_list):
        return [self.from_string(prog) for prog in progression_list]
