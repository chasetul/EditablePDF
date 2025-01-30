from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# RIGHT SIDE TEXT
# LEFT TOP
# text
pdf.drawString(350, 655, "Each specific parking")
pdf.drawString(350, 635, "location photo with")
pdf.drawString(350, 615, "entrances and exits")
# mini circle
pdf.circle (
    355, # X
    680, # Y
    10,  # R
    fill=0
)
# right top
pdf.drawString(475, 655, "Each specific parking")
pdf.drawString(475, 635, "location photo with")
pdf.drawString(475, 615, "entrances and exits")
pdf.circle (
    480, # X
    680, # Y
    10,  # R
    fill=0
)
# mid left
pdf.drawString(350, 535, "Each specific parking")
pdf.drawString(350, 515, "location photo with")
pdf.drawString(350, 495, "entrances and exits")
pdf.circle (
    355, # X
    560, # Y
    10,  # R
    fill=0
)
# mid right
pdf.drawString(475, 535, "Each specific parking")
pdf.drawString(475, 515, "location photo with")
pdf.drawString(475, 495, "entrances and exits")
pdf.circle (
    480, # X
    560, # Y
    10,  # R
    fill=0
)
# low left
pdf.drawString(350, 415, "Each specific parking")
pdf.drawString(350, 395, "location photo with")
pdf.drawString(350, 375, "entrances and exits")
pdf.circle (
    355, # X
    440, # Y
    10,  # R
    fill=0
)
# low right
pdf.drawString(475, 415, "Each specific parking")
pdf.drawString(475, 395, "location photo with")
pdf.drawString(475, 375, "entrances and exits")
pdf.circle (
    480, # X
    440, # Y
    10,  # R
    fill=0
)


# LEFT SIDE TEXT
pdf.drawString(70, 600, "Photo of overhead with each parking")
pdf.drawString(70, 580, "location identified with bubble numbers")




# IMAGES :
image_path2 = "logo copy.png"  # logo right side
pdf.drawImage(image_path2, 550, 750, width=50, height=30)


# MAIN BOX OUTLINE
pdf.rect( # BOX - MAIN
    10, # X
    180, # Y
    590, # width
    600, # height
    fill=0
)

# LEFT SIDE BOXES :
pdf.rect( # BOX - left Lg 
    15, # X
    290, # Y
    320, # width
    485, # height 
    fill=0
)
pdf.rect( # BOX - left Lg inner
    35, # X
    335, # Y
    280, # width
    420, # height 
    fill=0
)

# RIGHT SIDE BOXES
pdf.rect( # BOX - outline right lg
    340, # X
    290, # Y
    255, # width
    430, # height 
    fill=0
)
# MINI BOXES right
pdf.rect( # mini - top left
    345, # X
    580, # Y
    120, # width
    110, # height 
    fill=0
)
pdf.rect( # mini - top right
    470, # X
    580, # Y
    120, # width
    110, # height 
    fill=0
)
# MID
pdf.rect( # mini - mid left
    345, # X
    460, # Y
    120, # width
    110, # height 
    fill=0
)
pdf.rect( # mini - mid right
    470, # X
    460, # Y
    120, # width
    110, # height 
    fill=0
)
# LOW
pdf.rect( # mini - low left
    345, # X
    340, # Y
    120, # width
    110, # height 
    fill=0
)
pdf.rect( # mini - low right
    470, # X
    340, # Y
    120, # width
    110, # height 
    fill=0
)


# Circle : compass img
pdf.circle (
    290, # X
    730, # Y
    20,  # R
    fill=0
)




# TEXT TITLES:
pdf.drawString(
    390, # X
    750, # Y
    "AVENUES OF APPROACH" # STR
)
pdf.drawString(
    410, # X
    730, # Y
    "$$ PARKING $$" # STR
)


# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
fillpdfs.place_text_box( # local police UP-MOST
    'FieldName', 
    '$$ PARKING $$', 
    410, 
    53, 
    'base.pdf', 
    'Slide6.pdf', 
    1, 
    width=100, 
    height=20, 
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
