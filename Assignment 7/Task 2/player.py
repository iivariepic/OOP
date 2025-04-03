class Player:
    def __init__(self, name:str, player_id:int):
        self.__name = name
        self.__player_id = player_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def player_id(self):
        return self.__player_id

    @player_id.setter
    def player_id(self, player_id:int):
        self.__player_id = player_id

    def __str__(self):
        return f"{self.__name}: {self.player_id}"
