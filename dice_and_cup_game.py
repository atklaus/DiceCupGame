import random

class SixSidedDie:
    """
    Represents a dice with six sides

    Attributes
    ----------
    num_list : list
        list of numbers of all sides of a six sided dice
    roll_value : None
        value of the most recent dice roll, initially set to None
    """

    def __init__(self):
        self.num_list = list(range(1,7))
        self.roll_value = None

    def roll(self):
        """
        select a random value from the list of numbers on a six sided dice
        :return the value of the roll by updating the roll_value attribute:
        """
        roll_value = random.choice(self.num_list)
        self.roll_value = roll_value

    def getFaceValue(self):
        """
        return the value of the most recent dice rolls
        """
        return self.roll_value

    def __repr__(self):
        """
        return the string and canonical definition of the class with the class name and most recent dice roll
        """        
        return str(self.__class__.__name__ + "({})").format(self.roll_value) 


class TenSidedDie(SixSidedDie):
    """
    Represents a dice with ten sides
    child class of the SixSidedDie class 

    Attributes
    ----------
    inherits all methods and attributes from the SixSidedDie class, but overwrites num_list
    
    num_list : list
        list of numbers of all sides of a ten sided dice

    """
    def __init__(self):
        super().__init__()
        self.num_list = list(range(1,11))


class TwentySidedDie(SixSidedDie):
    """
    Represents a dice with ten sides
    child class of the SixSidedDie class 

    Attributes
    ----------
    inherits all methods and attributes from the SixSidedDie class, but overwrites num_list
    
    num_list : list
        list of numbers of all sides of a ten sided dice
    """    
    def __init__(self):
        super().__init__()
        self.num_list = list(range(1,21))

class Cup:
    """
    Represents a dice with ten sides
    child class of the SixSidedDie class 

    Attributes
    ----------
    six_ct: int
        number of six sided die to be rolled
    ten_ct: int
        number of ten sided die to be rolled
    twenty_ct: int
        number of twenty sided die to be rolled
    die_dict: dictionary
        list of numbers of all sides of a ten sided dice
    dice_sum: list
        list of ints that represent each roll of the
    repr_str: list
        list of each objects __repr__ per dice roll, which will allow access to
        each instantiation of of a die object  
        
    """      
    def __init__(self, six_ct=1, ten_ct=1, twenty_ct=1):
        """
        construct the Cup class with the user inputs of the number of each die
        
        Parameters
        ----------
        six_ct: int
            number of six sided die to be rolled
        ten_ct: int
            number of ten sided die to be rolled
        twenty_ct         
            number of ten sided die to be rolled
        """
        
        self.six_ct = six_ct
        self.ten_ct = ten_ct
        self.twenty_ct = twenty_ct
        self.die_dict = {
        'six':self.six_ct,
        'ten':self.ten_ct,
        'twenty':self.twenty_ct
        }
        self.dice_sum = 0
        self.repr_str = []
    
    def roll(self):
        """
        iterate through each die object and roll a given die (6, 10, 20 sided) the number of times input
        """
        
        for die in self.die_dict.keys(): # loop through each die object
            for roll_num in range(self.die_dict[die]): #iterate the input number of times
                dieObj = self.get_die_object(die) #instantiate the die object
                dieObj.roll() 
                self.repr_str.append(dieObj.__repr__()) #
                self.dice_sum += dieObj.getFaceValue() 
                # self.dice_sum.append(dieObj.getFaceValue())
    
    def getSum(self):
        """
        return the accumulated sum of each dice roll
        """
        return self.dice_sum
      
    def get_die_object(self, die):
        """
        based on the dictionary being iterated over return a six, ten or twenty sided die object

        Parameters
        ----------
        die: str
            dictionary key to represent which dice object should be created
        """

        if die == 'six':
            dieObj = SixSidedDie()
        elif die == 'ten':
            dieObj = TenSidedDie()
        else:
            dieObj =TwentySidedDie()
        return dieObj
    
    def __repr__(self):
        """
        using the list of __repr__ from each instantiated die objects, combine these strings with commas between each object
        """
        return ",".join(self.repr_str)


cupObj = Cup(1,2,1)
cupObj.roll()
cupObj.getSum()
cupObj

