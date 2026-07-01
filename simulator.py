import tkinter as tk

# Set up main window
root = tk.Tk()
root.title("Simulator")

# Create a canvas to draw our 15x6 grid
# 6 columns * 40px wide, 15 rows * 40px high
canvas = tk.Canvas(root, width=240, height=600, bg="white")
canvas.pack(padx=10, pady=10)

# Quick sample drawing a row
cell_size = 40
for row in range(15):
    for col in range(6):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        # Draw grid lines
        canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

# Start the application loop
root.mainloop()