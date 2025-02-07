# This script aims at taking a more programatic approach to the editable PDF reports.
# Goal: to have a series of text input fields tied to if/else blocks in order to 'edit'
# a PDF through the CLI. This way the fields are editable and the text can be wrangled.

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from fillpdf import fillpdfs
import textwrap


# Function to wrap text within a given width
def wrap_text(text, max_width): #font_size?
    """Splits text into lines to fit within a specific width."""
    wrapped_lines = textwrap.wrap(text, width=max_width)
    return wrapped_lines

# Function to place wrapped text in the PDF
def place_wrapped_text(text, x, y, pdf_path, output_path, page_number):
    file_name = 'base.pdf'
    pdf = canvas.Canvas(file_name, pagesize=letter)
    wrapped_lines = wrap_text(text, max_width=10)  # Adjust max_width as needed
    y_position = y  # Start Y position

    for line in wrapped_lines:
        print("\n ", line)
        pdf.drawString(x, y_position, line)
        #fillpdfs.place_text(line, x, y_position, pdf_path, output_path, page_number, font_size=12, font_name="helv")
        y_position -= 20  # Move to the next line
    
    pdf.save()


# TEST main function to run tests on wrap_text
def testMain():
    print("\n Testing text wrapping ...")
    fillpdfs.get_form_fields('base.pdf')
    
    # file_name = 'base.pdf'
    # pdf = canvas.Canvas(file_name, pagesize=letter)

    newMessage = input("Enter some text to wrap: ")
    
    place_wrapped_text(
        newMessage,
        350,
        600,
        'base.pdf',
        'blank1.pdf',
        1
    )


# MAIN
def main():
    # Reused for base pdf
    file_name = 'base.pdf'

    pdf = canvas.Canvas(file_name, pagesize=letter)

    pdf.drawString(350, 695, "TEXT")

    #pdf.save()
    fillpdfs.get_form_fields('base.pdf')

    fillpdfs.place_text(
        'Hello there i am inserting \nmore than a decent amount \nof text here to see what happens', #text, 
        10, #x, 
        10, #y, 
        'base.pdf', #input_pdf_path, 
        'blank1.pdf', #output_map_path, 
        1, #page_number, 
        font_size=12, 
        font_name="helv", 
        color=None
    )


    print("Starting CLI ...")

    # test field vars
    field1 = "Why hello"
    field2 = "Text is here"

    print("\n Field 1: " , field1)
    print("Field 2: " , field2)
    text = input("\n Which Field from above do you want to edit? (enter 1 or 2) :")

    while text != "1" and text != "2":
        text = input("\nIncorrect input. Try again :")

    if text == "1":
        print("\nField selected: " , field1)
        newText = input("Enter the new text : ")
        print("Your new text for Field1:\n" , newText)
        # pdf.drawString(350, 695, newText)
        # pdf.save()
        fillpdfs.place_text(
            newText, #text, 
            10, #x, 
            10, #y, 
            'base.pdf', #input_pdf_path, 
            'blank1.pdf', #output_map_path, 
            1, #page_number, 
            font_size=12, 
            font_name="helv", 
            color=None
        )

    if text == "2":
        print("\nField selected: " , field2)
        newText = input("Enter the new text : ")
        print("Your new text for Field2:\n" , newText)
        pdf.drawString(350, 695, newText)

    print("\n Exiting ... done.")


# FUNC RUNS
testMain()