import collections
import random

'''
Game class to manage TicTacToe methods
'''


class Tic_Tac_Toe:
    def __init__(self):
        self.blocks = collections.defaultdict(set)
        self.board = self.create_board()
        self.block_states = [["-"] * 3 for _ in range(3)]
        self.current_player = None
        self.offsets = {0: [0, 0], 1: [0, 1], 2: [0, 2], 3: [1, 0], 4: [1, 1], 5: [1, 2], 6: [2, 0], 7: [2, 1], 8: [2, 2]}
        self.possible_patterns = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                                  ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                                  ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
        self.winner = None

    def get_valid_positions(self,board):
        positions = set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == "-":
                    for number, block in self.blocks.items():
                        if (i,j) in block:
                            break
                    offseti, offsetj = self.offsets[number]
                    if self.block_states[offseti][offsetj] == "-":
                        positions.add((i,j))
        return positions

    def create_board(self):
        board = [["-"] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if i//3 == 0 and j//3 == 0:
                    self.blocks[0].add((i,j))
                if i//3 == 0 and j//3 == 1:
                    self.blocks[1].add((i,j))
                if i//3 == 0 and j//3 == 2:
                    self.blocks[2].add((i,j))
                if i//3 == 1 and j//3 == 0:
                    self.blocks[3].add((i,j))
                if i//3 == 1 and j//3 == 1:
                    self.blocks[4].add((i,j))
                if i//3 == 1 and j//3 == 2:
                    self.blocks[5].add((i,j))
                if i//3 == 2 and j//3 == 0:
                    self.blocks[6].add((i,j))
                if i//3 == 2 and j//3 == 1:
                    self.blocks[7].add((i,j))
                if i//3 == 2 and j//3 == 2:
                    self.blocks[8].add((i,j))
        return board

    def print_board(self,board):
        print('======= Game Board =======')
        for i in range(9):
            if i > 0 and i % 3 == 0:
                print("")
            string = ""
            for j in range(9):
                if j > 0 and j % 3 == 0:
                    string += (" " + board[i][j])
                else:
                    string += (board[i][j])

            print(string)

        print("==========================")
        print('======= Block Status =====')
        for i in range(3):
            string = ""
            for j in range(3):
                string += (" " + self.block_states[i][j])
            print(string)
        print("==========================")

    def is_finished(self):
        if self.winner:
            return True
        if not self.get_valid_positions(self.board):
            return True
        return False

    def get_winner(self):
        if self.winner:
            return self.winner
        else:
            return None

    def check_block(self, num, isFinal):
        if isFinal:
            board = self.block_states
        else:
            board = self.board
        offseti,offsetj = self.offsets[num]
        for pattern in self.possible_patterns:
            sol = set()
            for each in pattern:
                sol.add(board[each[0]+(offseti*3)][each[1]+(offsetj*3)])

            if len(sol) == 1 and "-" not in sol:
                block_winner = sol.pop()
                if isFinal:
                    self.winner = block_winner
                    return
                print((offseti,offsetj))
                self.block_states[offseti][offsetj] = block_winner
                # for p in self.blocks[num]:
                #     board[p[0]][p[1]] = self.current_player.symbol
                return
        return False

    def update_board(self,pos):
        self.board[pos[0]][pos[1]] = self.current_player.symbol
        cur_block,block_num = None,None
        for number,block in self.blocks.items():
            if pos in block:
                block_num,cur_block = number,block
                break
        self.check_block(block_num, False)

    def run_game(self,player1, player2):
        if player1.symbol == "0":
            temp = player1
            player1 = player2
            player2 = temp
        self.current_player = player1
        while(not self.is_finished()):
            if self.current_player.__class__.__name__ == "Player":
                print("Playing : player " + self.current_player.name)
            else:
                print("Playing : Bot")
            self.print_board(self.board)
            pos = self.current_player.move()
            if self.current_player.__class__.__name__ == "Player":
                print("Player " + self.current_player.name + " moved at : " + str(pos))
            else:
                print("Bot moved at : " + str(pos))
            self.update_board(pos)
            if self.current_player == player1:
                self.current_player = player2
            else:
                self.current_player = player1
            self.check_block(0, True)
        if not(self.get_winner()):
            print("DRAW")
        else:
            print("Winner is", self.get_winner())
        print("Winning board")
        self.print_board(self.board)

'''
    Player class 
'''


class Player:
    def __init__(self, name: str, game: Tic_Tac_Toe):
        self.name = name
        self.game = game
        self.symbol = None

    def move(self):
        pos = input("Enter valid input in format x y\n")
        while True:
            if pos.lower().strip() == "exit":
                exit()
            pos = pos.strip().split(" ")
            for i in pos:
                if not i.isnumeric():
                    pos = input("Invalid position Enter valid input\n")
                    continue
            pos = tuple(int(i) for i in pos)
            if len(pos) == 2 and (pos in self.game.get_valid_positions(self.game.board)):
                break
            else:
                pos = input("Invalid position Enter valid input in the format x y\n")
        return pos

    def set_symbol(self,symbol):
        self.symbol = symbol


'''
    Bot class 
'''


class Bot:

    def __init__(self, game):
        self.temp = 0
        self.game = game
        self.symbol = None

    def move(self):
        possible_positions = list(self.game.get_valid_positions(self.game.board))
        return possible_positions[random.randrange(len(possible_positions))]

    def set_symbol(self,symbol):
        self.symbol = symbol


'''
    Driver program
'''
if __name__ == "__main__":
    game = Tic_Tac_Toe()
    symbols = {}
    symbols[1] = "X"
    symbols[0] = "0"

    while True:
        choice = input("Choose type of game \n 1.Player V Player \n 2.Player V Bot\n")
        if choice.strip().isnumeric() and int(choice.strip()) == 1 or int(choice.strip()) == 2:
            choice = int(choice.strip())
            break
        print("Invalid choice")
    if choice == 1:
        name1 = input("Enter name for player 1\n")
        name2 = input("Enter name for player 2\n")
        player1 = Player(name1,game)
        player2 = Player(name2,game)
    elif choice == 2:
        name = input("Enter name for player\n")
        player1 = Player(name,game)
        player2 = Bot(game)

    num = random.uniform(0, 1)
    if num > 0.5:
        player1.set_symbol(symbols[0])
        player2.set_symbol(symbols[1])
    else:
        player1.set_symbol(symbols[1])
        player2.set_symbol(symbols[0])

    if choice == 1:
        print("Player " + player1.name + "is randomly assigned symbol : " + player1.symbol)
        print("Player " + player2.name + "is randomly assigned symbol : " + player2.symbol)
    if choice == 2:
        print("Player " + player1.name + "is randomly assigned symbol : " + player1.symbol)
        print("Bot is randomly assigned symbol : " + player2.symbol)

    game.run_game(player1,player2)

