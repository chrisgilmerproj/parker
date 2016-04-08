

from .chords import Chord
from .scales import Major


class Progression(object):

    def __init__(self, scale):
        self.scale = Major(scale)

    def _get_chord(self, lookup, extension='', flat=False):
        """
        Get chord for progression from a lookup index number.

        The extension helps determine the format.
        """
        note = self.scale.notes[lookup]
        if flat:
            note.set_diminish()
        ch_str = '{}{}'.format(note.generalize(), extension)
        return Chord(ch_str)

    def I(self, flat=False):
        return self._get_chord(0, 'M', flat=flat)

    def II(self, flat=False):
        return self._get_chord(1, 'M', flat=flat)

    def III(self, flat=False):
        return self._get_chord(2, 'M', flat=flat)

    def IV(self, flat=False):
        return self._get_chord(3, 'M', flat=flat)

    def V(self, flat=False):
        return self._get_chord(4, 'M', flat=flat)

    def VI(self, flat=False):
        return self._get_chord(5, 'M', flat=flat)

    def VII(self, flat=False):
        return self._get_chord(6, 'dim', flat=flat)

    def I7(self, flat=False):
        return self._get_chord(0, 'M7', flat=flat)

    def II7(self, flat=False):
        return self._get_chord(1, 'M7', flat=flat)

    def III7(self, flat=False):
        return self._get_chord(2, 'M7', flat=flat)

    def IV7(self, flat=False):
        return self._get_chord(3, 'M7', flat=flat)

    def V7(self, flat=False):
        return self._get_chord(4, 'M7', flat=flat)

    def VI7(self, flat=False):
        return self._get_chord(5, 'M7', flat=flat)

    def VII7(self, flat=False):
        return self._get_chord(6, 'dim7', flat=flat)

    def i(self, flat=False):
        return self._get_chord(0, 'm', flat=flat)

    def ii(self, flat=False):
        return self._get_chord(1, 'm', flat=flat)

    def iii(self, flat=False):
        return self._get_chord(2, 'm', flat=flat)

    def iv(self, flat=False):
        return self._get_chord(3, 'm', flat=flat)

    def v(self, flat=False):
        return self._get_chord(4, 'm', flat=flat)

    def vi(self, flat=False):
        return self._get_chord(5, 'm', flat=flat)

    def vii(self, flat=False):
        return self._get_chord(6, 'dim', flat=flat)

    def i7(self, flat=False):
        return self._get_chord(0, 'm7', flat=flat)

    def ii7(self, flat=False):
        return self._get_chord(1, 'm7', flat=flat)

    def iii7(self, flat=False):
        return self._get_chord(2, 'm7', flat=flat)

    def iv7(self, flat=False):
        return self._get_chord(3, 'm7', flat=flat)

    def v7(self, flat=False):
        return self._get_chord(4, 'm7', flat=flat)

    def vi7(self, flat=False):
        return self._get_chord(5, 'm7', flat=flat)

    def vii7(self, flat=False):
        return self._get_chord(6, 'dim7', flat=flat)

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
        flat = False
        if progression.startswith('b'):
            flat = True
            progression = progression[1:]
        return getattr(self, progression)(flat=flat)

    def from_list(self, progression_list):
        return [self.from_string(prog) for prog in progression_list]
