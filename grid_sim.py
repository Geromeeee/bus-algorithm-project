#grid_sim.py
# Bus Passenger GUI Simulation

from tkinter import *
import passenger as p

#Global variables
center = None
cells = {}
cell_types = {}
color=''

def build_window():
    #Intializes the Tkinter window and creates the 15x6 grid
    global center, cells, cell_types

    if center is not None:
        return center

    center = Tk()
    center.title("Bus Layout 15x6")
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

    return center


def start_app():
    build_window()
    center.after(100, p.simulate_algo)
    center.mainloop()


def is_valid_move(current_coords, next_coords, dest_coords):
    # Checks if passenger can move into adjacent cell
    nxt_row, nxt_col = next_coords
    dest_row, dest_col = dest_coords

    if next_coords == dest_coords: #if next step is the same as the destination
        return True

    if nxt_row == dest_row or nxt_row == 14:     #if next step is now on destination row or in back row, allow horizontal movement to seats or back row respectively
        return cell_types.get(next_coords) in ['yellow', 'purple', 'blue', 'green']

    return cell_types.get(next_coords) == 'green'

def move_to_next_cell(ids, curr, dest, final):
    # Visual movement of passenger from one cell to another
    cells[curr].delete(ids[0])
    cells[curr].delete(ids[1])
    if ids[2][0] == 'p':
        color = 'red'
    else:
        color = 'white'
    d = cells[dest].create_oval(5, 5, 45, 45, fill=color)
    e = cells[dest].create_text(25, 25, text=str(ids[2][1]), fill='black', 
                            font=('Arial', 10, 'bold'))
    ids = (d, e, ids[2])
    center.after(1000, circle_move_to_cell, ids, dest, final)

def circle_move_to_cell(d, curr, dest):
    # Calculates pathfinding for passenger movement visualization
    curr_row, curr_col = curr
    dest_row, dest_col = dest
    next_step = None

    if curr == dest: #if arrived, then sit
        return

    if curr_row == dest_row:    #if now on the correct row, move horizontally
        step_dir = 1 if dest_col > curr_col else -1
        next_step = (curr_row, curr_col + step_dir)
    else:
        step_dir = 1 if dest_row > curr_row else -1         #or else vertically
        test_step = (curr_row + step_dir, curr_col)

        if is_valid_move(curr, test_step, dest):
            next_step = test_step
        else:
            for col_offset in [-1, 1]:
                alt_step = (curr_row, curr_col + col_offset)
                if is_valid_move(curr, alt_step, dest):
                    next_step = alt_step
                    break

    if next_step and next_step in cells:
        move_to_next_cell(d, curr, next_step, dest)

def create_passenger(curr, dest, length):
    # intialize new passenger
    #print(curr, dest)
    if length[0] == 'p': color = 'red' 
    else: color = 'white'
    d = cells[curr].create_oval(5, 5, 45, 45, fill=color)
    e = cells[curr].create_text(25, 25, text=str(length[1]), fill='black', 
                            font=('Arial', 10, 'bold'))
    ids = (d, e, length)
    center.after(1000, circle_move_to_cell, ids, curr, dest)


if __name__ == "__main__":
    start_app()

