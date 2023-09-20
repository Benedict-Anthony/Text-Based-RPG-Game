import json
from game.customise_dragon import customise
from heading_func import game_heading


def get_weapons():
    costumes = {
        "g":"golden wings",
        "e":"eye of horis",
        "h":"haddies sheild"
    }
    
    print ("""
           Do you want to update weapons?
           
           yes/n
           no/n
           
           
           """)
    update_weapon = input("-----> ")
    game_heading(20, "select two costume")
    
    print("""
          g): golden wings
          e): eye of horis,
          h): haddies sheild
          
          """)
    selected_weapons =[]
    if update_weapon == "yes" or update_weapon == "y":
        while len(selected_weapons) < 2:
            choices = input("costume -----> ").lower()
            if choices != "skip":
                for chr in choices:
                    if chr in costumes.keys():  
                        selected_weapons.append(costumes.get(chr))
                        print(costumes.get(chr), "has been added to your list of costumes")
                        game_heading(15, "")
                        
                    
                    else:
                        print("invalid!!!, Select a key relating to the options provided")
    else:
        pass
            

    with open("account.json", "r") as account_detail:
        active_user = json.load(account_detail)
        active_user["weapons"] = selected_weapons
        
        with open("account.json", "w") as account_detail:
            json.dump(active_user, account_detail)

def get_dragon_weapons():
   game_heading(15, "Now get your weapons!")
   get_weapons()
   get_weapons = True
   while get_weapons == True:
        print("""
                1) dragon information
                2) get weapons and customise Your dragon
                3) Skip
                
                """)
        choices = int(input())
        
        if choices == 1:
            with open("account.json", "r") as account_detail:
                active_user = json.load(account_detail)
                print(" character --->  ", active_user.get("character"), "")
                print(" health --->  ", active_user.get("health"), )
                print(" costumes --->  ", active_user.get("costumes"), )
                if active_user.get("weapons") is None:
                    print(" costume --->  ", active_user.get("weapon"), "You have no custome yet")
                else:
                    print(" costume --->  ", active_user.get("weapons"))
                    
                print("""
                      Do you wish get weapons for your dragon?
                      
                      Yes/Y:
                      No/N:
                      """)
                
                choice = input("---> ").lower()
                
                if choice == "y" or choice =="yes":
                    customise()
                elif choice == "n" or choice == "no":
                    get_weapons = False
        elif  choices == 2:
            customise()
        elif choices == 3:
            customizing_dragon = False
        else:
            print("such command allowed Invalid")