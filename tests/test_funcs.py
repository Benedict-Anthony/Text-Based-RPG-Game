from random import randint
import unittest
from game.utils_func import decrease_monster_health
from game.utils_func import get_dragon
from game.utils_func import get_current_level_moster

class MudGameTest(unittest.TestCase):
    def test_active_dragon(self):
        print("sucess")
        self.assertEquals({"username": "ben", "password": "123", "health": 100, "character": "vhagar", "weapons": [], "costumes": ["amor", "amor"]}, get_dragon() )
        
    def test_get_current_level_moster(self):
        self.assertEquals(get_current_level_moster("seasmoke.json"), {"name": "seasmoke", "health": 100, "max_decrease": 10, "min_decrease": 5})
        
    def text_decrease_monster_health(self):
        self.assertEqual(randint(5, 10), decrease_monster_health("seasmoke.json"))

if __name__ == "__main__":
    unittest.main()
