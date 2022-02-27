import sys
from enum import Enum
EDITOR_MODE = len(sys.argv) >= 2 and "editor" in sys.argv[1].lower()
class State(Enum):
    MENU = 1
    PRE = 2
    GAME = 3
    RESULT_WIN = 4
    RESULT_LOSS = 5
    QUIT = 6
