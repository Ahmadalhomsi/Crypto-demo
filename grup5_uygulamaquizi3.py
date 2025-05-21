# QUIZ 3

# Grup 5

# 210201140
# Ahmad Alhomsi

# 210201126
# Ebrar Mustafa AÇIKYOL

# 210201120
# Cem Korkmaz


import os
import random


def number_to_binary(number: int, bit_number: int) -> str:
    b = format(number, "b")
    return b.zfill(bit_number)


def binary_to_number(binary_str: str) -> int:
    if not all(c in "01" for c in binary_str):
        raise ValueError("binary_str must contain only '0' or '1'")
    return int(binary_str, 2)


def hex_to_number(hex_str: str) -> int:
    s = hex_str.strip()
    if s.lower().startswith("0x"):
        s = s[2:]

    if not all(c in "0123456789abcdefABCDEF" for c in s):
        raise ValueError("hex_str must be a valid hexadecimal string")
    return int(s, 16)


# -------

import tkinter as tk
import random
from tkinter import simpledialog, messagebox


def generate_spiral(n):
    grid = [[0] * n for _ in range(n)]
    dx, dy = 0, 1
    x, y = 0, 0
    for i in range(1, n * n + 1):
        grid[x][y] = i
        if not (0 <= x + dx < n and 0 <= y + dy < n and grid[x + dx][y + dy] == 0):
            dx, dy = dy, -dx  # rotate
        x += dx
        y += dy
    return grid


def get_spiral_path(grid):
    n = len(grid)
    value_to_pos = {}
    for i in range(n):
        for j in range(n):
            value_to_pos[grid[i][j]] = (i, j)
    path = [value_to_pos[i] for i in range(1, n * n + 1)]
    return path


class SpiralGame:
    def __init__(self, root, size, obstacles):
        self.root = root
        self.root.title("Spiral Game")
        self.size = size
        self.grid = generate_spiral(size)
        self.path = get_spiral_path(self.grid)  # full spiral path
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.obs_arr = []
        self.lastPath = []

        self.start_choice = self.ask_start_choice()  # 1 or 2
        self.direction = 1 if self.start_choice == 1 else -1
        self.index = 0 if self.direction == 1 else size - 1
        self.current_pos = self.path[self.index]

        self.obstacles = self.generate_obstacles(obstacles)

        self.create_grid()
        self.highlight()

        self.next_button = tk.Button(root, text="Next", command=self.next_move)
        self.next_button.grid(row=self.size, column=0, columnspan=self.size)

        getCellText = self.getCellText(self.current_pos[0], self.current_pos[1])
        self.lastPath.append(getCellText)

    def ask_start_choice(self):
        while True:
            val = simpledialog.askinteger(
                "Choose Start",
                "Enter 1 to start at left or 2 to start at right:",
                minvalue=1,
                maxvalue=2,
            )
            if val in [1, 2]:
                return val
            messagebox.showerror("Invalid Choice", "Please choose 1 or 2.")

    def generate_obstacles(self, count):
        obstacles = set()
        safe_indices = {0, len(self.path) - 1}
        while len(obstacles) < count:
            idx = random.randint(0, len(self.path) - 1)
            if idx not in safe_indices:
                obstacles.add(self.path[idx])
        return obstacles

    def create_grid(self):
        int_size = int(self.size)  # assuming self.size is defined
        for i in range(int_size):
            for j in range(int_size):
                rand_num = random.randint(0, 15)
                hex_val = hex(rand_num)[2:].upper()  # Convert to hex and uppercase

                btn = tk.Button(self.root, text=hex_val, width=4, height=2)
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j] = btn

    def highlight(self):
        for i in range(self.size):
            for j in range(self.size):
                pos = (i, j)
                if pos == self.current_pos:
                    self.buttons[i][j].configure(bg="lightgreen")
                elif pos in self.obstacles:
                    self.buttons[i][j].configure(bg="gray", text="X")
                else:
                    rand_hex = random.randint(0, 15)
                    self.buttons[i][j].configure(
                        bg="SystemButtonFace", text=hex(rand_hex)[2:].upper()
                    )

    def highlight2(self):
        for i in range(self.size):
            for j in range(self.size):
                pos = (i, j)
                if pos == self.current_pos:
                    self.buttons[i][j].configure(bg="lightgreen")

    def getCellText(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.buttons[row][col].cget("text")
        else:
            return None

    def next_move(self):
        print("Next move")
        print(self.index)
        print(self.direction)
        next_index = self.index + self.direction
        print("Self path:", self.path)
        print("Length of path:", len(self.path))
        print("Next index:", next_index)
        if 0 <= next_index < len(self.path):
            next_pos = self.path[next_index]
            if next_pos in self.obstacles:
                messagebox.showerror("Game Over", "You hit an obstacle!")
                # self.next_button.config(state='disabled')
                self.obs_arr.append(next_pos)
                print("Obstacle positions:", self.obs_arr)
                self.lastPath = []

            else:
                getCellText = self.getCellText(next_pos[0], next_pos[1])
                print("Cell text:", getCellText)
                self.lastPath.append(getCellText)
                print("Last path:", self.lastPath)

            self.index = next_index
            self.current_pos = next_pos
            self.highlight2()
            if (self.direction == 1 and self.index == len(self.path) - 1) or (
                self.direction == -1 and self.index == 0
            ):
                messagebox.showinfo("🎉 You Win!", "You've completed the spiral!")
                self.next_button.config(state="disabled")

                for i in range(len(self.lastPath)):
                    if i == 0:
                        xor_result = hex_to_number(self.lastPath[i])
                    else:
                        xor_result ^= hex_to_number(self.lastPath[i])

                print("XOR result:", xor_result)

        else:
            messagebox.showinfo("Done", "No more moves.")
            self.next_button.config(state="disabled")
        print("Last path:", self.lastPath)


if __name__ == "__main__":
    size = input("Enter the size of the spiral: ")
    engelSayisi = input("Enter the number of obstacles: ")

    root = tk.Tk()
    game = SpiralGame(root, int(size), int(engelSayisi))
    root.mainloop()


# def main():
#     print("Quiz 3 - Grup 5")
#     print("Enter your a:")
#     a = input()


# if __name__ == "__main__":
#     main()
