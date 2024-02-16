# This is a follow-along of Gaurav Sen's tutorial on design practices 
# The main agenda is 
# A. Introduction to LLD
# B. In-dept learning about SOLID philosophy
# C. Introduction to some mainstream design patterns

# Design practices are design philosophies like OOPS, SOLID, DRY, KISS, Occams Razor
# Design patterns are templates like singleton, factory, chain-of-responsibility

## IMP
# WHAT I did while writing this code, and WHY!

# 1, I seperated different classes into different files
# This makes the codebase and logical a bit decoupled, easier to understand, and easier to interact with, without breaking things

# 2, then we make an interesting change by replacing board.cell[r][c] with board.get_cell(r, c)
# what we did here is equivalent to creating an interface (define a way to talk with our code)
# an interface is basically defining rules about how we want people to interact/work with our code
# API - application programming interface is a similar thing - defining how we want people to interact with the code

# 3, where do we create the get_cell()?
# In the parent board class, or its child, tic_tac_toe_board?
# Well, we may later add boards that do not have cells, and the function get_cells might not be logical
# hence it is more wise to add the method to the child class
# This is how we can ensure "EXTENSIBLITY". (How well can our code be extended)

#4, As a good practice, we are not accessing any attribute of a class irectly
# E.g. we don't use cell.row, instead expose the value using a getter, like cell.get_row()

#5, while writing the code, I am explicitly specifying data type of parameters
# This will greatly help in DEBUGGING the code and undersatnding what exactly is a function accepting
