import os, random
#import oxo_data file
import oxo_data
#Game Class, a class is a blueprint for an object and an object is a collection of data and methods
class Game():
#Constructor function, this type of function is used to initialize the variables of an object
#This special function is called whenever a new object of this class is initiated
#The self parameter is the object itself

    def __init__(self):
     self.board = list(" " * 9)

# This function saves the game by saving the board variable of the object to oxo_data by 
# calling the function saveGame defined inside oxo_data.
# oxo_data has already been imported in line number 2

    def save(self, game):
        ' save game to disk '
        oxo_data.saveGame(self.board)

#Function for restoring previously saved game by calling restoreGame defined in the oxo_data file
    def restore(self):
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
#Assign value returned by restoreGame() function
            self.board = oxo_data.restoreGame()
#If restoreGame doesn't return valid value or returns an error, initialize a new board
#The code list(" " * 9) creates a list with 9 space characters
            if len(self.board) != 9:
                self.board = list(" " * 9)
            return self.board
        except IOError:
            self.board = list(" " * 9)
        return self.board
#Function for generating random cell

    def _generateMove(self):
        ''' generate a random cell from those available.
        If all cells are used return -1'''
#Generate list of options available by going through the board and checking if any empty cell is available
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
#Generate a random choice from options if options has any valid element, otherwise return -1
        if options:
            return random.choice(options)
        else: return -1

#Function for checking winning move
    def _isWinningMove(self):
#Intialize wins as a list of combinations of cell needed for winning
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))
#Initialize game with the current value of board
        game = self.board
#Loop for checking if the combinations defined in wins all contains X or O
        for a, b, c in wins:
#Chars contains current combination from board
            chars = game[a] + game[b] + game[c]
#If this is the winning move return true else return false
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

#Function for users move
    def userMove(self, cell):
#If cell is not empty raise error
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
#Else Fill Cell
        else:
            self.board[cell] = 'X'
#If isWinningMove returns true return X else return empty string
        if self._isWinningMove():
            return 'X'
        else:
            return ""

#Function for computers move
    def computerMove(self):
#Call the generateMove function and assign to cell
        cell = self._generateMove()
#If -1 return D
        if cell == -1:
            return 'D'
#Fill value O in board
        self.board[cell] = 'O'
#If isWinningMove returns true return O else return empty string
        if self._isWinningMove():
            return 'O'
        else:
            return ""

#Function for testing the game
def test():
#Intialize result as empty string
        result = ""
#Call game function
        game = Game()
#Loop until there is a winner
        while not result:
            print(game.board)
#Generate users move if possible or raise error
            try:
                result = game.userMove(game._generateMove())
            except ValueError:
                print("Oops, that shouldn't happen")
#Generate computers move if result is still empty
            if not result:
                result = game.computerMove()
#If result is empty continue this loop
            if not result:
                continue
#If result is D, print Draw
            elif result == 'D':
                print("Its a draw")
#Else print the winner
            else:
                print("Winner is:", result)
#Print game board
                print(game.board)

#Run the test() function if the file is not being imported

if __name__ == "__main__":
    test()