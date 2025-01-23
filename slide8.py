from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# Mid title
pdf.drawString(70, 600, "Detailed description of any 3rd party ")
pdf.drawString(70, 580, "and contracted security teams and / or")
pdf.drawString(70, 560, "requirements. Can include property security")
pdf.drawString(70, 540, "policies or other findings of note.")




# IMAGES :
image_path2 = "logo copy.png"  # logo right side
pdf.drawImage(image_path2, 550, 750, width=50, height=30)


# MAIN BOX OUTLINE
pdf.rect( # BOX - MAIN
    10, # X
    80, # Y
    590, # width
    700, # height
    fill=0
)

# LEFT SIDE BOXES :
pdf.rect( # BOX - left Lg 
    15, # X
    310, # Y
    320, # width
    430, # height 
    fill=0
)

# RIGHT SIDE BOXES
pdf.rect( # BOX - outline right
    340, # X
    310, # Y
    255, # width
    430, # height 
    fill=0
)



# TEXT TITLES:
pdf.drawString(
    120, # X
    750, # Y
    "THIRD PARTY & CONTRACTED SECURITY REQUIREMENTS" # STR
)


# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
fillpdfs.place_text_box( # local police UP-MOST
    'FieldName', 
    'Description', 
    65, 
    267, 
    'base.pdf', 
    'blank.pdf', 
    1, 
    width=230, 
    height=100, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)


# Remove extra PDF's
def removePrePdfs():
    os.remove('blank.pdf')
    os.remove('blank2.pdf')
    os.remove('blank3.pdf')
    os.remove('blank4.pdf')
    os.remove('blank5.pdf')
    os.remove('blank6.pdf')

#removePrePdfs()
final_pdf = 'blank.pdf'
print("\n PDF Generated : " + final_pdf)
