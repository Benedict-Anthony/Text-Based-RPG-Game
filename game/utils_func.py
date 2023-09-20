import json
from random import randint
import os


# get the current moster life from the directory
def get_current_level_moster(monster):
    with open(monster, "r") as level_one_monster:
        fighting_monster = json.load(level_one_monster)
        return fighting_monster

# this get the active user charater 
def get_dragon():
    with open("account.json", "r") as level_one_dragon:
        fighting_dragon = json.load(level_one_dragon)
        return fighting_dragon

# this helps to reduce the monster life by a random number depending on the monster fighting
def decrease_monster_health(monster):
    health = randint(monster.get("min_decrease"), monster.get("max_decrease"))
    return health

# save progress after wining each round
def save_progress(dragon, account):
    with open(account+".json", "r") as save_progress:
        active_user = json.load(save_progress)
        active_user = dragon
        
        with open(account+".json", "w") as save_progress:
            json.dump(active_user, save_progress)


#  decrease player health randomly on every attack
def decrease_dragon_health():
    health = randint(1, 5)
    return health

#  increase player health randomly on every heal
def increase_dragon_health():
    health = randint(1, 10)
    return health

# show ths statistics of the player and monster health
def show_game_progress(dragon, moster):
    print("")
    print("")
    print("Moster", dragon["name"], "health",dragon["health"])
    print("")
    print("")
    print("Player", moster["username"], "health", moster["health"])
    
    
# this help to start a new game


def new_game():
    with open("account.json", "r") as account_detail:
        active_user = json.load(account_detail)
        active_user["health"] = 100
        
        with open("account.json", "w") as account_detail:
            json.dump(active_user, account_detail)
  
            
            
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
    
    monsters.reverse()
    return monsters



    