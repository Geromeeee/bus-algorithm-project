from tkinter import *

center=Tk()
center.title("9x9 grid")
color = ''
cells = {}
for row in range(15):
     for col in range(6):
        #color dictator
        if row == 0 and col == 0:
           color = 'indianred3'
        elif (row < 7 and col == 1) or (row == 1 and col == 0) or (row > 1 and row < 8 and col==4) or ((row < 2 or (row>6 and row<10))and col==5) or (row==14 and col ==3):
            color ='mediumpurple3'
        elif (row<14 and (col>1 and col<4)) or ((row < 2 or (row > 7 and row < 10 )) and col == 4):
            color = 'darkseagreen3'
        elif ((row>1 and row < 7) and (col == 0 or col == 5)) or ((row>9) and ((col < 2 or col>3) or (col == 2 and row ==14))):
            color = 'moccasin'
            #color='mediumpurple3'
        elif ((row > 6 and row < 10) and (col < 2)):
            color = 'steelblue2'

        cell = Frame(center, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=1, background = color,
                     width=50, height=50,  padx=3,  pady=3)
        cell.grid(row=row, column=col)
        cells[(row, col)] = cell

center.mainloop()