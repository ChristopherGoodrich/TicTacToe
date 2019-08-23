class TicTacToe():

    # winning combos
    wins = (('A1', 'B1', 'C1'),
            ('A2', 'B2', 'C2'),
            ('A3', 'B3', 'C3'),
            ('A1', 'A2', 'A3'),
            ('B1', 'B2', 'B3'),
            ('C1', 'C2', 'C3'),
            ('A1', 'B2', 'C3'),
            ('A3', 'B2', 'C1'))

    # tuple of all cells in tic-tac-toe board
    cells = ('A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3')

    def __init__(self, player1='player1', player2='player1'):

        self.board = dict.fromkeys(self.cells, ' ')

        self.player1_name = player1 + " ('X')"
        self.player2_name = player2 + " ('O')"
        self.current_player = self.player1_name
        
        self.next_turn = 'X'
        self.last_cell = ''
        self.winner = ''

        self.game_turn = 0
        self.game_over = 0

        self.print_tutorial()
        self.play_game()

    def print_tutorial(self):
        print('\n\nWelcome to Tic-Tac-Toe')
        print('\nThe rules are simple. Starting with ' + self.player1_name + ',')
        print('each player will place one mark on the board per turn.')
        print('This repeats until one player has three of their marks')
        print('in a row, column, or either diagonal direction. If after 9')
        print('turns neither player has won, the game is a tie.')
        print('\nValid cell choices: ' + ', '.join(self.cells) + ', RESET, and END')
        print('\nA1-C3: Places current player\'s mark in the corresponding cell.')
        print('RESET: This will reset the current board and start the game anew.')
        print('END: This will immediately stop the game and exit the program.')
        self.draw_board()

    # starts a game, which on conclusion is the end of the program
    def play_game(self):
        while self.game_over != 1:
            self.take_turn()

    # each call represents one player's turn. options here to end or reset the
    # game 
    def take_turn(self):
        cell_choice = input('\n' + self.current_player + ', what cell do you choose? ').upper()

        # options to end the game or reset it
        if cell_choice == 'END':
            print('\nYou have terminated the game.')
            self.game_over = 1
            return
        elif cell_choice == 'RESET':
            print('\nRestarting the game.')
            self.__init__(self.player1_name, self.player2_name)
            return

        # checks if valid cell choice, if it is then turn continues
        if cell_choice not in self.cells:
            print('\ninvalid cell choice')
            return
        elif self.board[cell_choice] != ' ':
            print('\nThat cell has already been selected. Choose again.')
            return
        else:
            self.update_board(cell_choice)
            self.draw_board()
            if self.game_turn >= 5:
                self.check_win()

    # updates board state and variables that remember player order and symbol
    def update_board(self, cell_choice):
        self.game_turn += 1

        self.board[cell_choice] = self.next_turn
        self.last_cell = cell_choice

        if self.next_turn == 'X':
            self.next_turn = 'O'
            self.current_player = self.player2_name
        else:
            self.next_turn = 'X'
            self.current_player = self.player1_name
                    
    # prints board to console as well as round and player info
    def draw_board(self):
        print('\n  Round ' + str(self.game_turn) + ' - Next symbol is \'' + self.next_turn + '\'.\n')
        print('          A   B   C')
        print('        -------------')
        print('      1 | ' + self.board['A1'] + ' | ' + self.board['B1'] + ' | ' + self.board['C1'] + ' |')
        print('        -------------')
        print('      2 | ' + self.board['A2'] + ' | ' + self.board['B2'] + ' | ' + self.board['C2'] + ' |')
        print('        -------------')
        print('      3 | ' + self.board['A3'] + ' | ' + self.board['B3'] + ' | ' + self.board['C3'] + ' |')
        print('        -------------')

    # checks if either player has won or 9 turns have been played. If they have 
    # won self.game_over is set as 1, which ends the while loop and program.
    def check_win(self):

        for seq in self.wins:
            if self.last_cell in seq:
                if (self.board[seq[0]] == self.board[seq[1]]
                    and self.board[seq[0]] == self.board[seq[2]]):
                        self.game_over = 1
                        if self.next_turn == 'O':
                            win_name = self.player1_name
                        else:
                            win_name = self.player2_name                             
                        print('\n' + win_name + ' is the winner!')
                        return
        
        if self.game_turn == 9:
            self.game_over = 1
            print('\nThis game has resulted in a very boring tie.')
            return

################################################################################
TicTacToe()