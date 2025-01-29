from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# RIGHT SIDE TEXT
pdf.drawString(350, 695, "SUMMARY WITH THREAT RATINGS")


# LEFT SIDE TEXT
pdf.drawString(60, 660, "MAP OF PROPERTY")
pdf.drawString(60, 640, "1. Always orient north")
pdf.drawString(60, 620, "2. If the map doesn't fit, insert aditional photos")
pdf.drawString(60, 600, "3. Clearly label ALL entries & exits")
pdf.drawString(60, 580, "4. Clearly highlight the wall")
pdf.drawString(60, 560, "5. Include a North seeking arrow")
pdf.drawString(60, 540, "6. Use a legend (if needed) to clarify odd graphics")
pdf.drawString(60, 520, "7. DO NOT INCLUDE GOOGLE BRANDING")
pdf.drawString(60, 500, "8. DO NOT INCLUDE THE RED LOCATOR")
pdf.drawString(60, 480, "   ICON ON GOOGLE MAPS")


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
pdf.rect( # BOX - left Lg top
    15, # X
    290, # Y
    320, # width
    440, # height 
    fill=0
)


# RIGHT SIDE BOXES
pdf.rect( # BOX - outline right lg
    340, # X
    290, # Y
    255, # width
    440, # height 
    fill=0
)




# TEXT TITLES:
pdf.drawString(
    390, # X
    750, # Y
    "EXECUTIVE SUMMARY" # STR
)
pdf.drawString(
    120, # X
    764, # Y
    "LOCATION" # STR
)
pdf.drawString(
    40, # X
    747, # Y
    "THREAT VULNERABILITY & RISK ASSESSMENT" # STR
)



# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
fillpdfs.place_text_box( # location top
    'FieldName', 
    'SUMMARY WITH THREAT RATINGS', 
    345, 
    80, 
    'base.pdf', 
    'blank.pdf', 
    1, 
    width=245, 
    height=240, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
 )
fillpdfs.place_text_box( # summary w threats
    'FieldName1', 
    'LOCATION', 
    115, 
    13, 
    'blank.pdf', 
    'blank1.pdf', 
    1, 
    width=70, 
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
final_pdf = 'blank1.pdf'
print("\n PDF Generated : " + final_pdf)
