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