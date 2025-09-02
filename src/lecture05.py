"""
Lecture05.py
====================================
This introduces the concepts of a Python class.

Some references:
    #. https://www.geeksforgeeks.org/python/inheritance-in-python/
    #. https://runestone.academy/ns/books/published/fopp/Classes/UserDefinedClasses.html
    #. https://www.geeksforgeeks.org/python/__init__-in-python/
    #. https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
    #. https://www.programiz.com/python-programming/property

| Seth McNeill
| 2025 September 02
"""

import random

class MSDie:
    """
    Multi-sided die

    from: 
        https://runestone.academy/ns/books/published/pythonds3/ProperClasses/a_proper_python_class.html

    Attributes
    ----------
    num_sides : int
       Number of sides on the die
    """

    def __init__(self, num_sides):
        """
        Initialize an MSDie object

        Parameters
        ----------
        num_side : int
          The number of sides to make the die
        """
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        """Roll the die to get a random number between 1 and num_sides
        """
        self.current_value = random.randrange(1,self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)


my_die = MSDie(6)
for i in range(5):
    print(my_die)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)
