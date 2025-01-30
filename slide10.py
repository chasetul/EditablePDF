from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# Create LABELS for the fields
pdf.drawString(15, 760, "Venue Reservations:")
pdf.drawString(15, 740, "Venue Concierge:")
pdf.drawString(15, 720, "Venue Emergency:")
pdf.drawString(15, 700, "Venue Alt. Emergency:")
pdf.drawString(15, 680, "Venue On Site Emergency:")
pdf.drawString(15, 660, "Emergency:")
pdf.drawString(15, 640, "Local PD Non-Emergency:")
pdf.drawString(15, 620, "Maj. PD Non-Emergency:")
pdf.drawString(15, 600, "Local Hospital:")
pdf.drawString(15, 580, "Local Fire Station:")
pdf.drawString(15, 560, "Local Fire & Rescue:")
pdf.drawString(15, 540, "Human Trafficking Line:")


# IMAGES :
image_path2 = "logo copy.png"  # logo right side
pdf.drawImage(image_path2, 550, 750, width=50, height=30)


# BOXES :
pdf.rect( # BOX - MAIN
    10, # X
    200, # Y
    590, # width
    580, # height
    fill=0
)
pdf.rect( # BOX - Items outline upper left
    10, # X
    530, # Y
    280, # width
    250, # height 260
    fill=0
)


# RECTS - TEXT BOX - EMERGENCY SERVICES MAP
pdf.rect(
    200, # X
    210, # Y
    180, # Width
    20, # Height
    fill=0
) # 


# TEXT TITLES:
pdf.drawString(
    205, # X
    215, # Y
    "EMERGENCY SERVICES MAP" # STR
)


# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
fillpdfs.place_text_box( # 
    'FieldName', # fieldname - not sure how to use
    '(XXX)-XXX-XXXX', # placeholder in editable field
    188, # X
    17, # Y : Smaller num = higher on page
    'base.pdf', # input pdf
    'blank.pdf', # output pdf
    1, # page num
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 1
    'FieldName1', 
    '(XXX)-XXX-XXXX', 
    188, 
    37, 
    'blank.pdf', 
    'blank1.pdf', 
    1, 
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 2
    'FieldName2', 
    '(XXX)-XXX-XXXX', 
    188, 
    57, 
    'blank1.pdf', 
    'blank2.pdf', 
    1, 
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 3
    'FieldName3', 
    '(XXX)-XXX-XXXX', 
    188, 
    77, 
    'blank2.pdf', 
    'blank3.pdf', 
    1, 
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 4
    'FieldName4', 
    '(XXX)-XXX-XXXX', 
    188, 
    97, 
    'blank3.pdf', 
    'blank4.pdf', 
    1, 
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 5
    'FieldName5', 
    '(XXX)-XXX-XXXX', 
    188, 
    117, 
    'blank4.pdf', 
    'blank5.pdf', 
    1, 
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 6
    'FieldName6', 
    '(XXX)-XXX-XXXX', 
    188, 
    137, 
    'blank5.pdf', 
    'blank6.pdf', 
    1, 
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 7
    'FieldName7', 
    '(XXX)-XXX-XXXX', 
    188, 
    157, 
    'blank6.pdf', 
    'blank7.pdf', 
    1, 
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 8
    'FieldName8', 
    '(XXX)-XXX-XXXX', 
    188, 
    177, 
    'blank7.pdf', 
    'blank8.pdf', 
    1, 
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 9
    'FieldName9', 
    '(XXX)-XXX-XXXX', 
    188, 
    197, 
    'blank8.pdf', 
    'blank9.pdf', 
    1, 
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 10
    'FieldName10', 
    '(XXX)-XXX-XXXX', 
    188, 
    217, 
    'blank9.pdf', 
    'blank10.pdf', 
    1, 
    width=100, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 11
    'FieldName11', 
    '(XXX)-XXX-XXXX', 
    188, 
    237, 
    'blank10.pdf', 
    'Slide10.pdf', 
    1, 
    width=100, 
    height=15, 
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
final_pdf = 'blank11.pdf'
print("\n PDF Generated : " + final_pdf)
