import json
import os
from random import randint
from random import choice
from heading_func import game_heading
from accout_func import get_or_create_account
from hint import hint_func
from level1 import level_1
from level2 import level_2
from level3 import level_3
from select_char import select_character_fun
from customise_dragon import customise_dragon
from get_wepons import get_dragon_weapons


def main():
    try:
        get_or_create_account()
        with open("account.json", "r") as accout_detail:
            if accout_detail is not None:
                game_heading(15, "")
                select_character_fun()
                customise_dragon()
                get_dragon_weapons()
                hint_func()

                game_heading(15, "Game started! Level One")
                level_1()

                game_heading(15, " Level Two")
                level_2()

                game_heading(15, " Level three")
                level_3()
    except KeyboardInterrupt:
        game_heading(20, "Game canceled. You can continue later")


main()
