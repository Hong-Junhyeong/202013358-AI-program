#1
import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

root = tk.Tk()
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()


#2
import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Greet", command=greet)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()


#3
import tkinter as tk

def add():
    result = int(entry1.get()) + int(entry2.get())
    label.config(text=f"Result: {result}")

root = tk.Tk()
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
button = tk.Button(root, text="Add", command=add)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()



#4
import tkinter as tk

def show_selection():
    selections = []
    if var1.get(): selections.append("Option 1")
    if var2.get(): selections.append("Option 2")
    label.config(text=", ".join(selections))

root = tk.Tk()
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
tk.Checkbutton(root, text="Option 1", variable=var1).pack()
tk.Checkbutton(root, text="Option 2", variable=var2).pack()
tk.Button(root, text="Show", command=show_selection).pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()

