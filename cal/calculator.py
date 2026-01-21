import tkinter as tk

# ---------------- Calculator Logic ----------------
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, font=("Arial", 16),
                        command=calculate)
    else:
        btn = tk.Button(frame, text=text, font=("Arial", 16),
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

clear_btn = tk.Button(root, text="Clear", font=("Arial", 16),
                      bg="red", fg="white", command=clear)
clear_btn.pack(fill=tk.BOTH, padx=10, pady=10)

for i in range(5):
    frame.rowconfigure(i, weight=1)
    frame.columnconfigure(i % 4, weight=1)

root.mainloop()
