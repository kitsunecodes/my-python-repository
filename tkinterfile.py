# prints hi when you press the button

import tkinter as tk

def print_hi():
  print("hi")

root = tk.Tk
root.Title = "Tkinter"

btn = tk.Button(root, text="press me", command=print_hi)
btn.pack(expand=True)

root.mainloop()
