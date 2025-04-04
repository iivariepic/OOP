class Task:
    id_counter = 0

    def __init__(self, description:str, programmer:str, workload: int):
        self.__description = description
        self.__programmer = programmer
        self.__workload = workload
        Task.id_counter += 1
        self.__id = Task.id_counter
        self.__is_finished:bool = False


    @property
    def description(self):
        return self.__description

    @property
    def programmer(self):
        return self.__programmer

    @property
    def workload(self):
        return self.__workload

    @property
    def id(self):
        return self.__id

    def is_finished(self):
        return self.__is_finished

    def mark_finished(self):
        self.__is_finished = True

    def __str__(self):
        result = f"{self.__id}: {self.__description}, ({self.workload} hours) programmer {self.__programmer}"
        if self.is_finished():
            result += " FINISHED"
        else:
            result += " NOT FINISHED"

        return result