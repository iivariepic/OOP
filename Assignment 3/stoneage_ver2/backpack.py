class Backpack:
    """
    Models a backpack in an adventure game.

    Copyright: Sami Pyöttiälä, 2006
    """

    def __init__(self, capacity):
        """
        Initializes a new backpack that can hold up to the specified capacity of items.

        Preconditions: capacity > 0.0
        """
        self.__capacity = capacity
        self.__items = []
        self.__topmost = -1

    # Observer methods

    def equals(self, other):
        """
        Checks if the given object is similar to the current one.

        (Two backpacks are considered similar if their capacity is the same.)
        """
        if other is None:
            return False
        if self is other:
            return True
        if not isinstance(other, Backpack):
            return False

        epsilon = 0.001

        return Tools.almost_equal(self.__capacity, other.get_capacity(), epsilon)

    def get_capacity(self):
        """
        Returns the total capacity, part of which may already be in use.

        Preconditions: True
        """
        return self.__capacity

    def get_used_space(self):
        """
        Returns the total size of items already in the backpack.

        Preconditions: True
        """
        return sum(item.get_volume() for item in self.__items)

    def get_remaining_capacity(self):
        """
        Returns the amount of free space.

        Preconditions: True
        """
        return self.get_capacity() - self.get_used_space()

    def is_empty(self):
        """
        Checks if the backpack is empty.

        Preconditions: True
        """
        return len(self.__items) == 0

    def contains(self, item):
        """
        Checks if the item is already in the backpack.

        Preconditions: (item is not None)
        """
        return item in self.__items

    def show_topmost(self):
        """
        Returns the topmost item.

        Preconditions: not is_empty()
        """
        assert not self.is_empty(), "The backpack must not be empty."
        return self.__items[self.__topmost]

    def __str__(self):
        """
        Returns a string representation of the backpack.

        Preconditions: True
        """
        class_name = self.__class__.__name__
        backpack_info = f"{class_name}: [fill ratio: ({self.get_used_space()} / {self.get_capacity()})]"

        indent = " " * (len(backpack_info) // 4)

        i = 0
        current_index = self.__topmost
        while i < len(self.__items):
            backpack_info += f"\n{indent}{self.__items[current_index]}"
            current_index = (current_index + 1) % len(self.__items)
            i += 1

        return backpack_info

    # Modification methods

    def put(self, item):
        """
        Puts the item in the backpack. The item goes on top.

        Preconditions: (item is not None) and item.get_volume() <= self.get_remaining_capacity() and not self.contains(item)
        """
        self.__items.append(item)
        self.__topmost = self.__items.index(item)

    def remove_topmost(self):
        """
        Removes the topmost item.

        Preconditions: not is_empty()
        """
        assert not self.is_empty(), "The backpack must not be empty."
        self.__items.pop(self.__topmost)
        if not self.is_empty():
            self.__topmost = (len(self.__items) + self.__topmost - 1) % len(self.__items)
        else:
            self.__topmost = -1

    def rummage(self):
        """
        Cycles the contents of the backpack so that the topmost item changes cyclically.

        Preconditions: not is_empty()
        """
        self.__topmost = (self.__topmost + 1) % len(self.__items)







