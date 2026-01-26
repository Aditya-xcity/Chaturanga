# Question: Create a Tkinter application that renders typed text as true circular Braille cells without square block artifacts
# Name - ADITYA BHARDWAJ
# Section - D2
# Roll No - 08
# Course – B TECH
# Branch – CSE

import tkinter as tk

brailleData = {
    "a": ["10","00","00"], "b": ["10","10","00"], "c": ["11","00","00"],
    "d": ["11","01","00"], "e": ["10","01","00"], "f": ["11","10","00"],
    "g": ["11","11","00"], "h": ["10","11","00"], "i": ["01","10","00"],
    "j": ["01","11","00"], "k": ["10","00","10"], "l": ["10","10","10"],
    "m": ["11","00","10"], "n": ["11","01","10"], "o": ["10","01","10"],
    "p": ["11","10","10"], "q": ["11","11","10"], "r": ["10","11","10"],
    "s": ["01","10","10"], "t": ["01","11","10"], "u": ["10","00","11"],
    "v": ["10","10","11"], "w": ["01","11","01"], "x": ["11","00","11"],
    "y": ["11","01","11"], "z": ["10","01","11"]
}

DOT = 14
GAP = 6
MAX_COLS = 8

def createDot(parent, filled):
    c = tk.Canvas(parent, width=DOT, height=DOT, highlightthickness=0)
    color = "purple" if filled else "#ddd"
    c.create_oval(1, 1, DOT-1, DOT-1, fill=color, outline=color)
    return c

def renderBraille():
    for w in outputFrame.winfo_children():
        w.destroy()

    text = inputEntry.get().lower()
    index = 0

    for ch in text:
        if ch not in brailleData:
            continue

        row = index // MAX_COLS
        col = index % MAX_COLS

        cell = tk.Frame(outputFrame)
        cell.grid(row=row, column=col, padx=12, pady=10)

        pattern = brailleData[ch]

        for r in range(3):
            for c in range(2):
                dot = createDot(cell, pattern[r][c] == "1")
                dot.grid(row=r, column=c, padx=GAP, pady=GAP)

        index += 1

root = tk.Tk()
root.title("True Braille Renderer (Circles Only)")

tk.Label(root, text="Enter Text").pack(pady=6)

inputEntry = tk.Entry(root, width=40)
inputEntry.pack(pady=6)

tk.Button(root, text="Render", command=renderBraille).pack(pady=6)

outputFrame = tk.Frame(root)
outputFrame.pack(pady=10)

root.mainloop()
