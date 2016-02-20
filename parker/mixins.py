import copy


class AugmentDiminishMixin(object):

    def set_augment(self):
        pass

    def augment(self):
        return self.clone().set_augment()

    def set_diminish(self):
        pass

    def diminish(self):
        return self.clone().set_diminish()


class CloneMixin(object):
    def clone(self):
        return copy.deepcopy(self)


class NotesMixin(object):

    def get_notes(self):
        return []

    def set_change_duration(self, duration):
        return self

    def change_duration(self, duration):
        return self.clone().set_change_duration(duration)

    def lowest_note(self):
        return self.get_notes()[0]

    def highest_note(self):
        return self.get_notes()[-1]

    def walk(self, func):
        for n in self.get_notes():
            func(n)
        return self


class TransposeMixin(object):

    def set_transpose(self, amount):
        return self

    def transpose(self, amount):
        return self.clone().set_transpose(amount)

    def transpose_list(self, lst):
        return [self.transpose(amount) for amount in lst]

    # IMMUTABLE TRANSPOSE UP
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

    # IMMUTABLE TRANSPOSE DOWN
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
