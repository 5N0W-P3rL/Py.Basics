# update high score containing file with new high score value

def game_score ():
    return 644   #Here the game function will return players score 
sc = game_score()

with open("high_score.txt") as f:
    hs = f.read()

if hs == '':
    with open("high_score.txt", "w") as f:
        f.write(str(sc))

elif sc > int(hs):
    with open("high_score.txt", "w") as f:
        f.write(str(sc))