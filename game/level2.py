import json
from random import randint
import random
from heading_func import game_heading
from utils_func import *
import os

monsters = []


def get_monsters():
    list_dirs = os.listdir()

    for monster in list_dirs:
        if monster.endswith(".json"):
            monsters.append(monster)
        else:
            pass

    if "account.json" in monsters:
        monsters.remove("account.json")
    if len(monsters) == 0:
        monsters.append()
    monsters.reverse()
    return monsters


def level_2():
    fighting_user = get_dragon()
    active_fighting_monster = get_current_level_moster(get_monsters()[1])
    healing_count = 0
    game_active = True
    monster_attack_part = ["neck", "leg", "chest", "eyes", "back"]

    game_heading(15, "Level Two! " + active_fighting_monster["name"] + " is not happy, Fight and pull him down")
    if active_fighting_monster["health"] <= 0:
        game_active = False
    game_heading(15, "the following command help you to defeat you enemy")

    while game_active:
        if active_fighting_monster["health"] <= 0 or fighting_user["health"] < 0:
            game_active = False
        print("""
            a) attack
            h) heal
            s) stealth
            r) run
            
            """)
        monster_attack_chance = randint(1, 5)
        attacked_part = random.choice(monster_attack_part)

        choice = input("---->  ").lower()
        if choice == "attack" or choice == "a":

            print("great strike on " + active_fighting_monster['name'] + "'s  " + attacked_part)
            fighting_user["health"] = fighting_user["health"] - decrease_dragon_health()
            active_fighting_monster["health"] = active_fighting_monster["health"] - decrease_monster_health(
                active_fighting_monster)

            if monster_attack_chance == 4 or monster_attack_chance / 2 == 1:
                game_heading(15, "Woo, That was strike from  " + active_fighting_monster['name'] + "'s  " + "on you")

                fighting_user["health"] = fighting_user["health"] - decrease_dragon_health() * 5

            show_game_progress(active_fighting_monster, fighting_user)
            game_heading(15, "")

            if active_fighting_monster["health"] <= 0:
                print("You Win")
                save_progress(fighting_user, "account")
                save_progress(active_fighting_monster, "sunfrye")
                game_active = False

            if fighting_user["health"] <= 0:
                print("You loose")
                save_progress(fighting_user, "account")
                save_progress(active_fighting_monster, "sunfrye")
                game_active = False

            save_progress(fighting_user, "account")
            save_progress(active_fighting_monster, active_fighting_monster["name"])


        elif choice == "stealth" or choice == "s":
            print("targetting the monster...........")
        elif choice == "defend" or choice == "d" and monster_attack_chance == 4:
            print("That was a good defense from " + active_fighting_monster["name"] + " s atack")
        elif choice == "defend" or choice == "d" and monster_attack_chance != 4:
            print(active_fighting_monster["name"] + " is trying to defend, Remember to defend!!")
        elif choice == "heal" or choice == "h":

            if fighting_user["health"] >= 100:
                print("full health! can't increase health")
            else:
                healing_count = healing_count + 1
                if healing_count >= 4 or healing_count <= 0:
                    game_heading(15, "can't heal now! Try again later")
                    healing_count = -3
                else:
                    fighting_user["health"] = fighting_user["health"] + increase_dragon_health()

            show_game_progress(active_fighting_monster, fighting_user)

        elif choice == "run" or choice == "r":
            print("running......")
            print(active_fighting_monster["name"], "is striking. ")
            print("Fight back before you run out of life")
        else:
            pass
