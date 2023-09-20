import json
from heading_func import game_heading
from utils_func import get_monsters

active_monster = {"name":"", "health":100, "max_decrease":10, "min_decrease": 5}


def picked(character):
   with open ("account.json", "r") as user_detail:
       active_user = json.load(user_detail)
       
       active_user["character"] = character
       
       with open("account.json", "w") as user_detail:
           json.dump(active_user, user_detail)
       

def get_charatter():
        game_heading(number=15, text="Welcome to the game World")
        print("""
            select your Dragon character
                1):  vhagar
                2):  dreamfyre
                3):  sunfrye
                4):  seasmoke
            """
            )
        
        option = int(input())
        dragons = [ "vhagar", "dreamfyre",  "sunfrye", "seasmoke"]
        selected_character = dragons[option - 1]
        monsters = []
        playing_dragon = []
        if selected_character in dragons:
            for dragon in dragons:
                if dragon != selected_character:
                    monsters.append(dragon)
            playing_dragon.append(selected_character)
            picked(playing_dragon[0])
        else:
            game_heading(15, "No charater selected! ")
        
        for monster in monsters:
            try:
                with open(monster+".json", "r") as monster_fight:
                    active_monsters = json.load(monster_fight)
                    if active_monsters == None:
                        with open(monster+".json", "w") as monster_fight:
                            active_monsters["health"] = 100
                            json.dumps(active_monsters, monster_fight)
                    else:
                        pass
            except:
                with open(monster+".json", "w")as create_monster:
                    active_monster["name"] = monster
                    json.dump(active_monster, create_monster)    
       
def select_character_fun():
    if len(get_monsters()) > 0:
        pass
    else:
        get_charatter()
                
                
       
 
            