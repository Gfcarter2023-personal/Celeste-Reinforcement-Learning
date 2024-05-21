import moves
import time

moves.initialize()
moves.dash("left")
moves.dash("up")
time.sleep(1)
moves.jump()
moves.dash("down-right")
moves.jump()

