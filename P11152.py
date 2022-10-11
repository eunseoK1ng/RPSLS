from RPSLS_player import RPSLS_player
import random
game_list = ["rock", "scissors", "paper", "lizard", "spock"]

class P11152(RPSLS_player):
    def __init__(self):
        pass

    def shoot(self) -> str:
        return random.choice(game_list)
    
    def update(self, result: str, competitor_shot: str):
        pass