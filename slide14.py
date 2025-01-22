from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# Create LABELS for the fields
pdf.drawString(360, 710, "CALLS FOR EMERGENCY SERVICE")
pdf.drawString(410, 690, "$$location$$ VICINITY")
pdf.drawString(360, 670, "SNAPSHOT OF LAST 25 RECORDED")

pdf.drawString(360, 500, "LAST 25 SIGACTS IN TABLE FORMAT")


# INFO STR :
pdf.drawString(20, 600, "Map of SIGACTS")
pdf.drawString(200, 580, "Listed crimes & amount")
pdf.drawString(20, 420, "SUMMARY: ")


# RIGHT MID BOX TEXT
# pdf.drawString(342, 560, ">  $$Target$$ CONTRACTOR GUIDE:")
# pdf.drawString(342, 540, ">  $$Target$$ FACILITIES GUIDE:")
# pdf.drawString(342, 520, ">  $$Target$$ SECURITY PAGE:")
# pdf.drawString(342, 500, ">  EMERGENCY NUMBERS:")



# IMAGES :
image_path2 = "logo copy.png"  # logo right side
pdf.drawImage(image_path2, 550, 750, width=50, height=30)


# LEFT SIDE BOXES :
pdf.rect( # BOX - MAIN
    10, # X
    310, # Y
    590, # width
    470, # height
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
    315, # Y
    320, # width
    155, # height 
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


# TEXT TITLES:
pdf.drawString(
    420, # X
    750, # Y
    "SIGACTS" # STR
)


# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
fillpdfs.place_text_box( # lower summary
    'FieldName', 
    '$$ Paragraph format summary of all relevant Significant Acts (SIGACTS). This is a summary of the facts and how those facts can impact both the average person moving through or staying in the area as well as how it could negatively impact security applications', 
    20, 
    400, 
    'base.pdf', 
    'blank.pdf', 
    1, 
    width=310, 
    height=70, 
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
