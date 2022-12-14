N = 5

from RPSLS_game import RPSLS_game

from P00000 import P00000
from P11152 import P11152

game = RPSLS_game(P00000, P11152)
for i in range(1, N+1):
    print(f"[Round {i}]")
    game.proceed_match()

print(game.get_score())