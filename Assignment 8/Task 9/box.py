from item import Item

class Box:
    def __init__(self):
        self.items:list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("No item found")

    def replace_item(self, old_item:Item, new_item:Item):
        if old_item in self.items:
            index = self.items.index(old_item)
            self.items.insert(index, new_item)
            self.items.remove(old_item)
        else:
            print("No item found")

    def get_descriptions(self):
        return [item.description for item in self.items]

    def find_item_by_title(self, query):
        for item in self.items:
            if item.title == query:
                return item

        print(f"No item was found with title {query}")