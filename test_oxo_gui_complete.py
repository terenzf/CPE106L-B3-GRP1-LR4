import unittest
from oxo_gui_complete import game

class test_game(unittest.TestCase):
    def test_game_new(self):
        t = game()
        self.assertEqual(list(" " * 9), t.newGame())
        
    def test_game_win(self):
        t = game()
        self.assertTrue(t._win("XXX    "))
        self.assertTrue(t._win("X X X "))
        self.assertTrue(t._win("X  X  X"))
        
    def test_game_auto_move(self):
        t = game()
        self.assertIn(t._auto_move(t.newGame()), [0,1,2,3,4,5,6,7,8])
        self.assertEqual(t._auto_move("XXXXXXXXX"), -1)
        
if __name__=='__main__': unittest.main()
