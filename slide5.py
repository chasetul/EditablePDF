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
pdf.drawString(350, 695, "CROSSROAD 1:")
pdf.drawString(350, 675, "CROSSROAD 2:")
pdf.drawString(350, 655, "CROSSROAD 3:")
pdf.drawString(350, 635, "CROSSROAD 4:")
pdf.drawString(350, 615, "DESTINATION MAIN ENTRANCE:")




# LEFT SIDE TEXT
pdf.drawString(70, 660, "INSERT MAP OF DESTINATION WITH")
pdf.drawString(70, 640, "MAJOR CROSSROADS IDENTIFIED")

# LOWER SMALL LEFT TEXT
pdf.drawString(110, 460, "STREET")
pdf.drawString(110, 440, "VIEW")
pdf.drawString(110, 420, "IMAGE")

pdf.drawString(40, 430, "INSERT")
pdf.drawString(40, 410, "MAP OF")
pdf.drawString(40, 390, "MAIN")
pdf.drawString(40, 370, "ENTRANCE")

pdf.drawString(40, 307, "MAIN ENTRANCE")

# LOWER SMALL RIGHT TEXT
pdf.drawString(270, 460, "STREET")
pdf.drawString(270, 440, "VIEW")
pdf.drawString(270, 420, "IMAGE")

pdf.drawString(200, 430, "INSERT")
pdf.drawString(200, 410, "MAP OF")
pdf.drawString(200, 390, "MAIN")
pdf.drawString(200, 370, "ENTRANCE")

pdf.drawString(200, 307, "REAR ENTRANCE")




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
    490, # Y
    320, # width
    285, # height 
    fill=0
)
pdf.rect( # BOX - left lower outline
    15, # X
    290, # Y
    320, # width
    195, # height 
    fill=0
)
pdf.rect( # BOX - left sm low left
    20, # X
    295, # Y
    150, # width
    185, # height 
    fill=0
)
pdf.rect( # BOX - left sm low left - corner left
    100, # X
    410, # Y
    70, # width
    70, # height 
    fill=0
)
pdf.rect( # BOX - left sm low left - low text box LEFT
    30, # X
    300, # Y
    130, # width
    20, # height 
    fill=0
)
pdf.rect( # BOX - left sm low right
    180, # X
    295, # Y
    150, # width
    185, # height 
    fill=0
)
pdf.rect( # BOX - left sm low left - corner right
    260, # X
    410, # Y
    70, # width
    70, # height 
    fill=0
)
pdf.rect( # BOX - left sm low left - low text box RIGHT
    190, # X
    300, # Y
    130, # width
    20, # height 
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




# TEXT TITLES:
pdf.drawString(
    390, # X
    750, # Y
    "AVENUES OF APPROACH" # STR
)



# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
fillpdfs.place_text_box( # crossroad 1
    'FieldName', 
    'SUMMARY OF CROSSROAD 1 WITH RELEVANT LOCATION DETAILS', 
    445, 
    80, 
    'base.pdf', 
    'blank.pdf', 
    1, 
    width=140, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
 )
fillpdfs.place_text_box( # crossroad 2
    'FieldName1', 
    'SUMMARY OF CROSSROAD 2 WITH RELEVANT LOCATION DETAILS', 
    445, 
    102, 
    'blank.pdf', 
    'blank1.pdf', 
    1, 
    width=140, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
 )
fillpdfs.place_text_box( # crossroad 3
    'FieldName2', 
    'SUMMARY OF CROSSROAD 3 WITH RELEVANT LOCATION DETAILS', 
    445, 
    124, 
    'blank1.pdf', 
    'blank2.pdf', 
    1, 
    width=140, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
 )
fillpdfs.place_text_box( # crossroad 4
    'FieldName3', 
    'SUMMARY OF CROSSROAD 4 WITH RELEVANT LOCATION DETAILS', 
    445, 
    146, 
    'blank2.pdf', 
    'blank3.pdf', 
    1, 
    width=140, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
 )
fillpdfs.place_text_box( # dest main entrance
    'FieldName3', 
    'SUMMARY OF MAIN ENTRANCE', 
    375, 
    186, 
    'blank3.pdf', 
    'blank4.pdf', 
    1, 
    width=200, 
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
