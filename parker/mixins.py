

class AugmentDiminishMixin(object):

    def set_augment(self):
        pass

    def augment(self):
        return self.clone().set_augment()

    def set_diminish(self):
        pass

    def diminish(self):
        return self.clone().set_diminish()


class TransposeMixin(object):

    def set_transpose(self, amount):
        return self

    def transpose(self, amount):
        return self.clone().set_transpose(amount)

    def transpose_list(self, lst):
        return [ self.transpose(amount) for amount in lst ]
    
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

    # MUTABLE TRANPOSE UP
    def set_minor_second_up(self):
        return self.set_transpose(1)

    def set_major_second_up(self):
        return self.set_transpose(2)

    def set_minor_third_up(self):
        return self.set_transpose(3)

    def set_major_third_up(self):
        return self.set_transpose(4)

    def set_major_fourth_up(self):
        return self.set_transpose(5)

    def set_perfect_fourth_up(self):
        return self.set_major_fourth_up()

    def set_minor_fifth_up(self):
        return self.set_transpose(6)

    def set_major_fifth_up(self):
        return self.set_transpose(7)

    def set_perfect_fifth_up(self):
        return self.set_major_fifth_up()

    def set_minor_sixth_up(self):
        return self.set_transpose(8)

    def set_major_sixth_up(self):
        return self.set_transpose(9)

    def set_minor_seventh_up(self):
        return self.set_transpose(10)

    def set_major_seventh_up(self):
        return self.set_transpose(11)

    def set_octave_up(self):
        return self.set_transpose(12)

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

    # MUTABLE TRANPOSE DOWN
    def set_minor_second_down(self):
        return self.set_transpose(-1)

    def set_major_second_down(self):
        return self.set_transpose(-2)

    def set_minor_third_down(self):
        return self.set_transpose(-3)

    def set_major_third_down(self):
        return self.set_transpose(-4)

    def set_major_fourth_down(self):
        return self.set_transpose(-5)

    def set_perfect_fourth_down(self):
        return self.set_major_fourth_down()

    def set_minor_fifth_down(self):
        return self.set_transpose(-6)

    def set_major_fifth_down(self):
        return self.set_transpose(-7)

    def set_perfect_fifth_down(self):
        return self.set_major_fifth_down()

    def set_minor_sixth_down(self):
        return self.set_transpose(-8)

    def set_major_sixth_down(self):
        return self.set_transpose(-9)

    def set_minor_seventh_down(self):
        return self.set_transpose(-10)

    def set_major_seventh_down(self):
        return self.set_transpose(-11)

    def set_octave_down(self):
        return self.set_transpose(-12)
