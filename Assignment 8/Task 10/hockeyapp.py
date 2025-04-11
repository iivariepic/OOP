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
            player_list = HockeyApp.read_file(input("file name: "))

            if not player_list is None:
                break

        self.__players = player_list
        print(f"read the data of {len(self.__players)} players")

    @staticmethod
    def read_file(filename) -> list | None:
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("File not found")
            return None

    def ui_main(self):
        ui_actions = HockeyApp.ui_actions

        while True:
            print("\ncommands")
            for action in ui_actions.keys():
                print(f"{action} {ui_actions[action]}")

            # Convert user input to usable string
            user_action = input("\ncommand: ").casefold()
            if user_action in ui_actions.keys():
                user_action = ui_actions[user_action]

            # Handle user input
            if user_action == "quit":
                break

            elif user_action == "search for player":
                self.search_for_player()

            elif user_action == "teams":
                self.show_all_unique("team")

            elif user_action == "countries":
                self.show_all_unique("nationality")

            elif user_action == "players in team":
                self.show_players_with_key("team", input("team: "))

            elif user_action == "players from country":
                self.show_players_with_key("nationality", input("country: "))

            elif user_action == "most points":
                self.show_top_players(HockeyApp.integer_input("how many: "), HockeyApp.total_score)

            elif user_action == "most goals":
                self.show_top_players(HockeyApp.integer_input("how many: "), HockeyApp.total_goals)

            else:
                print("Invalid Input")

    @staticmethod
    def integer_input(prompt):
        while True:
            user_input = input(prompt)

            if user_input.isnumeric():
                return user_input

            print("Please insert a number")

    def search_for_player(self):
        search_query = input("name: ").casefold()

        results = []
        for player in self.__players:
            if search_query in player['name'].casefold():
                results.append(player)

        print(f"\nshowing {len(results)} results of query: \"{search_query}\"")
        for player in results:
            HockeyApp.print_player(player)

    def show_all_unique(self, key):
        players = self.__players

        # Record each unique occurrence to a set
        appearances = set([])
        for player in players:
            appearances.add(player[key])

        # Print out the teams in alphabetical order
        appearances = sorted(list(appearances))
        for appearance in appearances:
            print(appearance)

    def show_players_with_key(self, key, value):
        all_players = self.__players
        players = []
        for player in all_players:
            if player[key] == value:
                players.append(player)

        players = sorted(players, key=HockeyApp.total_score, reverse=True)
        for player in players:
            HockeyApp.print_player(player)

    def show_top_players(self, amount, comparison):
        all_players = self.__players
        sorted_players = sorted(all_players, key=comparison, reverse=True)
        for index in range(int(amount)):
            HockeyApp.print_player(sorted_players[index])

    @staticmethod
    def total_score(player):
        return player['goals'] + player['assists']

    @staticmethod
    def total_goals(player):
        # Function that is only used for sorting
        return player['goals']

    @staticmethod
    def print_player(player):
        name = player['name']
        team = player['team']
        goals = player['goals']
        assists = player['assists']
        total = HockeyApp.total_score(player)

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
