from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# Create LABELS for the fields
pdf.drawString(380, 710, "TOP CUSTOMER COMPLAINTS :")
pdf.drawString(420, 695, "(LAST 90 DAYS)")
pdf.drawString(360, 660, "NUMBER 1 COMPLAINT:")
pdf.drawString(360, 640, "NUMBER 2 COMPLAINT:")
pdf.drawString(360, 620, "NUMBER 3 COMPLAINT:")
pdf.drawString(360, 600, "NUMBER 4 COMPLAINT:")
pdf.drawString(360, 580, "NUMBER 5 COMPLAINT:")

# INFO STR :
pdf.drawString(20, 360, "CUSTOMER COMPLAINTS DISCLAIMER:")
# pdf.drawString(375, 380, "Report cybercrime to the FBI's Internet")
# pdf.drawString(375, 360, "Crime Complaint Center (IC3).")



# IMAGES :
image_path2 = "logo copy.png"  # logo right side
pdf.drawImage(image_path2, 550, 750, width=50, height=30)


# BOXES :
pdf.rect( # BOX - MAIN
    10, # X
    310, # Y
    590, # width
    470, # height
    fill=0
)
pdf.rect( # BOX - Items outline left Lg
    10, # X
    390, # Y
    340, # width
    390, # height 
    fill=0
)
# CUSTOMER REVIEW SAMPLE BOXES
pdf.rect( # BOX - Items outline left Inner col0,row0
    15, # X
    720, # Y
    160, # width
    50, # height 
    fill=0
)
pdf.rect( # BOX - Items outline left Inner col0,row1
    185, # X
    720, # Y
    160, # width
    50, # height 
    fill=0
)
pdf.rect( # BOX - Items outline left Inner col1,row0
    15, # X
    650, # Y
    160, # width
    50, # height 
    fill=0
)
pdf.rect( # BOX - Items outline left Inner col1,row1
    185, # X
    650, # Y
    160, # width
    50, # height 
    fill=0
)
pdf.rect( # BOX - Items outline left Inner col2,row0
    15, # X
    580, # Y
    160, # width
    50, # height 
    fill=0
)
pdf.rect( # BOX - Items outline left Inner col2,row1
    185, # X
    580, # Y
    160, # width
    50, # height 
    fill=0
)
pdf.rect( # BOX - Items outline left Inner col3,row0
    15, # X
    510, # Y
    160, # width
    50, # height 
    fill=0
)
pdf.rect( # BOX - Items outline left Inner col3,row1
    185, # X
    510, # Y
    160, # width
    50, # height 
    fill=0
)
# RIGHT SIDE BOXES
pdf.rect( # BOX - Lg right
    355, # X
    390, # Y
    240, # width
    350, # height 
    fill=0
)
pdf.rect( # BOX - Lg low info box
    15, # X
    315, # Y
    580, # width
    70, # height 
    fill=0
)


# RECTS - TEXT BOX - EMERGENCY SERVICES MAP
# pdf.rect(
#     200, # X
#     210, # Y
#     180, # Width
#     20, # Height
#     fill=0
# )


# TEXT TITLES:
pdf.drawString(
    400, # X
    750, # Y
    "CUSTOMER REVIEWS" # STR
)

# LINK TRIALs:
# So far these don't work great
# file_path = '/Users/chase/Desktop'
# pdf.linkURL('https://{file_path}', # 'https://localhost/index.html'
#     (200, 
#      500, 
#      300, 
#      600
#     ), 
#     relative=0,
#     thickness=1
#     #color='(0,0,255)' # blue
# )
#pdf.cell(100, 50, txt="Open File", link="file:///absolute/path/to/your/file.jpg", border=0, align="C")

#pdf.linkURL(f'https://{file_path}', (200, 500, 300, 600), relative=0)

#pdf.drawImage() # May work if image name is grabbed as user input

# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
fillpdfs.place_text_box( # 0 - right complaint
    'FieldName', 
    'Complaint', 
    505, 
    117, 
    'base.pdf', 
    'blank.pdf', 
    1, 
    width=80, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 1 - right complaint
    'FieldName1', 
    'Complaint', 
    505, 
    137, 
    'blank.pdf', 
    'blank1.pdf', 
    1, 
    width=80, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 2 - right complaint
    'FieldName2', 
    'Complaint', 
    505, 
    157, 
    'blank1.pdf', 
    'blank2.pdf', 
    1, 
    width=80, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 3 - right complaint
    'FieldName3', 
    'Complaint', 
    505, 
    177, 
    'blank2.pdf', 
    'blank3.pdf', 
    1, 
    width=80, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # 4 - right complaint
    'FieldName4', 
    'Complaint', 
    505, 
    197, 
    'blank3.pdf', 
    'blank4.pdf', 
    1, 
    width=80, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

# TEXTBOXES - LEFT SIDE
fillpdfs.place_text_box( # (0,0) - upper left
    'FieldName5', 
    'INSERT SAMPLE OF CUSTOMER REVIEW', 
    20, # X
    25, # Y
    'blank4.pdf', 
    'blank5.pdf', 
    1, 
    width=150, 
    height=44, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # (1,0) - upper right
    'FieldName6', 
    'INSERT SAMPLE OF CUSTOMER REVIEW', 
    190, 
    25, 
    'blank5.pdf', 
    'blank6.pdf', 
    1, 
    width=150, 
    height=44, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # (0,1)
    'FieldName7', 
    'INSERT SAMPLE OF CUSTOMER REVIEW', 
    20, 
    95, 
    'blank6.pdf', 
    'blank7.pdf', 
    1, 
    width=150, 
    height=44, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # (1,1)
    'FieldName8', 
    'INSERT SAMPLE OF CUSTOMER REVIEW', 
    190, 
    95, 
    'blank7.pdf', 
    'blank8.pdf', 
    1, 
    width=150, 
    height=44, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # (0,2)
    'FieldName9', 
    'INSERT SAMPLE OF CUSTOMER REVIEW', 
    20, 
    165, 
    'blank8.pdf', 
    'blank9.pdf', 
    1, 
    width=150, 
    height=44, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # (1,2)
    'FieldName10', 
    'INSERT SAMPLE OF CUSTOMER REVIEW', 
    190, 
    165, 
    'blank9.pdf', 
    'blank10.pdf', 
    1, 
    width=150, 
    height=44, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # (0,3)
    'FieldName11', 
    'INSERT SAMPLE OF CUSTOMER REVIEW', 
    20, 
    235, 
    'blank10.pdf', 
    'blank11.pdf', 
    1, 
    width=150, 
    height=44, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # (0,3)
    'FieldName12', 
    'INSERT SAMPLE OF CUSTOMER REVIEW', 
    190, 
    235, 
    'blank11.pdf', 
    'blank12.pdf', 
    1, 
    width=150, 
    height=44, 
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
final_pdf = 'blank3.pdf'
print("\n PDF Generated : " + final_pdf)
