import json
import os
from  heading_func import game_heading
from level1 import get_monsters
from utils_func import *
from select_char import get_charatter


user_account = {"username":"","password":"","health":100, "character":"", "weapons":"", "costumes":""}

def create_account():
        print("")
        print("")
        game_heading(number=15, text="get an account and start gaming....... ")
    
        print("Do you want to create account?   ")
        print("1) Yes")
        print("2) No")
        confirm_create = int(input())
        if confirm_create == 1:
            username = input("Username --->  ")
            password = input("Password  --->  ")
            with open("account.json", "w" ) as account_detail:
                user_account["username"] = username
                user_account["password"] = password
                json.dump(user_account, account_detail)
        elif confirm_create == 2:
            print("Thanks")
            
        else:
            print("Command Not Recongnized")

def get_account_and_continue():
        game_heading(number=15, text="Welcome!  Login to Continue")
        account_found = False
        while account_found == False:
            username = input("Username --->  ")
            password = input("Password  --->  ")
            with open("account.json", "r") as account_detail:
                if account_detail is not None:
                    active_user = json.load(account_detail)
                    if active_user["username"] == username and active_user["password"] == password:
                        print("Welcome!!!", active_user["username"].upper())
                        account_found
                        account_found = True
                        
                    else:
                        game_heading(10,"Username or password incorrect")
                        print("")
                        print("Try again!!!")
                        
                    
                        
        if len(get_monsters()) > 0:
            
                print("do you want to continue your game")
            
                print("""
                    yes?/y
                    no/n
                    
                    """)
                continue_game = input("---> ").lower()
                
                if continue_game == "no" or continue_game == "n":
                    try:
                        monsters = get_monsters()
                        for monster in monsters:
                            os.remove(monster)
                    except :
                        pass
                    new_game()
                    get_charatter()
                    
                    
                elif continue_game == "yes" or continue_game == "y":
                    pass
                else:
                    print("Invalid commmand")
        elif len(get_monsters()) == 0:
            new_game()
                    
def get_or_create_account():  
        game_heading(text="Don't have an account? Press ctrl F2 (or ctrl C on window terminal) to an create account or Quit the game")
        try:
            get_account_and_continue()
        except KeyboardInterrupt:
            create_account()
        except FileNotFoundError:
           create_account()