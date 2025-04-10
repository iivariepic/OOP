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