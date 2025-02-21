import tkinter as tk
from tkinter import messagebox

def open_modal():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    messagebox.showinfo("PDF Button Clicked", "This is a Tkinter modal triggered from the PDF!")
    root.destroy()

if __name__ == "__main__":
    open_modal()
