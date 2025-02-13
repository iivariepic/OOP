from pygame import KEYDOWN, K_RIGHT, K_LEFT, K_DOWN, KSCAN_UP, KEYUP, K_SPACE

from item import Item
import pygame
from gridtile import GridTile
from backpack import Backpack

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
        self.__backpack = None

        self.__image:pygame.Surface = None
        self.__rect:pygame.Rect = None

        self.__animation_counter = 0
        self.__name_text = None
        self.__name_text_rect = None
        self.__inside_tile:GridTile = None


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

    def remove_item_from_hand(self, item:Item):
        if self.get_left_hand_item() == item:
            self.set_left_hand(None)
        elif self.get_right_hand_item() == item:
            self.set_right_hand(None)

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


    # Game processing
    def initialize_game(self):
        self.__image: pygame.Surface = pygame.image.load(".\\game_assets\\caveman.png").convert_alpha()
        self.__rect: pygame.Rect = self.__image.get_rect()

        self.__animation_counter = 0
        name_font = pygame.font.SysFont('Posterama', 24)
        self.__name_text = name_font.render(self.__name, True, (255, 0, 0))
        self.__name_text_rect = self.__name_text.get_rect()
        self.__inside_tile: GridTile = None


    def update(self):
        self.__play_animation()

    def __play_animation(self):
        # Flip image every 5 frames
        self.__animation_counter += 1
        if self.__animation_counter == 20:
            self.__image = pygame.transform.flip(self.__image, True, False)
            self.__animation_counter = 0

    def process_input(self, input, game):
        # Move to a direction based on input:
        direction = (0, 0)
        if input == K_LEFT:
            direction = (-1, 0)
        elif input == K_RIGHT:
            direction = (1, 0)
        elif input == 1073741906:
            direction = (0, -1)
        elif input == K_DOWN:
            direction = (0, 1)

        if direction != (0, 0):
            self.move_direction(direction, game)
            return

        if input == K_SPACE:
            pickup_list = game.get_items() + game.get_backpacks()
            for item in pickup_list:
                item_on_ground = item.is_on_ground()
                item_on_tile = item.get_inside_tile() == self.__inside_tile
                if item_on_tile and item_on_ground:
                    self.pick_up(item, game)
                    return

            interaction_list = game.get_characters() + game.get_shops()
            interaction_list.remove(self)

            objects_on_tile = []
            for thing in interaction_list:
                if thing.get_inside_tile() == self.__inside_tile:
                    objects_on_tile.append(thing)

            if len(objects_on_tile) > 0:
                pass
                return


    def blit(self, game):
        game.get_screen().blit(self.__image, self.__rect)
        game.get_screen().blit(self.__name_text, self.__name_text_rect)

    def pick_up(self, item, game):
        if type(item) == Backpack:
            if self.__backpack == None:
                # Get new backpack
                self.set_backpack(item)
                self.__backpack.pick_up()
                game.set_info_text(f"Picked up backpack with capacity {self.__backpack.get_capacity()}")
            else:
                # Switch backpack if already wearing one
                self.__backpack.place_on_ground(item.get_inside_tile())
                self.set_backpack(item)
                self.__backpack.pick_up()
                game.set_info_text(f"Switched to backpack with capacity {self.__backpack.get_capacity()}")
            return

        if self.has_free_hand():
            item.pick_up()
            self.set_free_hand(item)
            game.set_info_text(f"Picked up {item.get_name()} to free hand")

        elif self.__backpack:
            backpack_remaining = self.__backpack.get_remaining_capacity()
            if backpack_remaining >= item.get_volume():
                item.pick_up()
                self.__backpack.put(item)
                game.set_info_text(f"Picked up {item.get_name()} to backpack")
            else:
                game.set_info_text(f"No space for item: {item.get_name()}")

        else:
            game.set_info_text(f"No space for item: {item.get_name()}")


    def __set_coordinates(self, coordinates:tuple, game):
        self.__rect.topleft = coordinates
        screen_rect = game.get_screen().get_rect()

        self.__name_text_rect.center = self.__rect.center
        self.__name_text_rect.top = self.__rect.bottom + 2
        if self.__name_text_rect.top > screen_rect.bottom:
            self.__name_text_rect.bottom = self.__rect.top + 2

    def get_coordinates(self):
        return self.__rect.topleft

    def get_inside_tile(self):
        return self.__inside_tile

    def move_direction(self, direction:tuple[int, int], game):
        old_position = self.__rect.topleft
        new_direction = tuple(i * 32 for i in direction)
        new_position = tuple(sum(x) for x in zip(old_position,new_direction))

        for tile in game.get_grid():
            if tile.get_coordinates() == new_position:
                self.set_inside_tile(tile, game)

    def set_inside_tile(self, tile, game):
        self.__inside_tile = tile
        self.__set_coordinates(tile.get_coordinates(), game)