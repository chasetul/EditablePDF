# This program aims at uploading an image to a pdf
# To run: python stupidSimpleUploadingImg.py
#         *Note* It looks like it froze, it's working...
# To use: Look on Desktop for pop-up modal
#         Click an option from sheet button
#         Observe option printed in terminal
# To kill: Close modal or control-c in terminal

import tkinter as tk

root = tk.Tk()

def show_action_sheet():
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Option 1", command=lambda: print("Option 1 selected"))
    menu.add_command(label="Option 2", command=lambda: print("Option 2 selected"))
    menu.add_separator()
    menu.add_command(label="Cancel", command=menu.destroy)
    menu.post(root.winfo_pointerx(), root.winfo_pointery())

button = tk.Button(root, text="Show Action Sheet", command=show_action_sheet)
button.pack()
print("Image Modal Active")

root.mainloop()