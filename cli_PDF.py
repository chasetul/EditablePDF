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
    wrapped_lines = textwrap.wrap(text, width=max_width)
    return wrapped_lines

# Function to place wrapped text in the PDF
def place_wrapped_text(pdf, text, x, y, max_width): #, pdf_path, output_path, page_number
    # file_name = 'base.pdf'
    # pdf = canvas.Canvas(file_name, pagesize=letter)
    wrapped_lines = wrap_text(text, max_width)  # Adjust max_width as needed
    y_position = y  # Start Y position

    for line in wrapped_lines:
        print("\n ", line)
        pdf.drawString(x, y_position, line)
        #fillpdfs.place_text(line, x, y_position, pdf_path, output_path, page_number, font_size=12, font_name="helv")
        y_position -= 10  # Move to the next line
    
    #pdf.save()


# TEST main function to run tests on wrap_text
def testMain():
    print("\n Testing text wrapping ...")

    file_name = 'base.pdf'
    pdf = canvas.Canvas(file_name, pagesize=letter)

    newMessage = input("Enter some text to wrap: ")
    
    place_wrapped_text(
        pdf,
        newMessage,
        300,
        600
    )

    # TESTING A SECOND MESSAGE
    newMessage2 = input("Enter some more text to wrap: ")
    
    place_wrapped_text(
        pdf,
        newMessage2,
        300,
        400
    )

    pdf.save()
    print("\n DONE.")



# Slide 14 MAIN testing
def slide14():
    print("\n-------------- SLIDE 14 --------------")

    file_name = 'base-14.pdf'
    pdf = canvas.Canvas(file_name, pagesize=letter)

    # INITIAL PDF SETUP - TEXT LABELS
    pdf.drawString(
        420, # X
        750, # Y
    "SIGACTS" )
    pdf.drawString(360, 710, "CALLS FOR EMERGENCY SERVICE")
    pdf.drawString(410, 690, "                    VICINITY")
    pdf.drawString(360, 670, "SNAPSHOT OF LAST 25 RECORDED")
    pdf.drawString(360, 500, "LAST 25 SIGACTS IN TABLE FORMAT")
    pdf.drawString(20, 600, "Map of SIGACTS")
    pdf.drawString(200, 580, "Listed crimes & amount")
    pdf.drawString(20, 420, "SUMMARY: ")
    pdf.drawString(360, 640, "DATE")
    pdf.drawString(420, 640, "LOCATION")
    pdf.drawString(520, 640, "OFFENSE")
    # IMAGES
    image_path2 = "logo copy.png"
    pdf.drawImage(image_path2, 550, 750, width=50, height=30)
    # OUTLINE BOXES
    pdf.rect( # BOX - MAIN
        10, # X
        80, # Y
        590, # width
        700, # height
        fill=0
    )
    pdf.rect( # BOX - left Lg upper
        15, # X
        475, # Y
        320, # width
        300, # height 
        fill=0
    )
    pdf.rect( # BOX - left low
        15, # X
        215, # Y
        320, # width
        255, # height 
        fill=0
    )
    # RIGHT SIDE BOXES
    pdf.rect( # BOX - outline right
        340, # X
        320, # Y
        255, # width
        420, # height 
        fill=0
    )
    pdf.rect( # BOX - outline right lower
        350, # X
        330, # Y
        235, # width
        330, # height 
        fill=0
    )

    # START input messages
    newMessage = input("Enter the location name: ") # Get LOCATION text
    place_wrapped_text( # Place the location text to pdf
        pdf,
        newMessage,
        410,
        695,
        10
    )
    newMessage2 = input("Enter the summary: ") # Get SUMMARY text
    place_wrapped_text( # Place the location text to pdf
        pdf,
        newMessage2,
        20,
        400,
        55 # max line width
    )
    newImage = input("Enter the image path (SIGACTS Map): ")
    if os.path.exists(newImage):
        pdf.drawImage(newImage, 20, 620, width=110, height=140)
    else:
        print("No file found with path [", newImage, "]")

    place_wrapped_text( # Place the DATE
        pdf,
        "02/10/2025",
        353,
        625,
        20
    )

    # EOF
    pdf.save()
    print("\n PDF changed: " , file_name)


# FUNC RUNS
#testMain()
slide14()