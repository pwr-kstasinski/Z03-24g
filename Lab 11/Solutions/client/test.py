from scrollable import Scrollable
import tkinter as tk
from tkinter import ttk
root = tk.Tk()

header = ttk.Frame(root)
body = ttk.Frame(root)
footer = ttk.Frame(root)
header.pack()
body.pack()
footer.pack()

ttk.Label(header, text="The header").pack()
ttk.Label(footer, text="The Footer").pack()


scrollable_body = Scrollable(body, width=32)

for i in range(30):
    ttk.Button(scrollable_body, text="I'm a button in the scrollable frame").grid()

scrollable_body.update()

root.mainloop()