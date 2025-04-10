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