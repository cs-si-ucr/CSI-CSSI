from enum import Enum
from pathlib import Path
import os
from definitions import ROOT_DIR

class GameState(Enum):
    INTRO = 0
    ASSIGNMENT = 1
    HOUSE = 2
    AMAZON = 3
    CULT = 4


class Action(Enum):
    TALK = 0
    INVESTIGATE = 1
    ARREST = 2

def read_state():
    with open(str(Path(ROOT_DIR) / '.Secret' / 'save_file.txt'), 'r') as fin:
        return GameState(int(fin.read()))

def write_state(state):
    with open(str(Path(ROOT_DIR) / '.Secret' / 'save_file.txt'), 'w') as fin:
        fin.write(str(state.value))

game_state = read_state()


def _move_file(src, dest):
    os.rename(str(Path(ROOT_DIR) / src), str(Path(ROOT_DIR) / dest))


def _set_state(g_state):
    game_state = g_state
    write_state(game_state)
    if game_state == GameState.ASSIGNMENT:
        # Coding assignment
        _move_file('.Secret/Temp/machine_learning', 'Mystery/Chapter_1/SIPD/Your_PC/Code/machine_learning')
        # Move over to our documents
        _move_file('.Secret/Temp/people.txt', '.Secret/Notes/people.txt')
        _move_file('.Secret/Temp/Omar_Phone', '.Secret/Notes/Omar_Phone')
    elif game_state == GameState.HOUSE:
        # Move over house
        _move_file('.Secret/Temp/Andre_House', 'Mystery/Chapter_1/Streets/Andre_House')
        # Move chief
        _move_file('Mystery/Chapter_1/SIPD/Chief.person', 'Mystery/Chapter_1/Streets/Andre_House/Chief.person')
    elif game_state == GameState.AMAZON:
        # Move SF
        _move_file('.Secret/Temp/SF', 'Mystery/Chapter_1/SF')
        # Move chief
        _move_file('Mystery/Chapter_1/Streets/Andre_House/Chief.person', 'Mystery/Chapter_1/SF/Chief.person')


def _check_password():
    try:
        with open(str(Path(ROOT_DIR) / 'Mystery' / 'Chapter_1' / 'SF' / 'AWS_Alley' / 'Computer' / 'password.txt'), 'r') as fin:
            return fin.read().strip() == 'money'
    except Exception:
        return False


def progress(action, target):

    # state machine
    if game_state == GameState.INTRO:
        if action == Action.TALK and target == 'Chief.person':
            _set_state(GameState.ASSIGNMENT)

    elif game_state == GameState.ASSIGNMENT:
        if action == Action.INVESTIGATE and target == 'College Avenue 34':
            _set_state(GameState.HOUSE)

    elif game_state == GameState.HOUSE:
        if action == Action.INVESTIGATE and target == '.wallpaper':
            _set_state(GameState.AMAZON)

    elif game_state == GameState.AMAZON:
        if action == Action.TALK and target == 'Kennen.person' and _check_password():
            _set_state(GameState.CULT)

    elif game_state == GameState.CULT:
        pass
