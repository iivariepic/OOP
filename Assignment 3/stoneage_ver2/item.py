
class Item:
    """
        Models a general item in an adventure game.
    
        Copyright: Sami Pyöttilä, 2006
    """

    def __init__(self, name, value, volume, damage, max_durability):
        """ Initializes a new item.

            Arguments:
            name : the name of the item
            value : the value of the item in money
            volume : the volume of the item for storage
            damage : the damage the item can cause, e.g., when used as a weapon
            max_durability : the maximum durability of the item when fully intact

            Preconditions: 
            (name is not None) and (len(name) > 0) and 
            (value > 0.0) and (volume > 0.0) and (damage > 0.0) and (max_durability > 0.0)
        """
        self.__name = name
        self.__value = value
        self.__volume = volume
        self.__damage = damage
        self.__max_durability = max_durability
        self.__durability = max_durability


    def is_functional(self):
        """ Is the item still in working condition?
            Preconditions: True
        """
        return self.__durability > 0.0

    def get_damage(self):
        """ Returns the damage value.
            Preconditions: True
        """
        return self.__damage

    def get_max_durability(self):
        """ Returns the maximum durability when intact.
            Preconditions: True
        """
        return self.__max_durability

    def get_volume(self):
        """ Returns the volume.
            Preconditions: True
        """
        return self.__volume

    def get_value(self):
        """ Returns the value.
            Preconditions: True 
        """
        return self.__value

    def get_name(self):
        """ Returns the name.
            Preconditions: True
        """
        return self.__name

    def __str__(self):
        """ Returns a string representation of the item.
            Preconditions: True
        """
        return f"{self.__class__.__name__}: [{self.__name} {self.__value} {self.__volume} {self.__damage} ({self.__durability} / {self.__max_durability})]"

    def repair(self):
        """ Repairs the item to full durability.
            Preconditions: True
        """
        self.__durability = self.__max_durability


