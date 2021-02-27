'''
From here the project will start.

we have to import all the methods to create the board of game
and frames on window are loaded.

'''
from board import *
from frame import *

# configue the window's title, background and icon
root = Tk()
root.title("CONCUR PATHS")
root.configure(background = 'green')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='logo.png'))

# resctrict the window to change its size.
root.resizable(False, False)

# create an object of Frame class.
# initialize the object of Frame class to call its functions
my_frame = Frame(root)

# create the first frame in window
my_frame.create_first_frame()

# create the second frame in window
my_frame.design_first_frame()

# call function to create second frame which include game board.
my_frame.create_board_frame()
root.mainloop()
