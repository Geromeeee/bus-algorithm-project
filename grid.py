from tkinter import *
#import passenger as p

center=Tk()
center.title("15x6 grid")
color = ''
width = 50
height = 50
cells = {}
cell_types = {}
for row in range(15):
     for col in range(6):
        #color dictator
        if row == 0 and col == 0:
           color, space_type = 'indianred3', 'red'
        elif (row < 7 and col == 1) or (row == 1 and col == 0) or (row > 1 and row < 8 and col==4) or ((row < 2 or (row>6 and row<10))and col==5) or (row==14 and col ==3):
            color, space_type ='mediumpurple3', 'purple'
        elif (row<14 and (col>1 and col<4)) or ((row < 2 or (row > 7 and row < 10 )) and col == 4):
            color, space_type = 'darkseagreen3', 'green'
        elif ((row>1 and row < 7) and (col == 0 or col == 5)) or ((row>9) and ((col < 2 or col>3) or (col == 2 and row ==14))):
            color, space_type = 'moccasin', 'yellow'
            #color='mediumpurple3'
        elif ((row > 6 and row < 10) and (col < 2)):
            color, space_type = 'steelblue2', 'blue'

        cell = Canvas(center, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=1, background = color,
                     width=width, height=height)
        cell.grid(row=row, column=col)
        cells[(row, col)] = cell
        cell_types[(row, col)] = space_type

def is_valid_move(current_coords, next_coords):
    nxt_row, nxt_col = next_coords
    if nxt_row == 14:
        return cell_types.get(next_coords)
    return cell_types.get(next_coords) == 'green'

def move_to_next_cell( curr, dest):
    cells[curr].delete("all")
    cells[dest].create_oval(5, 5, 45, 45, fill='white')
    center.after(1000, circle_move_to_cell, dest)

def circle_move_to_cell( curr = (8,4), dest = (14, 0)):
    curr_row, curr_col = curr
    dest_row, dest_col = dest
    next_step = None
    if curr_row == 0 or curr_row == dest_row:
        step_dir = 1 if dest_col > curr_col else -1
        next_step = (curr_row, curr_col + step_dir)
    else:

        step_dir = 1 if dest_row > curr_row else -1
        test_step = (curr_row + step_dir, curr_col)
        
     
        if is_valid_move(curr, test_step):
            next_step = test_step
        else:
            
            for col_offset in [-1, 1]:
                alt_step = (curr_row, curr_col + col_offset)
                if is_valid_move(curr, alt_step):
                    next_step = alt_step
                    break


    if next_step and next_step in cells:
        move_to_next_cell( curr, next_step)

    
cells[(8,4)].create_oval(5, 5, 45, 45, fill='white')
center.after(100, circle_move_to_cell)
center.mainloop()

