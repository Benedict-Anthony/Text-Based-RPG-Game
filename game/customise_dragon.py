import json
from heading_func import game_heading


def customise():
    costumes = {
        "w":"wing",
        "s":"sheild",
        "a":"amor"
    }
    
    game_heading(20, "select two costume")
    
    print(""" 
          w): wing
          s): sheild,
          a): amor
          
          """)
    selected_costumes =[]
    while len(selected_costumes) < 2:
        costume = input("costume -----> ")[0]
        for chr in costume:
           if chr in costumes.keys():
            selected_costumes.append(costumes.get(chr))
            print(costumes.get(chr), "has been added to your list of costumes")
           else:
               print("invalid!!!, Select a key relating to the options provided")

    with open("account.json", "r") as account_detail:
        active_user = json.load(account_detail)
        active_user["costumes"] = selected_costumes
        
        with open("account.json", "w") as account_detail:
            json.dump(active_user, account_detail)

def customise_dragon():
   game_heading(15, "Get ready to defeat anyone who dares you!")
   customizing_dragon = True
   while customizing_dragon == True:
        print("""
                1) dragon information
                2) get costumes and customise Your dragon
                3) Skip
                
                """)
        choices = int(input())
        
        if choices == 1:
            with open("account.json", "r") as account_detail:
                active_user = json.load(account_detail)
                print(" character --->  ", active_user.get("character"), "")
                print(" health --->  ", active_user.get("health"), )
                if active_user.get("costumes") is None or active_user.get("weapons") is None:
                    print(" costume --->  " "You have no custome yet")
                    print(" costume --->  " "You have no weapons yet")
                else:
                    print(" costume --->  ", active_user.get("costumes"))
                    print(" weapons--->  ", active_user.get("weapons"))
                    
                print("""
                      Do you wish get costumes for your dragon?
                      
                      Yes/Y:
                      No/N:
                      """)
                
                choice = input("---> ").lower()
                
                if choice == "y" or choice =="yes":
                    customise()
                elif choice == "n" or choice == "no":
                    customizing_dragon = False
        elif  choices == 2:
            customise()
        elif choices == 3:
            customizing_dragon = False
        else:
            print("such command allowed Invalid")