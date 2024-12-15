import tkinter as tk
import random
from pygraph.classes.graph import graph

# Парамеры ивры АХАХА
CELL_SIZE = 20
ROWS = 20
COLS = 30
DELAY = 300

def create_grid_graph(rows, cols):
    g = graph()
    for r in range(rows):
        for c in range(cols):
            g.add_node((r, c))
    return g

def count_alive_neighbors(graph, grid, r, c):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if graph.has_node((nr, nc)) and grid[nr][nc]:
            count += 1
    return count

def next_generation(graph, grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[False for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            alive_neighbors = count_alive_neighbors(graph, grid, r, c)
            if grid[r][c]:
                new_grid[r][c] = 2 <= alive_neighbors <= 3
            else:
                new_grid[r][c] = alive_neighbors == 3
    return new_grid

class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.graph = create_grid_graph(rows, cols)
        self.grid = [[False for _ in range(cols)] for _ in range(rows)]

        self.root = tk.Tk()
        self.root.title("Игра Жизнь (Conway's Game of Life)")
        
        self.canvas = tk.Canvas(self.root, width=cols * CELL_SIZE, height=rows * CELL_SIZE, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.toggle_cell)
        
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack(side=tk.LEFT)
        
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.pack(side=tk.LEFT)

        self.running = False
        self.update_canvas()

    def toggle_cell(self, event):
        c, r = event.x // CELL_SIZE, event.y // CELL_SIZE
        if self.graph.has_node((r, c)):
            self.grid[r][c] = not self.grid[r][c]
            self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                x1, y1 = c * CELL_SIZE, r * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                color = "black" if self.grid[r][c] else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def run_generation(self):
        if self.running:
            self.grid = next_generation(self.graph, self.grid)
            self.update_canvas()
            self.root.after(DELAY, self.run_generation)

    def start_game(self):
        if not self.running:
            self.running = True
            self.run_generation()

    def reset_game(self):
        self.running = False
        self.grid = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.update_canvas()

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = GameOfLife(ROWS, COLS)
    game.start()
