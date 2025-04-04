from libraryitem import LibraryItem

class Loan:
    def __init__(self, item:LibraryItem, due_date:str):
        self.item = item
        self.due_date = due_date