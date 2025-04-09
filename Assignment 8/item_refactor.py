"""
Refactor the code, in the exercise sheet there is a list of possible problems that you can find from this program.
Some of the problems are overlapping, so you might fix two problems when you are fixing the code.

Hint. start by utilizing inheritance and method overriding, then continue with other parts of the code.
"""
class Item:
    def __init__(
            self,
            title=None,
            author=None,
            artist=None,
            director=None,
            developer=None,
            year=None
    ):
        # Initialize the item with various attributes
        self.__title = title
        self.__author = author
        self.__artist = artist
        self.__director = director
        self.__developer = developer
        self.__year = year

    @property
    def title(self):
        # Return the title of the item
        return self.__title

    @property
    def author(self):
        # Return the author of the item (only for books)
        return self.__author

    @property
    def artist(self):
        # Return the artist of the item (only for music)
        return self.__artist

    @property
    def director(self):
        # Return the director of the item (only for movies)
        return self.__director

    @property
    def developer(self):
        # Return the developer of the item (only for computer games)
        return self.__developer

    @property
    def year(self):
        # Return the year of the item
        return self.__year

    def print_item_description(self):
        # Print the description of the item
        description = f"Title: {self.title}, Year: {self.year}"
        if self.author:
            description += f", Author: {self.author}"
        if self.artist:
            description += f", Artist: {self.artist}"
        if self.director:
            description += f", Director: {self.director}"
        if self.developer:
            description += f", Developer: {self.developer}"
        return description

    def update_info(self, title=None, author=None, artist=None, director=None, developer=None, year=None):
        # Updates the information in the item
        if title:
            self.__title = title
        if author:
            self.__author = author
        if artist:
            self.__artist = artist
        if director:
            self.__director = director
        if developer:
            self.__developer = developer
        if year:
            self.__year = year

class Box:
    def __init__(self):
        self.items = {}

    def add_item(self, key, item: Item):
        self.items[key] = item

    def remove_item(self, key):
        if key in self.items:
            del self.items[key]
        else:
            print("No item found")

    def replace_item(self, old_key, new_key, new_item):
        if old_key in self.items:
            del self.items[old_key]
            self.items[new_key] = new_item
        else:
            print("No item found")

    def get_descriptions(self):
        return [item.print_item_description() for item in self.items.values()]

    def update_item(self, key, title=None, author=None, artist=None, director=None, developer=None, year=None):
        #Hint! check here how to use kwargs!
        # for example: https://realpython.com/python-kwargs-and-args/
        if key in self.items:
            self.items[key].update_info(title, author, artist, director, developer, year)
        else:
            print("No item found")

class PackItems:
    def __init__(self):
        self.box = Box()
        self.log = []

    def user_interface(self):
        while True:
            print("\nOptions:")
            print("1. Add item")
            print("2. Remove item")
            print("3. Replace item")
            print("4. View items")
            print("5. Edit item")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter title: ")
                author = input("Enter author (or leave blank): ")
                artist = input("Enter artist (or leave blank): ")
                director = input("Enter director (or leave blank): ")
                developer = input("Enter developer (or leave blank): ")
                year = input("Enter year: ")
                item = Item(title, author, artist, director, developer, year)
                self.box.add_item(title, item)
                self.log.append(f"Added item: {title}")
            elif choice == "2":
                title = input("Enter title of item to remove: ")
                self.box.remove_item(title)
                self.log.append(f"Removed item: {title}")
            elif choice == "3":
                old_title = input("Enter title of item to replace: ")
                new_title = input("Enter new title: ")
                author = input("Enter author (or leave blank): ")
                artist = input("Enter artist (or leave blank): ")
                director = input("Enter director (or leave blank): ")
                developer = input("Enter developer (or leave blank): ")
                year = input("Enter year: ")
                new_item = Item(new_title, author, artist, director, developer, year)
                self.box.replace_item(old_title, new_title, new_item)
                self.log.append(f"Replaced item: {old_title} with {new_title}")
            elif choice == "5":
                title = input("Enter title of item to edit: ")
                new_title = input("Enter new title (or leave blank): ")
                author = input("Enter new author (or leave blank): ")
                artist = input("Enter new artist (or leave blank): ")
                director = input("Enter new director (or leave blank): ")
                developer = input("Enter new developer (or leave blank): ")
                year = input("Enter new year (or leave blank): ")
                self.box.update_item(title, title=new_title, author=author, artist=artist, director=director, developer=developer, year=year)
                self.log.append(f"Edited item: {title}")
            elif choice == "6":
                self.save_log()
                break
            else:
                print("Invalid option. Please try again.")

    def save_log(self):
        with open("log.txt", "w") as file:
            for entry in self.log:
                file.write(entry + "\n")


if __name__ == "__main__":
    pack_items = PackItems()
    pack_items.user_interface()

    # This is for testing the Item class

    item1 = Item(title="1984", author="George Orwell", year=1949)
    item2 = Item(title="Thriller", artist="Michael Jackson", year=1982)
    item3 = Item(title="Inception", director="Christopher Nolan", year=2010)
    item4 = Item(title="The Legend of Zelda", developer="Nintendo", year=1986)

    print(item1.print_item_description())
    print(item2.print_item_description())
    print(item3.print_item_description())
    print(item4.print_item_description())

    box = Box()
    box.add_item("1984", Item(title="1984", author="George Orwell", year=1949))
    box.add_item("Thriller", Item(title="Thriller", artist="Michael Jackson", year=1982))

    print("Before replacement:")
    for description in box.get_descriptions():
        print(description)

    box.replace_item("1984", "1984", Item(title="1984", author="George Orwell", year=1950))

    print("\nAfter replacement:")
    for description in box.get_descriptions():
        print(description)