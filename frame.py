# import components of board so that we can call the board class from here
from board import *

class Frame:
    
    '''
    this very first function will set the background and fonts of root window
    '''
    def __init__(self, root):
        self.root = root
        
        # change the background and fonts of buttons and labels in header frame
        self.style = ttk.Style()
        self.style.configure('TButton', background = 'sky blue')
        self.style.configure('TLabel', background = 'sky blue', font = ('Courier', 15))
        
        # initialize total number of rows and columns of game board
        # this is the minimum number of rows and columns which will be present.
        self.no_of_rows = 3
        self.no_of_columns = 3
        
    '''
    create the function to make first frame
    this frame will include some buttons and labels and statistics.
    this frame will be called or created at once on starting the app.
    '''
    def create_first_frame(self):
        
        # create first frame in root window
        self.frame_header = LabelFrame(self.root, height = 356, width = 356, text = 'Game Statics', bg = 'light green')
        
        # pack the frame header
        self.frame_header.pack()     

    '''
    create a function to make second frame for game
    This function will be used again and againg as we start the game
    and will create a new frame every time for every new board
    '''
    def create_board_frame(self):
        self.next_frame = LabelFrame(self.root, height = 356, width = 356, text = 'Game Board', bg = 'light green')
        self.next_frame.pack()
        return self.next_frame
        
    '''
    the first frame include the buttons to start the game,
    to quit the window
    or to watch the statistics like, how much player scored,
    or total time
    '''
    def design_first_frame(self):
        
        # create a button to start the game 
        # when this Start button is press the "start_new_game" function will be called
        start_button = ttk.Button(self.frame_header, text = 'Start', command = self.start_new_game)
        start_button.grid(row=0, column = 0, padx = 5)
        
        # create a button to quit the game
        # this will close the whole root window
        # when this Start button is press the "end_game" function will be called
        quit_button = ttk.Button(self.frame_header, text = 'Quit', command = self.end_game)
        quit_button.grid(row = 2, column = 0, padx = 5)
        
        # add text labels which will define, how well the player played
        # text1 = maximum time that can be consumed to complete the level
        self.text1 = ttk.Label(self.frame_header, text = " Total time taken: ")
        self.text1.grid(row = 0, column = 1, padx = 20, pady = 3, sticky= 'ne')
        self.text1.config(relief = RIDGE)
        
        #text2 = total points collected by player
        self.text2 = ttk.Label(self.frame_header, text = ' Points Collected: ')
        self.text2.grid(row = 1, column = 1, padx = 20, pady = 3, sticky= 'e')
        self.text2.config(relief = RIDGE)
        
        # text3 = time taken by player to complete the level
        self.text3 = ttk.Label(self.frame_header, text = ' Your time taken : ')
        self.text3.grid(row = 2, column = 1, padx = 20, pady = 3, sticky= 'se')
        self.text3.config(relief = RIDGE)
        
        # add values to the above text1 Label
        self.total_time = ttk.Label(self.frame_header, text = '00:00')
        self.total_time.grid(row = 0, column = 2, padx = 20, pady = 3, sticky= 'se')
        self.total_time.config(relief = RIDGE)
        
        # add values to the above text2 Label
        self.Points_Collected = ttk.Label(self.frame_header, text = '    0')
        self.Points_Collected.grid(row = 1, column = 2, padx = 20, pady = 3, sticky= 'se')
        self.Points_Collected.config(relief = RIDGE)
        
        # add values to the above text3 Label
        self.time_taken = ttk.Label(self.frame_header, text = '0 sec')
        self.time_taken.grid(row = 2, column = 2, padx = 20, pady = 3, sticky= 'se')
        self.time_taken.config(relief = RIDGE)

    '''
    this function will be called on starting of every new game
    it sets the board and frame for the player
    '''
    def start_new_game(self):
        
        # destroy the empty frame
        self.next_frame.destroy()
        
        # create a new frame for board
        self.board_frame = self.create_board_frame()
        
        # increase the number of rows by one for every new continuous game.
        self.no_of_rows += 1
        
        # increase the number of columns by one for every new continuous game.
        self.no_of_columns += 1
        
        # create an object of board
        # pass the references of root and frame,
        # with the number of rows and columns
        self.board = Board(self.root, self.board_frame, self, self.no_of_rows, self.no_of_columns)
        
        # create a canvas on frame
        canvas = self.board.add_canvas()
        
        # call the function to design the board cells
        self.board.design_board()
        
        # add a player block 
        self.board.player_design()
        
        # add a destination block
        self.board.add_goal_block()
        
        # bind the movement keys on root window
        self.board.set_movement_keys()
        
    '''
    This function will be called on pressing the Quit window
    or if player wants to quit the game from pop up.
    This function will close the whole root window.
    '''
    def end_game(self):
        self.root.destroy()
