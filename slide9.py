from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# This way works well - have to rm (n - 1) blank_n.pdf's
# n = num textboxes + images?

file_name = 'base.pdf' # Starting pdf

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - GENERATE BASE PDF FOR FIELD BINDING

# Create labels for the fields
pdf.drawString(315, 720, "EMERGENCY")
pdf.drawString(319, 700, "SERVICE")

pdf.drawString(400, 720, "PHONE")
pdf.drawString(400, 700, "NUMBER")

pdf.drawString(470, 720, "ADDRESS")

pdf.drawString(560, 730, "EST")
pdf.drawString(538, 715, "RESPONSE")
pdf.drawString(558, 700, "TIME")

# Not used, connects to pdf.linkURL() -> url must be 'https...'
def myfunc():
    print("\n START")
    return 'file:///Users/chase/Desktop/AlphaRecon/juptyterbooks/EditablePDF/index.html'

# Button that links to flask server
# pdf.linkURL('file:///Users/chase/Desktop/AlphaRecon/juptyterbooks/EditablePDF/index.html', (100, 500, 300, 520), relative=0, thickness=1)
# pdf.rect(100, 500, 200, 20, fill=0)  # Draw the rectangle for the button
# pdf.drawString(110, 505, "Upload Image")


# IMAGES :
# image_path = "survEq.jpg"  # upper parking lot
# pdf.drawImage(image_path, 10, 600, width=300, height=155)

# image_path3 = "security-camera.webp"  # lower parking lot
# pdf.drawImage(image_path3, 10, 440, width=300, height=155)

image_path2 = "logo copy.png"  # logo right side
pdf.drawImage(image_path2, 560, 755, width=50, height=30)

image_path4 = "main-entry.jpg"  # main entry
pdf.drawImage(image_path4, 25, 335, width=110, height=60)

image_path5 = "rear-entry.jpg"  # main entry
pdf.drawImage(image_path5, 180, 335, width=110, height=60)


# BOXES :
pdf.rect( # BOX - main photo upload
    10, # X
    400, # Y
    300, # width
    355, # height
    fill=0
)

pdf.rect( # BOX - below main
    10, # X
    300, # Y
    300, # width
    100, # height
    fill=0
)

pdf.rect( # BOX - below main - BL
    12, # X
    302, # Y
    146, # width
    96, # height
    fill=0
)

pdf.rect( # BOX - below main - BR
    162, # X
    302, # Y
    146, # width
    96, # height
    fill=0
)

pdf.rect( # BOX - main items outline
    310, # X
    300, # Y
    300, # width
    455, # height
    fill=0
)

pdf.rect( # BOX - title
    10, # X
    755, # Y
    600, # width
    30, # height
    fill=0
)

pdf.rect( # BOX - title categ's main inner box
    315, # X
    305, # Y - 305
    289, # width
    445, # height
    fill=0
)

pdf.rect( # BOX - title categ's hold box
    315, # X
    700, # Y - 700 aligns w top of ^
    289, # width
    50, # height
    fill=0
)

pdf.rect( # BOX - title categ's hold box 2nd line
    315, # X
    645, # Y (above_y -= 50) - 645
    289, # width
    55, # height
    fill=0
)

pdf.rect( # BOX - title categ's hold box 3rd line
    315, # X
    595, # Y (above_y -= 50)
    289, # width
    50, # height
    fill=0
)

pdf.rect( # BOX - title categ's low line
    315, # X
    545, # Y (above_y -= 50)
    289, # width
    50, # height
    fill=0
)


# LINES
pdf.line( # straight line - left col div
    380, # x1
    545, # y1 - low
    380, # x2
    700 # y2 - top
)

pdf.line( # straight line - mid col div
    460, # x1
    545, # y1 - low
    460, # x2
    700 # y2 - top
)

pdf.line( # straight line - right col div
    540, # x1
    545, # y1 - low
    540, # x2
    700 # y2 - top
)


