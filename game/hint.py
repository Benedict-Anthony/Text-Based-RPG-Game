from heading_func import game_heading


def hint_func():
    print("want to take a quick guild?")
    
    print("""
          
          help) :help
          skip) :skip
          
          """)
    choice = input("----->  ")
    if choice == "help":
        game_heading(15, "the following command help you to defeat you enemy")
        
        print("""
              a) attack ------> This command help you strike and decrease the monster's life.
              
              
              s) stealth ------> this give you the ability to target before attacking
              
              
              r) run -----> when you are running out of life, be sure to run while you keep attacking
              
              
              h) heal ------> this will heal you up with a heal up with random number ranging from 1 to 5
              
              
              d) defend ----> this give you the ability to defend the monsters attack. Not you can't predict the monster's attack
              
              
              
              """)
        
        game_heading(15, "Press any key to start")
        start_game = input("--------> click OK")
    elif choice == "skip":
        game_heading(15, "Press any key to start")
        start_game = input("--------> click OK")