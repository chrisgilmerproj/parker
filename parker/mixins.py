import copy

from .constants import SEMITONE_TO_INTERVAL


class CloneMixin(object):
    """Return a Clone or deepcopy of the object"""

    def clone(self):
        return copy.deepcopy(self)


class CommonEqualityMixin(object):

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)


class AugmentDiminishMixin(CloneMixin):

    def set_augment(self):
        raise NotImplementedError

    def augment(self):
        return self.clone().set_augment()

    def set_diminish(self):
        raise NotImplementedError

    def diminish(self):
        return self.clone().set_diminish()


class Aug(CommonEqualityMixin):
    """
    Augment the transpose amount by one.

    Example: For Aug(7) you would be asking to take the seventh and
             augment by 1 after it was transposed.
    """

    def __init__(self, transpose_amount):
        self.amount = transpose_amount

    def update(self, note):
        return note.set_augment()

    def __repr__(self):
        return "{}({})".format(type(self).__name__, str(self.amount))


class Dim(CommonEqualityMixin):
    """
    Diminish the transpose amount by one.

    Example: For Dim(7) you would be asking to take the seventh and
             diminish by 1 after it was transposed.
    """

    def __init__(self, transpose_amount):
        self.amount = transpose_amount

    def update(self, note):
        return note.set_diminish()

    def __repr__(self):
        return "{}({})".format(type(self).__name__, str(self.amount))


class NotesMixin(object):
    root = None

    def get_notes(self):
        raise NotImplementedError

    def lowest_note(self):
        return self.get_notes()[0]

    def highest_note(self):
        return self.get_notes()[-1]

    def walk(self, func):
        for n in self.get_notes():
            func(n)
        func(self.root)
        return self


