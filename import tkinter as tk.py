import tkinter as tk

def on_select(event):
    selected_item = listbox.get(listbox.curselection())
    print(f"Selected Item: {selected_item}")

# Create the main window
root = tk.Tk()
root.title("List Selection Example")

# Create a listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Populate the listbox with items
items = ["Item 1", "Item 2", "Item 3", "Item 4"]
for item in items:
    listbox.insert(tk.END, item)

# Bind the listbox selection to the on_select function
listbox.bind('<<ListboxSelect>>', on_select)

# Run the Tkinter event loop
root.mainloop()
