# import random to use randint function
import random

# import tkinter to work with gui
from tkinter import *
from tkinter import ttk

# import messagebox to show a pop on some event
from tkinter import messagebox

class Board:
    def __init__(self, root, board_frame, frame, no_of_rows, no_of_columns):
    
        # initialize some basic configurations
        # this is reference of root window
        self.root = root
        
        # this is reference of object Frame class
        self.frame = frame
        
        # this is reference of second frame on which game board will be made
        self.board_frame = board_frame
        
        # row_num and col_num varialble will track the current cell of player
        self.row_num = 0
        self.col_num = 0
        
        # prev_row_num and prev_col_num variable will track the cell which is one step back of player
        # or the previous cell
        self.prev_row_num = 0
        self.prev_col_num = 0
        
        # store the total number of rows and columns
        self.no_of_rows = no_of_rows
        self.no_of_columns = no_of_columns
        
        # initialize the destination of goal block
        # which will be changed in every next game
        self.goal_position = [0,0]
    
    '''
    here the canvas function is defined
    it will configure the width, height and background of canvas.
    This canvas is made on second frame of root
    that's why reference of board_frame is given as parameter in Canvas function
    '''
    def add_canvas(self):
        self.canvas = Canvas(self.board_frame)
        self.canvas.pack()
        self.canvas.config(width = 350, height = 350, bg = 'light green')

    '''
    this function is used to design only the board
    board will have square shape cells and
    
    the starting and last point of every cell is stored as list
    in a 2d list - dimensions
    
    To configure the cells, reference of each cell is stored in a 2d list - list_of_boxes
    on every cell weight of each cell is allocated dynamically using randint function
    and stored in the 2d list - paths
    '''
    def design_board(self):
        self.list_of_boxes = []
        self.dimensions = []
        self.paths = []
        
        # (x1, y1) --> is starting point of each cell
        # (x2, y2) --> is last point of each cell
        y1 = 10
        y2 = 60
        
        # this loop will go through all the rows of board
        for rows in range(self.no_of_rows):
            # x1 is started from negative so that it will become equal on adding in function
            x1 = -40
            x2 = 10
            
            # row, dimension and path are local variables
            # these are used to append in variables
            # list_of_boxes, dimensions, paths respectively
            row = []
            dimension = []
            path = []
            
            # this loop will go through all the columns of each row
            for columns in range(self.no_of_columns):
                dimension.append([x1+50, y1, x2+50, y2])
                
                # add rectangular boxes to canvas and configure the background
                box = self.canvas.create_rectangle(x1+50, y1, x2+50, y2)
                self.canvas.itemconfigure(box, fill = 'light yellow')
                row.append(box)
                
                # select an integer between 1 to 9 randomly
                # and add it to list path
                Path = str(random.randint(1,9))
                path.append(Path)
                
                # add the integer as a text to each cell
                # this integer will denote the weight of cell
                text = self.canvas.create_text(x1+50+25, y1+25, text = Path)
                
                # configure the text color same as cell color
                # so that only text of next step from current step can be highlighted
                self.canvas.itemconfigure(text, fill = 'light yellow')
                
                # increase the value of x axis to draw next cell
                x1 += 50
                x2 += 50
                
            # append path of each row in a 2d list paths
            self.paths.append(path)
            
            # append dimension of each cell in that that row in the list dimensions
            self.dimensions.append(dimension)
            
            # append the reference of each boxes in each row in the list list_of_boxes
            self.list_of_boxes.append(row)
            
            # increase the y-ais
            y1 += 50
            y2 += 50
            
        # total_points variable stores the total number of points a player achieved
        # initialize it with the weight of the first cell
        # which will be increased step by step as player moved
        self.total_points = int(self.paths[0][0])
        Points_Collected_text = "    " + str(self.total_points)
        
        # update the value of text3 i.e. Points_Collected in first frame
        self.frame.Points_Collected.config(text = Points_Collected_text)
            
    # add goal block of oval shape with black color with white text
    def add_goal_block(self):
    
        # select a random position for goal,
        # select random row number and column number
        # which should not be greater than total number of rows and columns
        # and create a list goal_position
        self.goal_position[0] = random.randint(1,self.no_of_rows-1)
        self.goal_position[1] = random.randint(1,self.no_of_columns-1)
        
        # pick the dimensions of that goal position and assign the location for goal
        goal_location = self.dimensions[self.goal_position[0]][self.goal_position[1]]
        
        # add a fixed goal of oval shape on that location
        # and configure the backgound as red
        self.goal = self.canvas.create_oval(goal_location)
        self.canvas.itemconfigure(self.goal, fill = 'red')
        
        # set the text on goal box
        # and configure the color as black
        self.goal_text = self.canvas.create_text(
			goal_location[0]+25, 
			goal_location[1]+25, 
			text = "Goal")
        self.canvas.itemconfigure(self.goal_text, fill = 'black')

    '''
    this is the block of code which define the player
    which can move back and forth, up and down,
    and by which player plays the game
    '''
    def player_design(self):
        
        # these next two lines are to delete the previous player block at previous step
        # this will get error on very starting of game 
        # and after 2 step, on every next step it will work.
        try:
            self.canvas.delete(self.head)
            self.canvas.delete(self.head_text)
            
        # in except block no code is written
        # because it is not require to perform any function on very first step
        except:
            pass
        
        # define local variable to represent coordinates of oval
        # i.e. (x1, y1), (x2, y2)
        x1 = self.dimensions[self.row_num][self.col_num][0]
        y1 = self.dimensions[self.row_num][self.col_num][1]
        x2 = self.dimensions[self.row_num][self.col_num][2]
        y2 = self.dimensions[self.row_num][self.col_num][3]
        
        # add player in canvas and configure the background as sky blue
        self.head = self.canvas.create_oval(x1+5, y1+5, x2-5, y2-5)
        self.canvas.itemconfigure(self.head, fill = 'sky blue')
        
        # add a text to the oval and configure the color as black
        self.head_text = self.canvas.create_text(x1+25, y1+25, text = "You")
        self.canvas.itemconfigure(self.head_text, fill = 'black')
        
        # now delete the next steps from previous position of player
        self.prev_possible_moves()
        
        # and display the next steps from current position of player
        self.next_possible_moves()


    '''
    this will make remove highlighted boxes, shown as next step,
    and change them into simple cells
    '''
    def prev_possible_moves(self):
        # we have shown the next possible steps which are total 4 in count in all directions
        # to set them as normal cell
        # we have to check first whether they exist or not.
        # if not done, then it will give index out of range error of list_of_boxes list
        # check if the row number of next possible step is less than or equal to the total number of rows
        if self.prev_row_num+1 <=self.no_of_rows-1:
            self.canvas.itemconfigure(self.list_of_boxes[self.prev_row_num+1][self.prev_col_num], fill = 'light yellow')
            
        # check if the row number of next possible step is greater than or equal to the total number of rows
        if self.prev_row_num-1 >= 0:
            self.canvas.itemconfigure(self.list_of_boxes[self.prev_row_num-1][self.prev_col_num], fill = 'light yellow')
            
        # check if the column number of next possible step is less than or equal to the total number of columns
        if self.prev_col_num+1 <=self.no_of_columns-1:
            self.canvas.itemconfigure(self.list_of_boxes[self.prev_row_num][self.prev_col_num+1], fill = 'light yellow')
            
        # check if the column number of next possible step is greater than or equal to the total number of columns
        if self.prev_col_num-1 >= 0:
            self.canvas.itemconfigure(self.list_of_boxes[self.prev_row_num][self.prev_col_num-1], fill = 'light yellow')

    def next_possible_moves(self):
    
        # we have to show the next possible steps in all 4 directions
        # for this we have to check first, whether they exist or not
        # if they exist then show otherwise don't show
        
        # check if the row number of next possible step is less than or equal to the total number of rows
        if self.row_num+1 <=self.no_of_rows-1:
            self.canvas.itemconfigure(self.list_of_boxes[self.row_num+1][self.col_num], fill = 'green')
        
        # check if the row number of next possible step is greater than or equal to the total number of rows
        if self.row_num-1 >= 0:
            self.canvas.itemconfigure(self.list_of_boxes[self.row_num-1][self.col_num], fill = 'green')
        
        # check if the column number of next possible step is less than or equal to the total number of columns 
        if self.col_num+1 <=self.no_of_columns-1:
            self.canvas.itemconfigure(self.list_of_boxes[self.row_num][self.col_num+1], fill = 'green')
            
        # check if the column number of next possible step is greater than or equal to the total number of columns
        if self.col_num-1 >=0:
            self.canvas.itemconfigure(self.list_of_boxes[self.row_num][self.col_num-1], fill = 'green')
            

    '''
    the player have to play the game using arrow keys
    i.e., (Left, Right, Up, Down)
    this function will bind the arrow keys on the root 
    not on any frame
    '''
    def set_movement_keys(self):
        self.root.bind('<Left>', self.player_position)
        self.root.bind('<Right>', self.player_position)
        self.root.bind('<Up>', self.player_position)
        self.root.bind('<Down>', self.player_position)

    '''
    on pressing any key if player position changes
    then the points will be collected, which is actually the weight of cell,
    and these will be added to the total_points 
    thorough this variable
    '''
    def change_total_points(self):
        
        # add points collected
        self.total_points += int(self.paths[self.row_num][self.col_num])
        
        # create the text to be updated
        Points_Collected_text = "   " + str(self.total_points)
        
        # update the total points collected on first frame
        self.frame.Points_Collected.config(text = Points_Collected_text)
    
    '''
    On pressing any arrow key, certain functions have to be done
    these functions include increament and decreament of row and column number,
    move player position, show next steps for player, increase the points, etc.
    '''
    def player_position(self, event):

        # functions to be performed on pressing "left arrow key"
        if event.keysym == "Left":
            
            # check if the player is not in first column
            if self.col_num > 0:
                # change the status of previous location
                self.prev_col_num = self.col_num
                self.prev_row_num = self.row_num
                
                # change the column number according to current location of player
                self.col_num -= 1
                
                # locate the player at its new position
                self.player_design()
                
                # call the function to add points
                self.change_total_points()

        # functions to be performed  on pressing "right arrow key"
        elif event.keysym == "Right":
            
            # check if the player is not in last column
            if self.col_num < self.no_of_columns-1:
                
                # change the status of previous location
                self.prev_col_num = self.col_num
                self.prev_row_num = self.row_num
                
                # change the column number according to current location of player
                self.col_num += 1
                
                # locate the player at its new position
                self.player_design()
                
                # call the function to add points
                self.change_total_points()

        # functions to be performed on pressing "up arrow key"
        elif event.keysym == "Up":
            
            # check if the player is not in first row
            if self.row_num > 0:
                
                # change the status of previous location
                self.prev_col_num = self.col_num
                self.prev_row_num = self.row_num
                
                # change the row number according to current location of player
                self.row_num -= 1
                
                # locate the player at its new position
                self.player_design()
                
                # call the function to add points
                self.change_total_points()

        # functions to be performed on pressing "down arrow key"
        elif event.keysym == "Down":
            
            # check if the player is not in last row
            if self.row_num < self.no_of_rows-1:
                
                # change the status of previous location
                self.prev_col_num = self.col_num
                self.prev_row_num = self.row_num
                
                # change the row number according to current location of player
                self.row_num += 1
                
                # locate the player at its new position
                self.player_design()
                
                # call the function to add points
                self.change_total_points()
        
        # if the player reaches at the goal
        # i.e. the location of goal and player become same
        # then stop the game and show the points collected by player
        if self.row_num == self.goal_position[0] and self.col_num == self.goal_position[1]:
            self.stop_game()
    
    '''
    this function will stop the game if player reaches at goal
    and display the pop and will ask want to play again or not,
    if pressed to play again then it will restart the game 
    and if pressed no, then it will ask whether to quit the window
    or to just watch the game played
    '''
    def stop_game(self):
    
        # create the string to 
        final_score_message = "Your score is: " + str(int(20/100*self.total_points)) + " Do you want to play again?"
        
        # show the pop to restart the game or not
        self.restart = messagebox.askquestion(title = 'YOU WON', message = final_score_message)
        
        # if says yes then delete the second frame
        # and create new frame and board, and start the game
        if self.restart == "yes":
            self.board_frame.destroy()
            frame = self.frame
            frame.start_new_game()
            
        # if says no then show next popup to quit or not
        elif self.restart == "no":
            self.quit_game = messagebox.askquestion(title = 'QUIT', message ="Quit the game")
            
            # if says yes then close the window
            if self.quit_game == "yes":
                self.root.destroy()
                
            # if says no then freeze the keys
            elif self.quit_game == "no":
                self.release_movement_keys()
                
    '''
    if player neither wants to play the game nor to quit the window
    the keys must not work until the game starts again
    '''
    def release_movement_keys(self):
        self.root.unbind('<Left>')
        self.root.unbind('<Right>')
        self.root.unbind('<Up>')
        self.root.unbind('<Down>')

