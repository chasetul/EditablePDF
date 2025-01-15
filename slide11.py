from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# Create LABELS for the fields
pdf.drawString(360, 700, "VENUE INTERNET:")
pdf.drawString(360, 680, "WORK DEVICES:")
pdf.drawString(360, 660, "PERSONAL DEVICES:")
pdf.drawString(360, 640, "PETTY CYBERCRIME:")
# INFO STR :
pdf.drawString(375, 400, "HOW TO REPORT CYBERCRIME:")
pdf.drawString(375, 380, "Report cybercrime to the FBI's Internet")
pdf.drawString(375, 360, "Crime Complaint Center (IC3).")
# pdf.drawString(15, 620, "Maj. PD Non-Emergency:")
# pdf.drawString(15, 600, "Local Hospital:")
# pdf.drawString(15, 580, "Local Fire Station:")
# pdf.drawString(15, 560, "Local Fire & Rescue:")
# pdf.drawString(15, 540, "Human Trafficking Line:")


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
pdf.rect( # BOX - Items outline upper left
    10, # X
    480, # Y
    340, # width
    300, # height 260
    fill=0
)
pdf.rect( # BOX - Lg low
    10, # X
    320, # Y
    340, # width
    150, # height 260
    fill=0
)
pdf.rect( # BOX - Sm left down items
    15, # X
    485, # Y
    140, # width
    140, # height 260
    fill=0
)
pdf.rect( # BOX - Sm left up items
    15, # X
    635, # Y
    140, # width
    140, # height 260
    fill=0
)
pdf.rect( # BOX - Md right items
    165, # X
    485, # Y
    180, # width
    290, # height 260
    fill=0
)
pdf.rect( # BOX - Lg right
    355, # X
    320, # Y
    240, # width
    420, # height 260
    fill=0
)
pdf.rect( # BOX - Lg low right
    360, # X
    325, # Y
    230, # width
    100, # height 260
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
    "CYBER VULNERABILITY" # STR
)

# LINK TRIALs:
file_path = '/Users/chase/Desktop'
pdf.linkURL('https://{file_path}', # 'https://localhost/index.html'
    (200, 
     500, 
     300, 
     600
    ), 
    relative=0,
    thickness=1
    #color='(0,0,255)' # blue
)
#pdf.cell(100, 50, txt="Open File", link="file:///absolute/path/to/your/file.jpg", border=0, align="C")

#pdf.linkURL(f'https://{file_path}', (200, 500, 300, 600), relative=0)


#pdf.drawImage() # May work if image name is grabbed as user input

# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
fillpdfs.place_text_box( # 
    'FieldName', # fieldname - not sure how to use
    'Enter text here', # placeholder in editable field
    480, # X
    77, # Y : Smaller num = higher on page
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
    'Enter text here', 
    480, 
    97, 
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
    'Enter text here', 
    490, 
    117, 
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
    'Enter text here', 
    490, 
    137, 
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
# fillpdfs.place_text_box( # 4
#     'FieldName4', 
#     '(XXX)-XXX-XXXX', 
#     188, 
#     97, 
#     'blank3.pdf', 
#     'blank4.pdf', 
#     1, 
#     width=100, 
#     height=15, 
#     font_size=12, 
#     font_name=None, 
#     fill_color=(0.8,0.8,0.8), 
#     font_color=(0,0,0)
# )
# fillpdfs.place_text_box( # 5
#     'FieldName5', 
#     '(XXX)-XXX-XXXX', 
#     188, 
#     117, 
#     'blank4.pdf', 
#     'blank5.pdf', 
#     1, 
#     width=100, 
#     height=15, 
#     font_size=12, 
#     font_name=None, 
#     fill_color=(0.8,0.8,0.8), 
#     font_color=(0,0,0)
# )
# fillpdfs.place_text_box( # 6
#     'FieldName6', 
#     '(XXX)-XXX-XXXX', 
#     188, 
#     137, 
#     'blank5.pdf', 
#     'blank6.pdf', 
#     1, 
#     width=100, 
#     height=15, 
#     font_size=12, 
#     font_name=None, 
#     fill_color=(0.8,0.8,0.8), 
#     font_color=(0,0,0)
# )
# fillpdfs.place_text_box( # 7
#     'FieldName7', 
#     '(XXX)-XXX-XXXX', 
#     188, 
#     157, 
#     'blank6.pdf', 
#     'blank7.pdf', 
#     1, 
#     width=100, 
#     height=15, 
#     font_size=12, 
#     font_name=None, 
#     fill_color=(0.8,0.8,0.8), 
#     font_color=(0,0,0)
# )
# fillpdfs.place_text_box( # 8
#     'FieldName8', 
#     '(XXX)-XXX-XXXX', 
#     188, 
#     177, 
#     'blank7.pdf', 
#     'blank8.pdf', 
#     1, 
#     width=100, 
#     height=15, 
#     font_size=12, 
#     font_name=None, 
#     fill_color=(0.8,0.8,0.8), 
#     font_color=(0,0,0)
# )
# fillpdfs.place_text_box( # 9
#     'FieldName9', 
#     '(XXX)-XXX-XXXX', 
#     188, 
#     197, 
#     'blank8.pdf', 
#     'blank9.pdf', 
#     1, 
#     width=100, 
#     height=15, 
#     font_size=12, 
#     font_name=None, 
#     fill_color=(0.8,0.8,0.8), 
#     font_color=(0,0,0)
# )
# fillpdfs.place_text_box( # 10
#     'FieldName10', 
#     '(XXX)-XXX-XXXX', 
#     188, 
#     217, 
#     'blank9.pdf', 
#     'blank10.pdf', 
#     1, 
#     width=100, 
#     height=15, 
#     font_size=12, 
#     font_name=None, 
#     fill_color=(0.8,0.8,0.8), 
#     font_color=(0,0,0)
# )
# fillpdfs.place_text_box( # 11
#     'FieldName11', 
#     '(XXX)-XXX-XXXX', 
#     188, 
#     237, 
#     'blank10.pdf', 
#     'blank11.pdf', 
#     1, 
#     width=100, 
#     height=15, 
#     font_size=12, 
#     font_name=None, 
#     fill_color=(0.8,0.8,0.8), 
#     font_color=(0,0,0)
# )


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
