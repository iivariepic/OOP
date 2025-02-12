
class Character:
    """
        Models a character in an adventure game.
    
        Copyright: Sami Pyöttilä, 2006
    """

    def __init__(self, name, strength, skill, max_health):
        """ Initializes a new character with empty hands and no backpack.

            Arguments:
            name : the name of the character
            strength : the strength of the character
            skill : the skill and cleverness of the character
            max_health : the maximum health of the character when fully healthy

            Preconditions: 
            (name is not None) and (len(name) > 0) and 
            (strength > 0.0) and (skill > 0.0) and (max_health > 0.0)
        """
        self.__name = name
        self.__strength = strength
        self.__skill = skill
        self.__max_health = max_health
        self.__health = max_health
        self.__money:float = 0

        self.__left_hand = None
        self.__right_hand = None
        self.__backpack = None ###


    # Observation

    def is_alive(self):
        """ Is the character alive? """
        return self.__health > 0.0

    def has_free_hand(self):
        """ Is there space in at least one hand? """
        return self.is_left_hand_free() or self.is_right_hand_free()

    def is_left_hand_free(self):
        """ Is the left hand empty? """
        return self.__left_hand is None

    def is_right_hand_free(self):
        """ Is the right hand empty? """
        return self.__right_hand is None

    def get_left_hand_item(self):
        """ Returns the item in the left hand. """
        return self.__left_hand

    def get_right_hand_item(self):
        """ Returns the item in the right hand. """
        return self.__right_hand

    def get_name(self):
        """ Returns the name. """
        return self.__name

    def get_health(self):
        """ Returns the health. """
        return self.__health

    def get_money(self):
        return self.__money

    def enough_money(self, target_amount:float):
        return self.__money >= target_amount

    def get_backpack(self):
        return self.__backpack

    def __str__(self):
        """ Returns a string representation of the character. """
        class_name = self.__class__.__name__
        character_info = f"{class_name}: [{self.__name} {self.__strength} {self.__skill} ({self.__health} / {self.__max_health})]"

        indent = " " * (len(character_info) // 4)
        character_info += f"\n{indent}right: {self.__right_hand}"
        character_info += f"\n{indent}left: {self.__left_hand}"

        character_info += "\n" + self.__backpack.__str__()

        return character_info

    # Modification

    def set_left_hand(self, item):
        """ Sets the item in the left hand. """
        self.__left_hand = item

    def set_right_hand(self, item):
        """ Sets the item in the right hand. """
        self.__right_hand = item

    def set_free_hand(self, item):
        """ Sets the item in the right hand if it is free. 
            Otherwise, sets the item in the left hand.

            Preconditions: (item is not None) and has_free_hand()
        """
        if self.is_right_hand_free():
            self.set_right_hand(item)
        else:
            self.set_left_hand(item)


    def set_backpack(self, new_backpack):
        """Sets new_backpack for the current character.

        Preconditions: (new_backpack != None)
        """
        self.__backpack = new_backpack




    def give_item(self, other, item):
        """ Gives the item in hand to another character (other).
            After giving, the current character no longer has the item in hand.

        Preconditions: (other is not None) and (item is not None)
                       and (item == self.get_left_hand_item() 
                       or item == self.get_right_hand_item())
                       and (other.has_free_hand())
        """
        # Give the item:
        other.set_free_hand(item)

        # Release the item:
        if item == self.get_left_hand_item():
            self.set_left_hand(None)
        if item == self.get_right_hand_item():
            self.set_right_hand(None)


    def take_damage(self, damage_amount):
        """ Suffers a hit that causes damage.

            Preconditions: damage_amount >= 0
        """
        self.__health -= damage_amount


    def attack(self, other, use_right_hand):
        """ Attacks another character with the right hand or the item in the right hand if specified.
            Otherwise, attacks with the left hand.

            Preconditions: (other is not None)
        """
        import random
        luck = random.random()

        multiplier = self.__strength / 100.0
        multiplier += self.__skill / 120.0

        weapon = self.get_right_hand_item() if use_right_hand else self.get_left_hand_item()

        # Is the item usable?
        if weapon is None or not weapon.is_functional():
            damage = 1.0
        else:
            damage = weapon.get_damage()

        damage *= multiplier * luck
        other.take_damage(damage)


    def heal_fully(self):
        """ Sets the character's health to the maximum possible. """
        self.__health = self.__max_health

    def change_money(self, amount:float):
        """ Changes the character's money.
        Preconditions: if amount is negative,
        character needs to have enough money"""
        self.__money += amount