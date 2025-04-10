import json

class HockeyApp:
    ui_actions = {
        "0": "quit",
        "1": "search for player",
        "2": "teams",
        "3": "countries",
        "4": "players in team",
        "5": "players from country",
        "6": "most points",
        "7": "most goals",
    }

    def __init__(self):
        while True:
            filename = input("file name: ")
            if not filename is None:
                break

        self.__players = HockeyApp.read_file(filename)
        print(f"read the data of {len(self.__players)} players")

    @staticmethod
    def read_file(filename) -> list | None:
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("File not found")
            return

    def ui_main(self):
        ui_actions = HockeyApp.ui_actions

        while True:
            print("\ncommands")
            for action in ui_actions.keys():
                print(f"{action} {ui_actions[action]}")

            user_action = input("\ncommand: ").casefold()
            if user_action in ui_actions.keys():
                user_action = ui_actions[user_action]

            if user_action == "quit":
                break

            elif user_action == "search for player":
                self.search_for_player()

    def search_for_player(self):
        search_query = input("name: ").casefold()

        results = []
        for player in self.__players:
            if search_query in player['name'].casefold():
                results.append(player)

        print(f"\nshowing {len(results)} results of query: \"{search_query}\"")
        for player in results:
            HockeyApp.print_player(player)

    @staticmethod
    def print_player(player):
        name = player['name']
        team = player['team']
        goals = player['goals']
        assists = player['assists']
        total = goals + assists

        whitespace_name = 22 - len(name)
        whitespace_team = 4 - len(str(goals))
        whitespace_goals = 3 - len(str(assists))
        whitespace_assists = 4 - len(str(total))

        print(name + " " * whitespace_name, end="")
        print(team + " " * whitespace_team, end="")
        print(f"{str(goals)} +" + " " * whitespace_goals, end="")
        print(f"{str(assists)} =" + " " * whitespace_assists, end="")
        print(total)







if __name__ == "__main__":
    my_app = HockeyApp()
    my_app.ui_main()
