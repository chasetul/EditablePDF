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
# pdf.drawString(350, 695, "CROSSROAD 1:")
# pdf.drawString(350, 675, "CROSSROAD 2:")
# pdf.drawString(350, 655, "CROSSROAD 3:")
# pdf.drawString(350, 635, "CROSSROAD 4:")
# pdf.drawString(350, 615, "DESTINATION MAIN ENTRANCE:")




# LEFT SIDE TEXT
pdf.drawString(18, 515, "ALT MAIN ENTRANCE")
pdf.drawString(25, 760, "MAIN ENTRANCE")

# TOP 4 ROW TITLE TEXT
pdf.drawString(170, 760, "REF. 1")
pdf.drawString(260, 760, "REF. 2")
pdf.drawString(350, 760, "REF. 3")
pdf.drawString(440, 760, "REF. 4")
pdf.drawString(530, 760, "REF. 5")
pdf.drawString(530, 585, "REF. 6")
pdf.drawString(530, 480, "REF. 7")
pdf.drawString(530, 375, "REF. 8")

# mid lowest text
pdf.drawString(250, 300, "GENEREAL ORIENTATION")

# upper middle text
pdf.drawString(250, 600, "INSERT SATELLITE VIEW OF")
pdf.drawString(250, 580, "TARGET DESTINATION WITH")
pdf.drawString(250, 560, "SURROUNDING STREETS")
pdf.drawString(250, 540, "HIGHLIGHTED")

# under alt main entrce text
pdf.drawString(40, 480, "INSERT")
pdf.drawString(40, 460, "SATELLITE")
pdf.drawString(40, 440, "IMAGE OF ALT.")
pdf.drawString(40, 420, "ENTRANCE")

# under  main entrce text
pdf.drawString(40, 730, "INSERT")
pdf.drawString(40, 710, "SATELLITE")
pdf.drawString(40, 690, "IMAGE OF")
pdf.drawString(40, 670, "MAIN")
pdf.drawString(40, 650, "ENTRANCE")







# IMAGES :
# image_path2 = "logo copy.png"  # logo right side
# pdf.drawImage(image_path2, 550, 750, width=50, height=30)


# MAIN BOX OUTLINE
pdf.rect( # BOX - MAIN
    10, # X
    180, # Y
    590, # width
    600, # height
    fill=0
)

# LEFT SIDE BOXES :
pdf.rect( # BOX - left low 
    15, # X
    290, # Y
    130, # width
    240, # height 
    fill=0
)
pdf.rect( # BOX - left high
    15, # X
    535, # Y
    130, # width
    240, # height 
    fill=0
)
pdf.rect( # BOX - bottom title box - left
    15, # X
    510, # Y
    130, # width
    20, # height 
    fill=0
)
pdf.rect( # BOX - upper title box - left
    15, # X
    755, # Y
    130, # width
    20, # height 
    fill=0
)

# MIDDLE MAIN BOX
pdf.rect( # BOX - outline mid lg
    150, # X
    290, # Y
    350, # width
    380, # height 
    fill=0
)

# TOP MINI BOXES 4 ACROSS
pdf.rect( # BOX - 0 (leftmost)
    150, # X
    675, # Y
    85, # width
    100, # height 
    fill=0
)
pdf.rect( # BOX - 1
    238, # X
    675, # Y
    85, # width
    100, # height 
    fill=0
)
pdf.rect( # BOX - 2
    327, # X
    675, # Y
    85, # width
    100, # height 
    fill=0
)
pdf.rect( # BOX - 3
    415, # X
    675, # Y
    85, # width
    100, # height 
    fill=0
)
pdf.rect( # BOX - TOP title 0
    150, # X
    755, # Y
    85, # width
    20, # height 
    fill=0
)
pdf.rect( # BOX - TOP title 1
    238, # X
    755, # Y
    85, # width
    20, # height 
    fill=0
)
pdf.rect( # BOX - TOP title 2
    327, # X
    755, # Y
    85, # width
    20, # height 
    fill=0
)
pdf.rect( # BOX - TOP title 3
    415, # X
    755, # Y
    85, # width
    20, # height 
    fill=0
)

# RIGHT SIDE BOXS
pdf.rect( # BOX - 0 UPMOST
    505, # X
    605, # Y
    90, # width
    170, # height 
    fill=0
)
pdf.rect( # BOX - 1
    505, # X
    500, # Y
    90, # width
    100, # height 
    fill=0
)
pdf.rect( # BOX - 2
    505, # X
    395, # Y
    90, # width
    100, # height 
    fill=0
)
pdf.rect( # BOX - 3
    505, # X
    290, # Y
    90, # width
    100, # height 
    fill=0
)
# RIGHT SIDE BOX TITLES
pdf.rect( # BOX - right upmost title 0
    505, # X
    755, # Y
    90, # width
    20, # height 
    fill=0
)
pdf.rect( # BOX - 1
    505, # X
    580, # Y
    90, # width
    20, # height 
    fill=0
)
pdf.rect( # BOX - 2
    505, # X
    475, # Y
    90, # width
    20, # height 
    fill=0
)
pdf.rect( # BOX - 3
    505, # X
    370, # Y
    90, # width
    20, # height 
    fill=0
)
pdf.rect( # BOX - gen orientation
    230, # X
    295, # Y
    200, # width
    20, # height 
    fill=0
)



# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS
# fillpdfs.place_text_box( # crossroad 1
#     'FieldName', 
#     'SUMMARY OF CROSSROAD 1 WITH RELEVANT LOCATION DETAILS', 
#     445, 
#     80, 
#     'base.pdf', 
#     'blank.pdf', 
#     1, 
#     width=140, 
#     height=20, 
#     font_size=12, 
#     font_name=None, 
#     fill_color=(0.8,0.8,0.8), 
#     font_color=(0,0,0)
#  )



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
