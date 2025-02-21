import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image, ImageTk
import PyPDF2
from tkinter.scrolledtext import ScrolledText

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("JPEG files", "*.jpeg"), ("GIF files", "*.gif")])
    if file_path and file_path.strip():  # Ensure a valid file is selected
        load_image(file_path)


def load_image(path):
    try:
        image = Image.open(path)
        image = image.resize((250, 250), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(image)
        canvas.image = img  # Keep reference
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
    except Exception as e:
        print(f"Error loading image: {e}")


def display_text():
    user_text = text_entry.get("1.0", tk.END).strip()
    label.config(text=user_text)

def load_static_image():
    static_image = Image.open("main-entry.jpg")  # Ensure this file exists in the script directory
    static_image = static_image.resize((250, 250), Image.Resampling.LANCZOS)
    static_img = ImageTk.PhotoImage(static_image)
    static_canvas.image = static_img  # Keep reference
    static_canvas.create_image(0, 0, anchor=tk.NW, image=static_img)

def load_pdf(path):
    try:
        with open(path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text_content = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
            pdf_display.delete("1.0", tk.END)
            pdf_display.insert(tk.END, text_content)
    except Exception as e:
        print(f"Error loading PDF: {e}")

def load_static_pdf():
    load_pdf("base-14.pdf")  # Ensure this file exists in the script's directory

# Create main window
root = tk.Tk()
root.title("Text and Image Uploader")
root.geometry("400x500")

# Text entry
text_entry = Text(root, height=3, width=40)
text_entry.pack(pady=10)

# Button to display text
text_button = tk.Button(root, text="Show Text", command=display_text)
text_button.pack()

# Label to display text
label = tk.Label(root, text="", wraplength=380)
label.pack(pady=10)

# Button to open image file
image_button = tk.Button(root, text="Upload Image", command=open_file)
image_button.pack()

# Canvas to display image
canvas = tk.Canvas(root, width=250, height=250)
canvas.pack(pady=10)

# Static image display
# static_canvas = tk.Canvas(root, width=250, height=250)
# static_canvas.pack(pady=10)
# load_static_image()

# Text widget to display PDF content
pdf_display = ScrolledText(root, height=20, width=60)
pdf_display.pack(pady=10)

load_static_pdf()

# Run main loop
root.mainloop()
