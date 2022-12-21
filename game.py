from player import Player
from random import randint
from time import sleep


class Game:
    '''
    Game class is responsible for game mechanics.
    '''

    MAX_ROUNDS = 3
    player1, player2 = None, None
    figures = ("rock", "paper", "scissors")


    def initialize_player(self):
        name = input("Enter player's name: ")
        player = Player(name)
        return player


    def round_start_message(self, counter):
        print(f"\n========= New round [Round no.: {counter}] =========\n")


    def draw(self):
        return randint(0,2)


    def match(self):
        player1_figure = self.draw()
        print(f"Player {self.player1.get_name()} show {self.figures[player1_figure]}")
        player2_figure = self.draw()
        print(f"Player {self.player2.get_name()} show {self.figures[player2_figure]}")
        if (player1_figure > player2_figure):
            self.increase_score(self.player1)
        elif (player1_figure == player2_figure):
            print("Draw!")
        else: 
            self.increase_score(self.player2)


    def increase_score(self, player):
        player.add_point()
        print(f"{player.get_name()} has won this round. Total score: [{player.get_score()}]")


    def check_winner(self):
        if (self.player1.get_score() == self.MAX_ROUNDS):
            print(f"\n:: {self.player1.get_name()} has won! ::\n")
            return self.player1
        if (self.player2.get_score() == self.MAX_ROUNDS):
            print(f"\n:: {self.player2.get_name()} has won! ::\n")
            return self.player2
        return None


    def do_players_exist(self):
        if (self.player1 and self.player2 is not None):
            return True
        else: return False

    
    def create_players(self):
        if not self.do_players_exist():
            self.player1 = self.initialize_player()
            self.player2 = self.initialize_player()


    def handle_round(self, counter):
        self.create_players()
        sleep(2.5)
        self.round_start_message(counter)
        self.match()


    def has_winner(self):
        if self.do_players_exist() and self.check_winner():
            return True


    def start(self):
        _round_counter = 0

        while True:
            _round_counter += 1
            if (self.has_winner()):
                break
            self.handle_round(_round_counter)
