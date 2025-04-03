from task import Task

class OrderBook:
    def __init__(self):
        self.orders:list[Task] = []

    def add_order(self, description:str, programmer:str, workload:int):
        new_order = Task(description, programmer, workload)
        self.orders.append(new_order)

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list({order.programmer for order in self.orders})

    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return

        raise ValueError(f"No order exists with the id {id}")

    def finished_orders(self):
        result:list[Task] = []
        for order in self.orders:
            if order.is_finished:
                result.append(order)

        return result

    def unfinished_orders(self):
        result:list[Task] = []
        for order in self.orders:
            if not order.is_finished:
                result.append(order)

        return result

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f"Programmer {programmer} is not assigned to a Task")

        finished_tasks = []
        finished_hours = 0
        unfinished_tasks = []
        unfinished_hours = 0

        for task in self.orders:
            if task.programmer == programmer:
                if task.is_finished():
                    finished_tasks.append(task)
                    finished_hours += task.workload
                else:
                    unfinished_tasks.append(task)
                    unfinished_hours += task.workload

        return len(finished_tasks), len(unfinished_tasks), finished_hours, unfinished_hours