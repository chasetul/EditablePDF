from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# Top title
pdf.drawString(350, 710, "KEY $$ LOCAL POLICE $$ FINDINGS AS")
pdf.drawString(410, 690, "OF $$ DATE OF REPORT $$")
# bullet pnts *
pdf.drawString(350, 660, "* Reported homicide offenses:")
pdf.drawString(350, 620, "* Reported aggravated assault offenses:")
pdf.drawString(350, 580, "* Reported fraud offenses:")
pdf.drawString(350, 540, "* Reported motor vehicle theft offenses:")
pdf.drawString(350, 500, "* Reported robbery offenses:")
pdf.drawString(350, 460, "* Reported B&E and burglary offenses:")
pdf.drawString(350, 420, "* Reported stolen property offenses:")
pdf.drawString(350, 380, "* Reported narcotics offenses:")
pdf.drawString(350, 340, "* Reported weapons law violation offenses:")
# low right info
pdf.drawString(360, 300, "KEY OBSERVATIONS FOR THE ")
pdf.drawString(390, 280, "$$ LOCAL POLICE $$ :")
pdf.drawString(360, 260, "Person Crimes :")
pdf.drawString(360, 220, "Societal Crimes :")
pdf.drawString(360, 180, "Predictive Analysis :")
# INFO STR left
pdf.drawString(70, 600, "Local police crime statistics chart")




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
    90, # Y
    320, # width
    685, # height 
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
pdf.rect( # BOX - outline right
    340, # X
    90, # Y
    255, # width
    650, # height 
    fill=0
)



# TEXT TITLES:
pdf.drawString(
    420, # X
    750, # Y
    "ANNUAL SIGACTS" # STR
)


# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
fillpdfs.place_text_box( # local police UP-MOST
    'FieldName', 
    '$$ LOCAL POLICE $$', 
    375, 
    67, 
    'base.pdf', 
    'blank.pdf', 
    1, 
    width=127, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # date of report
    'FieldName1', 
    '$$ DATE OF REPORT $$', 
    432, 
    90, 
    'blank.pdf', 
    'blank1.pdf', 
    1, 
    width=145, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # bullet 1
    'FieldName2', 
    '$$ Increase OR decrease, percentage change Y/Y $$', 
    360, 
    140, 
    'blank1.pdf', 
    'blank2.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # bullet 2
    'FieldName3', 
    '$$ Increase OR decrease, percentage change Y/Y $$', 
    360, 
    180, 
    'blank2.pdf', 
    'blank3.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # bullet 3
    'FieldName4', 
    '$$ Increase OR decrease, percentage change Y/Y $$', 
    360, 
    220, 
    'blank3.pdf', 
    'blank4.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # bullet 4
    'FieldName5', 
    '$$ Increase OR decrease, percentage change Y/Y $$', 
    360, 
    260, 
    'blank4.pdf', 
    'blank5.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # bullet 5
    'FieldName6', 
    '$$ Increase OR decrease, percentage change Y/Y $$', 
    360, 
    300, 
    'blank5.pdf', 
    'blank6.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # bullet 6
    'FieldName7', 
    '$$ Increase OR decrease, percentage change Y/Y $$', 
    360, 
    340, 
    'blank6.pdf', 
    'blank7.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # bullet 7
    'FieldName8', 
    '$$ Increase OR decrease, percentage change Y/Y $$', 
    360, 
    380, 
    'blank7.pdf', 
    'blank8.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # bullet 8
    'FieldName9', 
    '$$ Increase OR decrease, percentage change Y/Y $$', 
    360,
    420, 
    'blank8.pdf', 
    'blank9.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # bullet 9
    'FieldName10', 
    '$$ Increase OR decrease, percentage change Y/Y $$', 
    360, 
    460, 
    'blank9.pdf', 
    'blank10.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
# low local police
fillpdfs.place_text_box( # 
    'FieldName11', 
    '$$ LOCAL POLICE $$', 
    360, 
    500, 
    'blank10.pdf', 
    'blank11.pdf', 
    1, 
    width=150, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
#person
fillpdfs.place_text_box( # 
    'FieldName12', 
    '$$ LOCAL POLICE $$', 
    360, 
    540, 
    'blank11.pdf', 
    'blank12.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
#societal
fillpdfs.place_text_box( # 
    'FieldName13', 
    '$$ LOCAL POLICE $$', 
    360, 
    580, 
    'blank12.pdf', 
    'blank13.pdf', 
    1, 
    width=230, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
# predictive
fillpdfs.place_text_box( # 
    'FieldName14', 
    '$$ LOCAL POLICE $$', 
    360, 
    620, 
    'blank13.pdf', 
    'Slide15.pdf', 
    1, 
    width=230, 
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
