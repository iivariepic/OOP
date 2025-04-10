from box import Box
from item import Item
from book import Book
from game import Game
from song import Song
from movie import Movie

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
            add_item = "1"
            remove_item = "2"
            replace_item = "3"
            edit_items = "5"
            exit = "6"

            if choice == add_item:
                title ={"title": input("Enter title: ")}
                info = PackItems.prompt_item_info()
                item = PackItems.create_item(**(title | info))
                if isinstance(item, Item):
                    self.box.add_item(item)
                    self.log.append(f"Added item: {title}")
                else:
                    print(item + ", Please try again")

            elif choice == remove_item:
                title = input("Enter title of item to remove: ")
                self.box.remove_item(self.box.find_item_by_title(title))
                self.log.append(f"Removed item: {title}")

            elif choice == replace_item:
                old_title = input("Enter title of item to replace: ")
                new_title = {"title": input("Enter new title: ")}
                info = PackItems.prompt_item_info()

                new_item = PackItems.create_item(**(new_title | info))
                if isinstance(new_item, Item):
                    self.box.replace_item(self.box.find_item_by_title(old_title), new_item)
                    self.log.append(f"Replaced item: {old_title} with {new_title}")
                else:
                    print(new_item + ", Please try again")

            elif choice == edit_items:
                title = input("Enter title of item to edit: ")
                new_title = {"title": input("Enter new title (or leave blank): ")}
                info = PackItems.prompt_item_info()

                item = self.box.find_item_by_title(title)
                if item:
                    item.update_info(**(new_title | info))
                self.log.append(f"Edited item: {title}")

            elif choice == exit:
                self.save_log()
                break

            else:
                print("Invalid option. Please try again.")

    @staticmethod
    def prompt_item_info():
        item_info =  {
        "author": input("Enter author (or leave blank): "),
        "artist": input("Enter artist (or leave blank): "),
        "director": input("Enter director (or leave blank): "),
        "developer": input("Enter developer (or leave blank): "),
        "year": input("Enter year: "),
        }
        # Return only values that are not empty
        return {key: value for key, value in item_info.items() if value != ""}

    @staticmethod
    def create_item(**item_info) -> Item | str:
        if "year" not in item_info:
            return "Year was not provided"

        # Check that there are no multiple creator types
        creator_types = ["author", "artist", "director", "developer"]
        present_types = [key for key in creator_types if key in item_info]
        if len(present_types) != 1:
            return "You must provide exactly one of author, artist, director, or developer"

        if "author" in item_info:
            return Book(item_info["title"], item_info["year"], item_info["author"])

        if "artist" in item_info:
            return Song(item_info["title"], item_info["year"], item_info["artist"])

        if "director" in item_info:
            return Movie(item_info["title"], item_info["year"], item_info["director"])

        if "developer" in item_info:
            return Game(item_info["title"], item_info["year"], item_info["developer"])


    def save_log(self):
        with open("log.txt", "w") as file:
            for entry in self.log:
                file.write(entry + "\n")

if __name__ == "__main__":
    pack_items = PackItems()
    pack_items.user_interface()