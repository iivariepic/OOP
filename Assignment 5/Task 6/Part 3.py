from wordgame import WordGame

class RPSLS(WordGame):
    valid_inputs = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    wins = {
        'rock': ['lizard', 'scissors'],
        'paper': ['spock', 'rock'],
        'scissors': ['lizard', 'paper'],
        'lizard': ['spock', 'paper'],
        'spock': ['rock', 'scissors']
    }


    def round_winner(self, player1_word: str, player2_word: str):
        player1_word = player1_word.casefold()
        player2_word = player2_word.casefold()

        ## Check validity
        player1_valid = player1_word in self.valid_inputs
        player2_valid = player2_word in self.valid_inputs
        if not player1_valid and not player2_valid:
            return 0
        elif not player1_valid:
            return 2
        elif not player2_valid:
            return 1

        if player1_word == player2_word:
            return 0
        elif player2_word in self.wins[player1_word]:
            return 1
        else:
            return 2

def main():
    p = RPSLS(3)
    p.play()

if __name__ == '__main__':
    main()