class TransposeMixin(CloneMixin):

    def set_transpose(self, amount):
        raise NotImplementedError

    def transpose(self, amount):
        return self.clone().set_transpose(amount)

    def transpose_list(self, lst):
        return [self.transpose(amount) for amount in lst]

    # Transpose Up
    def minor_second_up(self):
        return self.transpose(1)

    def major_second_up(self):
        return self.transpose(2)

    def minor_third_up(self):
        return self.transpose(3)

    def major_third_up(self):
        return self.transpose(4)

    def major_fourth_up(self):
        return self.transpose(5)

    def perfect_fourth_up(self):
        return self.major_fourth_up()

    def minor_fifth_up(self):
        return self.transpose(6)

    def major_fifth_up(self):
        return self.transpose(7)

    def perfect_fifth_up(self):
        return self.major_fifth_up()

    def minor_sixth_up(self):
        return self.transpose(8)

    def major_sixth_up(self):
        return self.transpose(9)

    def minor_seventh_up(self):
        return self.transpose(10)

    def major_seventh_up(self):
        return self.transpose(11)

    def octave_up(self):
        return self.transpose(12)

    def minor_ninth_up(self):
        return self.transpose(13)

    def compound_minor_second_up(self):
        return self.minor_ninth_up()

    def major_ninth_up(self):
        return self.transpose(14)

    def compound_major_second_up(self):
        return self.major_ninth_up()

    def augmented_ninth_up(self):
        return self.transpose(15)

    def minor_tenth_up(self):
        return self.augmented_ninth_up()

    def compound_augmented_second_up(self):
        return self.augmented_ninth_up()

    def compound_minor_third_up(self):
        return self.augmented_ninth_up()

    def major_tenth_up(self):
        return self.transpose(16)

    def compound_major_third_up(self):
        return self.major_tenth_up()

    def major_eleventh_up(self):
        return self.transpose(17)

    def compound_perfect_fourth_up(self):
        return self.major_eleventh_up()

    def augmented_eleventh_up(self):
        return self.transpose(18)

    def compound_augmented_fourth_up(self):
        return self.augmented_eleventh_up()

    def minor_thirteenth_up(self):
        return self.transpose(20)

    def compound_minor_sixth_up(self):
        return self.minor_thirteenth_up()

    def major_thirteenth_up(self):
        return self.transpose(21)

    def compound_major_sixth_up(self):
        return self.major_thirteenth_up()

    # Transpose Down
    def minor_second_down(self):
        return self.transpose(-1)

    def major_second_down(self):
        return self.transpose(-2)

    def minor_third_down(self):
        return self.transpose(-3)

    def major_third_down(self):
        return self.transpose(-4)

    def major_fourth_down(self):
        return self.transpose(-5)

    def perfect_fourth_down(self):
        return self.major_fourth_down()

    def minor_fifth_down(self):
        return self.transpose(-6)

    def major_fifth_down(self):
        return self.transpose(-7)

    def perfect_fifth_down(self):
        return self.major_fifth_down()

    def minor_sixth_down(self):
        return self.transpose(-8)

    def major_sixth_down(self):
        return self.transpose(-9)

    def minor_seventh_down(self):
        return self.transpose(-10)

    def major_seventh_down(self):
        return self.transpose(-11)

    def octave_down(self):
        return self.transpose(-12)

    def minor_ninth_down(self):
        return self.transpose(-13)

    def compound_minor_second_down(self):
        return self.minor_ninth_down()

    def major_ninth_down(self):
        return self.transpose(-14)

    def compound_major_second_down(self):
        return self.major_ninth_down()

    def augmented_ninth_down(self):
        return self.transpose(-15)

    def minor_tenth_down(self):
        return self.augmented_ninth_down()

    def compound_augmented_second_down(self):
        return self.augmented_ninth_down()

    def compound_minor_third_down(self):
        return self.augmented_ninth_down()

    def major_tenth_down(self):
        return self.transpose(-16)

    def compound_major_third_down(self):
        return self.major_tenth_down()

    def major_eleventh_down(self):
        return self.transpose(-17)

    def compound_perfect_fourth_down(self):
        return self.major_eleventh_down()

    def augmented_eleventh_down(self):
        return self.transpose(-18)

    def compound_augmented_fourth_down(self):
        return self.augmented_eleventh_down()

    def minor_thirteenth_down(self):
        return self.transpose(-20)

    def compound_minor_sixth_down(self):
        return self.minor_thirteenth_down()

    def major_thirteenth_down(self):
        return self.transpose(-21)

    def compound_major_sixth_down(self):
        return self.major_thirteenth_down()

    def all_transpositions(self):
        """
        Create all available named transpositions
        """
        return {
            'minor_second_up': self.transpose(1),
            'major_second_up': self.transpose(2),
            'minor_third_up': self.transpose(3),
            'major_third_up': self.transpose(4),
            'major_fourth_up': self.transpose(5),
            'perfect_fourth_up': self.major_fourth_up(),
            'minor_fifth_up': self.transpose(6),
            'major_fifth_up': self.transpose(7),
            'perfect_fifth_up': self.major_fifth_up(),
            'minor_sixth_up': self.transpose(8),
            'major_sixth_up': self.transpose(9),
            'minor_seventh_up': self.transpose(10),
            'major_seventh_up': self.transpose(11),
            'octave_up': self.transpose(12),
            'minor_ninth_up': self.transpose(13),
            'compound_minor_second_up': self.minor_ninth_up(),
            'major_ninth_up': self.transpose(14),
            'compound_major_second_up': self.major_ninth_up(),
            'augmented_ninth_up': self.transpose(15),
            'minor_tenth_up': self.augmented_ninth_up(),
            'compound_augmented_second_up': self.augmented_ninth_up(),
            'compound_minor_third_up': self.augmented_ninth_up(),
            'major_tenth_up': self.transpose(16),
            'compound_major_third_up': self.major_tenth_up(),
            'major_eleventh_up': self.transpose(17),
            'compound_perfect_fourth_up': self.major_eleventh_up(),
            'augmented_eleventh_up': self.transpose(18),
            'compound_augmented_fourth_up': self.augmented_eleventh_up(),
            'minor_thirteenth_up': self.transpose(20),
            'compound_minor_sixth_up': self.minor_thirteenth_up(),
            'major_thirteenth_up': self.transpose(21),
            'compound_major_sixth_up': self.major_thirteenth_up(),
            'minor_second_down': self.transpose(-1),
            'major_second_down': self.transpose(-2),
            'minor_third_down': self.transpose(-3),
            'major_third_down': self.transpose(-4),
            'major_fourth_down': self.transpose(-5),
            'perfect_fourth_down': self.major_fourth_down(),
            'minor_fifth_down': self.transpose(-6),
            'major_fifth_down': self.transpose(-7),
            'perfect_fifth_down': self.major_fifth_down(),
            'minor_sixth_down': self.transpose(-8),
            'major_sixth_down': self.transpose(-9),
            'minor_seventh_down': self.transpose(-10),
            'major_seventh_down': self.transpose(-11),
            'octave_down': self.transpose(-12),
            'minor_ninth_down': self.transpose(-13),
            'compound_minor_second_down': self.minor_ninth_down(),
            'major_ninth_down': self.transpose(-14),
            'compound_major_second_down': self.major_ninth_down(),
            'augmented_ninth_down': self.transpose(-15),
            'minor_tenth_down': self.augmented_ninth_down(),
            'compound_augmented_second_down': self.augmented_ninth_down(),
            'compound_minor_third_down': self.augmented_ninth_down(),
            'major_tenth_down': self.transpose(-16),
            'compound_major_third_down': self.major_tenth_down(),
            'major_eleventh_down': self.transpose(-17),
            'compound_perfect_fourth_down': self.major_eleventh_down(),
            'augmented_eleventh_down': self.transpose(-18),
            'compound_augmented_fourth_down': self.augmented_eleventh_down(),
            'minor_thirteenth_down': self.transpose(-20),
            'compound_minor_sixth_down': self.minor_thirteenth_down(),
            'major_thirteenth_down': self.transpose(-21),
            'compound_major_sixth_down': self.major_thirteenth_down(),
        }


class OctaveMixin(object):
    """Translate Semitones to Octave"""

    def get_octave_construction(self):
        return [SEMITONE_TO_INTERVAL[i] for i in self.intervals]
