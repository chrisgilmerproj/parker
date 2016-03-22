Tutorial 01 - Notes
===================

The basic building block of any music is the note.  A note is defined by its
name, octave, and accidentals following Scientific Pitch Notation.  Let's play
with notes:

>>> from parker.notes import Note


----


Note objects
-------------

A note can be easily constructed from a valid note name.  Let's try a few:


>>> n = Note('C')
>>> print(n)
C4
>>> repr(n)
"Note('C4')"


You'll notice immediately that the note that was returned says `C4` instead of
`C`.  This is because the default octave will be the middle or fourth (4)
octave of the scale.  It also has no accidentals (sharps or flats).

There are a lot of valid notes that you can construct:


>>> note_list = ['C', 'C4', 'C#4', 'Cbb4']
>>> print([Note(note) for note in note_list])
[Note('C4'), Note('C4'), Note('C#4'), Note('Cbb4')]


Suprisingly you can use some very interesting notes:


>>> Note('C######bb')
Note('C####4')
>>> Note('C#b#bb##b##bb')
Note('C4')


You can use a convenience method to check if the format of the note is valid
before constructing a note:


>>> from parker.notes import note_is_valid
>>> note_is_valid('C')
True
>>> note_is_valid('c')
False


Note Properties
---------------

As mentioned previously every Note object is constructed from a name, octave,
and accidentals.  You can get to these properties directly if desired:


>>> n = Note('C#4')
>>> n.base_name
>>> 'C'
>>> n.octave
>>> 4
>>> n.accidentals
>>> 1


The accidentals are captured as integer steps, or semitones, above the base
note.  The accidentals are changed internally into regognizable strings using
a private method:


>>> n = Note('C#4')
>>> n._get_accidentals_as_string()
'#'


Notes as Integers
-----------------

Notes can also be represented as integers:


>>> int(Note('C4'))
60


Or constructed from integers:


>>> Note(60)
Note('C4')


Constructing Notes
------------------

You can construct notes using strings, integers, and other Note objects.  As
demonstrated all of these are valid:


>>> Note('C')
Note('C4')
>>> Note(60)
Note('C4')
>>> Note(Note('C'))
Note('C4')



Augment and Diminish Notes
--------------------------

Should you want to augment or diminish a note you can use easy convenience
methods:


>>> n = Note('C4')
>>> n.augment()
Note('C#4')
>>> n.diminish()
Note('Cb4')
>>> n
Note('C4')


The methods to augment and diminish return new note objects instead of
modifying the note in place.  To modify in place you must use a different
method:


>>> n = Note('C4')
>>> n.set_augment()
Note('C#4')
>>> n
Note('C#4')
>>> n.set_diminish()
Note('C4')
>>> n
Note('C4')


Other Reprentations
-------------------

There are different use cases for representing a note.  In some cases the note
is needed without the octave in the string.  This is called Generalization:


>>> n = Note('C####4')
>>> n.generalize()
'C####'


In other cases what is needed is the note in its most succinct form.  This is
called Normalization:


>>> n = Note('C####4')
>>> n.normalize()
'E'


Note Frequencies
----------------

Every note has a frequency.  To access the frequency of a note simply ask:


>>> n = Note('C4')
>>> n.get_frequency()
261.6255653005985


This is a bit cumbersome so it can be managed by setting the desired digits:


>>> n = Note('C4')
>>> n.get_frequency(ndigits=3)
261.626


You can get a note object from a frequency by using a convenience method:


>>> from parker.notes import note_from_frequency
>>> note_from_frequency(261.626)
Note('C4')


This method will only get the closest note but will not tell how far out
of tune the note is given the frequency.

