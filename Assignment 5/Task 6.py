import random

class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        player1Length = len(player1_word)
        player2Length = len(player2_word)

        if player1Length == player2Length:
            return 0
        elif player1Length > player2Length:
            return 1
        else:
            return 2


class MostVowels(WordGame):
    vowels = ['a', 'e', 'i', 'o', 'u']

    @staticmethod
    def count_vowels(word:str) -> int:
        result:int = 0

        for character in word:
            if character in MostVowels.vowels:
                result += 1

        return result

    def round_winner(self, player1_word: str, player2_word: str):
        player1Count = self.count_vowels(player1_word)
        player2Count = self.count_vowels(player2_word)

        if player1Count == player2Count:
            return 0
        elif player1Count > player2Count:
            return 1
        else:
            return 2



def main():
    p = MostVowels(3)
    p.play()

if __name__ == '__main__':
    main()