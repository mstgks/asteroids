game_modes = [0, 1, 2, 3]
def difficulty():
    while True:
        try:
            mode = int(input("Type 1 for easy mode, 2 for medium, 3 for hard: "))
            if mode not in game_modes:
                continue
            elif mode == 0:
                print("GOD MODE ACTIVATED")
                return mode
            else:
                return mode
        except ValueError:
            pass
mode = difficulty()
if mode == 0:
    god_mode = True
else:
    god_mode = False

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
LINE_WIDTH = 2
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 350 - (mode * 25)
PLAYER_SPEED = 250 - (mode * 25)
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 1.0 - (mode / 10)
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.1 + (mode / 10)