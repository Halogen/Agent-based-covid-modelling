"""
File Doc
"""
import numpy as np

class Stan():
    """
    Class Doc
    """
    def __init__(self):
        val = 1
        self.temp = 5
        self.val = self.tester(val)

    def tester(self, temp_value):
        """
        Func Doc
        """
        new_value = temp_value + np.random.randint(10) + self.temp
        return new_value

    def other_func(self):
        """
        Another function to make pylint happy
        """
        self.temp = self.temp ** 2
