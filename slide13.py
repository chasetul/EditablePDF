from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# Create LABELS for the fields
pdf.drawString(360, 710, "TOP recommended ALERT Method :")
pdf.drawString(400, 590, "OTHER RESOURCES")
pdf.drawString(370, 430, "$$Location$$ SIGACTS IN THE NEWS")


# INFO STR :
pdf.drawString(20, 600, "Photo or screenshot of any public notification systems,")
pdf.drawString(20, 580, "office of Public Safety, WHATSAPP, Twitter Feeds for")
pdf.drawString(20, 560, "mayor, security department, etc.")

# RIGHT MID BOX TEXT
pdf.drawString(342, 560, ">  $$Target$$ CONTRACTOR GUIDE:")
pdf.drawString(342, 540, ">  $$Target$$ FACILITIES GUIDE:")
pdf.drawString(342, 520, ">  $$Target$$ SECURITY PAGE:")
pdf.drawString(342, 500, ">  EMERGENCY NUMBERS:")



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
    15, # X
    315, # Y
    320, # width
    460, # height 
    fill=0
)

# RIGHT SIDE BOXES
pdf.rect( # BOX - upper right
    340, # X
    640, # Y
    255, # width
    100, # height 
    fill=0
)
pdf.rect( # BOX - right mid
    340, # X
    480, # Y
    255, # width
    100, # height 
    fill=0
)
pdf.rect( # BOX - right lower
    340, # X
    320, # Y
    255, # width
    100, # height 
    fill=0
)



# TEXT TITLES:
pdf.drawString(
    400, # X
    750, # Y
    "EMERGENCY ALERTS" # STR
)

# LINK TRIALs:
pdf.linkURL('https://alpharecon.com', 
    (200, 
     500, 
     300, 
     540
    ), 
    relative=0,
    thickness=1
    #color='(0,0,255)' # blue
)
pdf.drawString(220, 515, "Click Here")


# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
fillpdfs.place_text_box( # upper right rec method
    'FieldName', 
    'Enter here', 
    370, 
    100, 
    'base.pdf', 
    'blank.pdf', 
    1, 
    width=200, 
    height=40, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # contractors guide
    'FieldName1', 
    'or blueprints with link', 
    555, 
    220, 
    'blank.pdf', 
    'blank1.pdf', 
    1, 
    width=40, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # faciilies
    'FieldName2', 
    'A breif overview of Facilities', 
    535, 
    240, 
    'blank1.pdf', 
    'blank2.pdf', 
    1, 
    width=60, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # security page
    'FieldName3', 
    'Go to the $$target$$ security page for updates on weapons, marijuana, vehicle inspection, & do not disturb policies.', 
    525, 
    260, 
    'blank2.pdf', 
    'blank3.pdf', 
    1, 
    width=70, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # emergency nums
    'FieldName4', 
    'Additional contacts for $$Location$$ Health District. Includes several public safety FAQs and emergency services contacts', 
    505, 
    280, 
    'blank3.pdf', 
    'blank4.pdf', 
    1, 
    width=90, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # lower right SIGACTS
    'FieldName5', 
    'List of news reports with links (3-4 is generally enough with URL linked)', 
    360, # X
    400, # Y
    'blank4.pdf', 
    'blank5.pdf', 
    1, 
    width=210, 
    height=50, 
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
final_pdf = 'blank5.pdf'
print("\n PDF Generated : " + final_pdf)
