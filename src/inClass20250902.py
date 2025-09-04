"""
inClass20250902.py
=======================================

This is demonstrating starting a class in class.

| Seth McNeill
| 2025 September 02
"""

import random  # so that we can random rolls
from datetime import datetime  # For getting the current time
import pdb  # for debugging
from time import sleep  # for delaying

class MSDie:
    """
    Multi-sided die

    Parameter
    ---------
    num_sides : int
      Number of sides for the die

    Attributes
    ----------
    num_sides : int
        number of sides for the die
    current_value : int
        Value from the last roll
    """

    def __init__(self, num_sides):
        """
        Initialize the MSDie object
        """
        self.num_sides = num_sides
        self.current_value = self.roll()
        print(f'MSDie init ran, num_sides is {self.num_sides}')

    def roll(self):
        """
        Roll the die to get a random number between 1 and num_sides

        Returns
        --------
        current_value : int
          The value from the last roll
        """
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value
    
    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return str(self.current_value)


class namedMSDie(MSDie):
    """
    Named MSDie 

    Includes a name as well as everything from MSDie

    Parameters
    ----------
    num_sides : int
      Number of sides for the die
    name : str
      Name for die

    Attributes
    ----------
    name : str
        Name for the die
    """

    def __init__(self, num_sides, dName):
        super().__init__(num_sides)
        self.name = dName
        print('namedMSDie init ran')

    def __str__(self):
        return self.name + ' : ' + str(self.current_value)

    def __repr__(self):
        return self.name + ' : ' + str(self.current_value)


class animal:
    """
    Animal class

    Parameters
    ----------
    name : str
      name for animal
    type : str
      type of animal 
    """
    
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.birthday = datetime.now()

    def __str__(self):
        return self.name + " is a " + self.animal_type 

    def age(self):
        """
        Returns the animals age in seconds

        Also see age().total_seconds()

        Returns
        --------
        age : float
          The animal's age in seconds
        """
        return (datetime.now() - self.birthday).total_seconds()

class myDog(animal):
    """
    myDog class that inherits from animal but presets the type to 'dog'

    Parameters
    ----------
    name : str
      Name for dog
    """

    def __init__(self, name):
        super().__init__(name, 'dog')
        self.nLegs = 4

if __name__ == "__main__":
    d6a = MSDie(6)
    print(d6a)
    print(d6a.roll())
    d_list = [MSDie(7), MSDie(20)]
    print(d_list)

    a1 = animal("bob", "bird")
    print(a1)
    
    print("our new named die")
    nd1 = namedMSDie(9, 'charlie')
    print(nd1)

    dog1 = myDog('fido')
    sleep(2) # wait for 2 seconds
    print(f'{dog1.name} is {dog1.age()} seconds old and is a {dog1.animal_type}')

    pdb.set_trace()