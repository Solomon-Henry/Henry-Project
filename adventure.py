from player import Player
from general import game_cnt
    
def Game_Loop():
    User = Player()
    while game_cnt[0] <= game_cnt[1]:
        if not game_cnt[0] == game_cnt[1]:
            User.move(game_cnt[0])
            game_cnt[0] += 1
        else:
            User.restart()

def main():
    Game_Loop()

main()