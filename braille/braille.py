# Question: Create a Tkinter application to visually represent all alphabets (a–z) using a 3x2 Chaturanga grid chart
# Name - ADITYA BHARDWAJ
# Section - D2
# Roll No - 08
# Course – B TECH
# Branch – CSE

import tkinter as tk

data = {
    "a": ["10", "00", "00"],
    "b": ["10", "10", "00"],
    "c": ["11", "01", "00"],
    "d": ["11", "01", "00"],
    "e": ["11", "00", "00"],
    "f": ["10", "01", "00"],
    "f": ["11", "10", "00"],
    "g": ["11", "11", "00"],
    "h": ["10", "11", "00"],
    "i": ["01", "10", "00"],
    "j": ["01", "11", "00"],
    "k": ["10", "00", "10"],
    "l": ["10", "10", "10"],
    "m": ["11", "00", "10"],
    "n": ["11", "01", "10"],
    "o": ["10", "01", "10"],
    "p": ["11", "10", "10"],
    "q": ["11", "11", "10"],
    "r": ["10", "11", "10"],
    "s": ["01", "10", "10"],
    "t": ["01", "11", "10"],
    "u": ["10", "00", "11"],
    "v": ["10", "10", "11"],
    "w": ["01", "11", "01"],
    "x": ["11", "00", "11"],
    "y": ["11", "01", "11"],
    "z": ["10", "01", "11"]
}

root = tk.Tk()
root.title("Chaturanga Alphabet Chart")

canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas)

frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

row = 0
col = 0
maxCols = 6

for letter, pattern in data.items():
    container = tk.Frame(frame, relief="ridge", borderwidth=2, padx=8, pady=5)
    container.grid(row=row, column=col, padx=8, pady=8)

    tk.Label(container, text=letter.upper(), font=("Arial", 14, "bold")).pack()

    gridFrame = tk.Frame(container)
    gridFrame.pack()

    for r in range(3):
        for c in range(2):
            value = pattern[r][c]
            color = "purple" if value == "1" else "lightgray"
            lbl = tk.Label(
                gridFrame,
                width=3,
                height=1,
                bg=color,
                relief="solid"
            )
            lbl.grid(row=r, column=c, padx=2, pady=2)

    col += 1
    if col >= maxCols:
        col = 0
        row += 1

root.mainloop()
