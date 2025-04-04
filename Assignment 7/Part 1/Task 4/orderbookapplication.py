from orderbook import OrderBook
import re

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()

    @staticmethod
    def get_commands():
        print("0 - exit")
        print("1 - add order")
        print("2 - list finished tasks")
        print("3 - list unfinished tasks")
        print("4 - mark task as finished")
        print("5 - programmers")
        print("6 - status of programmer")

    def add_order(self):
        description = input("Description: ")
        programmer_workload = input("Programmer and workload estimate: ")
        match = re.search(r"(.+)\s(\d+)$", programmer_workload)
        if not match:
            print("erroneous input")
            return

        programmer, workload = programmer_workload.split(" ")
        self.__orderbook.add_order(description, programmer, int(workload))

    def list_finished(self):
        for task in self.__orderbook.finished_orders():
            print(task)

    def list_unfinished(self):
        for task in self.__orderbook.unfinished_orders():
            print(task)

    def mark_finished(self):
        id = input("id: ")
        if not id.isnumeric():
            print("erroneous input")
            return

        for task in self.__orderbook.unfinished_orders():
            if task.id == int(id):
                task.mark_finished()
                print("marked as finished")
                return

        print(f"no unfinished task found with id {id}")

    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer_name = input("programmer: ")
        if programmer_name not in self.__orderbook.programmers():
            print("erroneous input")
            return

        print(self.__orderbook.status_of_programmer(programmer_name))

    def execute(self):
        self.get_commands()
        while True:
            user_input = input("command: ")
            if user_input == "0":
                return

            elif user_input == "1":
                self.add_order()

            elif user_input == "2":
                self.list_finished()

            elif user_input == "3":
                self.list_unfinished()

            elif user_input == "4":
                self.mark_finished()

            elif user_input == "5":
                self.programmers()

            elif user_input == "6":
                self.status_of_programmer()

            else:
                print("erroneous input")

def main():
    app = OrderBookApplication()
    app.execute()

if __name__ == "__main__":
    main()