# RECTS - TEXT BOXS
pdf.rect(40, 400, 220, 20, fill=0) # EMERGENCY SERVICES box
pdf.rect(20, 310, 125, 20, fill=0) # LOCAL POLICE box
pdf.rect(170, 310, 120, 20, fill=0) # LOCAL HOSPITAL box
pdf.rect(310, 760, 100, 20, fill=0) # CLIENT LOGO box
pdf.rect(365, 310, 200, 20, fill=0) # ALTERNATE HOSPITAL box


# TEXT TITLES:
pdf.drawString(418, 765, "EMERGENCY SERVICES")
pdf.drawString(50, 406, "EMERGENCY SERVICES MAP")
pdf.drawString(25, 315, "LOCAL POLICE DPT.")
pdf.drawString(175, 315, "LOCAL HOSPITAL")
pdf.drawString(320, 765, "CLIENT LOGO")
pdf.drawString(370, 315, "ALTERNATE HOSPITAL ROUTES")


# Bind fields to base PDF
pdf.save()


# PART II - OVERLAY EDITABLE FIELDS

# Load fields
fillpdfs.get_form_fields('base.pdf') #fillable_form

# TEXT BOXS
fillpdfs.place_text_box( # top row, 1st left
    'FieldName', # fieldname - make unique
    'LOCAL HOSPITAL & MEDICAL CENTER EMERGENCY ROOM', # placeholder in editable field
    317, # X
    100, # Y
    'base.pdf', # input pdf
    'blank.pdf', # output pdf
    1, # page num
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # top row, 2nd
    'FieldName2', 
    '(XXX)-XXX-XXXX', 
    390, 
    100, 
    'blank.pdf', 
    'blank2.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # top row, 3rd
    'FieldName3', 
    'ST, CITY, ZIP CODE', 
    468, 
    100, 
    'blank2.pdf', 
    'blank3.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # top row, 4th
    'FieldName4', 
    'XX Minutes', 
    540, 
    100, 
    'blank3.pdf', 
    'blank4.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # mid row, 1st
    'FieldName5', 
    'LOCAL POLICE DEPT.', 
    317, 
    150, 
    'blank4.pdf', 
    'blank5.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # mid row, 2nd
    'FieldName6', 
    '(XXX)-XXX-XXXX', 
    390, 
    150, 
    'blank5.pdf', 
    'blank6.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # mid row, 3rd
    'FieldName7', 
    'ST, CITY, ZIP CODE', 
    468, 
    150, 
    'blank6.pdf', 
    'blank7.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # mid row, 4th
    'FieldName8', 
    'XX Minutes', 
    540, 
    150, 
    'blank7.pdf', 
    'blank8.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # low row, 1st
    'FieldName9', 
    'LOCAL FIRE STATION', 
    317, 
    200, 
    'blank8.pdf', 
    'blank9.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # low row, 2nd
    'FieldName10', 
    '(XXX)-XXX-XXXX', 
    390, 
    200, 
    'blank9.pdf', 
    'blank10.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # low row, 3rd
    'FieldName11', 
    'ST, CITY, ZIP CODE', 
    468, 
    200, 
    'blank10.pdf', 
    'blank11.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

fillpdfs.place_text_box( # low row, 4th
    'FieldName12', 
    'XX Minutes', 
    540, 
    200, 
    'blank11.pdf', 
    'Slide9.pdf', 
    1, 
    width=60, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

# Func to remove extra 'in-between' pdfs:
def removePrePdfs():
    os.remove('blank.pdf')
    os.remove('blank2.pdf')
    os.remove('blank3.pdf')
    os.remove('blank4.pdf')
    os.remove('blank5.pdf')
    os.remove('blank6.pdf')
    os.remove('blank7.pdf')
    os.remove('blank8.pdf')
    os.remove('blank9.pdf')
    os.remove('blank10.pdf')
    os.remove('blank11.pdf')

removePrePdfs()
final_pdf = 'blank12.pdf'
print("\n PDF Generated : " + final_pdf)
