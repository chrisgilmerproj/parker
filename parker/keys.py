
ORDER_OF_FLATS = ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb']
ORDER_OF_SHARPS = ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#']


class Key(object):
    """
    Reference: https://en.wikipedia.org/wiki/Key_(music)
    """
    MAJOR = 'major'
    MINOR = 'minor'

    def __init__(self, key='C'):
        self.key = key
        self.mode = self.MINOR if key.islower() else self.MAJOR
        self.signature = 0

    def __str__(self):
        return "{} {}".format(self.key, self.mode)

    def __repr__(self):
        return "{}('{}')".format(type(self).__name__, str(self.key))

    def is_major(self):
        return self.mode == self.MAJOR

    def is_minor(self):
        return self.mode == self.MINOR
