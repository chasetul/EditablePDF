from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# RIGHT SIDE TEXT
pdf.drawString(370, 695, "SUMMARY OF AVG. TEMPERATURES")
pdf.drawString(370, 675, "AND WEATHER FOR THE MONTH")
pdf.drawString(370, 655, "OF TRAVEL WITH IMPACT")
pdf.drawString(370, 635, "STATEMENT. All in text format")

pdf.drawString(370, 435, "AVERAGE PRECIPITATION FOR")
pdf.drawString(370, 415, "DESTINATION GRAPHIC")





# LEFT SIDE TEXT
pdf.drawString(20, 720, "CLIMATE AND WEATHER AVERAGES GRAPHIC FOR")
pdf.drawString(20, 700, "DESTINATION CITY")

pdf.drawString(20, 580, "MONTH CLIMATE AND WEATHER AVERAGES FOR")
pdf.drawString(20, 560, "DESTINATION CITY")

pdf.drawString(20, 460, "ASSESSMENT: Weather will have an overall IMPACT LEVEL")

pdf.drawString(20, 440, "ENVIRONMENTAL EFFECTS")
pdf.line( # line from (x1,y1) -> (x2, y2)
    20, # X1
    438, # Y1
    180, # X2
    438  # Y2
)

pdf.drawString(20, 420, "Visibility will have AMOUNT effect on TYPE assets")
pdf.drawString(20, 400, "Winds will have AMOUNT effect on TYPE assets")
pdf.drawString(20, 380, "Precipitation will have AMOUNT effect on TYPE assets")
pdf.drawString(20, 360, "Cloud Cover will have AMOUNT effect on TYPE assets")
pdf.drawString(20, 340, "Temperature will have AMOUNT effect on TYPE assets")

pdf.drawString(20, 320, "OPERATIONAL IMPACTS")
pdf.line( # line from (x1,y1) -> (x2, y2)
    20, # X1
    318, # Y1
    160, # X2
    318  # Y2
)

pdf.drawString(20, 300, "AMOUNT impact on TYPE and AMOUNT impact on TYPE")







# pdf.drawString(110, 440, "VIEW")
# pdf.drawString(110, 420, "IMAGE")

# pdf.drawString(40, 430, "INSERT")
# pdf.drawString(40, 410, "MAP OF")
# pdf.drawString(40, 390, "MAIN")
# pdf.drawString(40, 370, "ENTRANCE")

# pdf.drawString(40, 307, "MAIN ENTRANCE")

# # LOWER SMALL RIGHT TEXT
# pdf.drawString(270, 460, "STREET")
# pdf.drawString(270, 440, "VIEW")
# pdf.drawString(270, 420, "IMAGE")

# pdf.drawString(200, 430, "INSERT")
# pdf.drawString(200, 410, "MAP OF")
# pdf.drawString(200, 390, "MAIN")
# pdf.drawString(200, 370, "ENTRANCE")

# pdf.drawString(200, 307, "REAR ENTRANCE")




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
pdf.rect( # BOX - left top
    15, # X
    615, # Y
    340, # width
    160, # height 
    fill=0
)
pdf.rect( # BOX - left mid
    15, # X
    490, # Y
    340, # width
    120, # height 
    fill=0
)
pdf.rect( # BOX - left lower outline
    15, # X
    290, # Y
    340, # width
    195, # height 
    fill=0
)


# RIGHT SIDE BOXES
pdf.rect( # BOX - outline right lg
    360, # X
    290, # Y
    235, # width
    450, # height 
    fill=0
)
pdf.rect( # BOX - lower
    365, # X
    295, # Y
    225, # width
    225, # height 
    fill=0
)
pdf.rect( # BOX - lower
    365, # X
    525, # Y
    225, # width
    210, # height 
    fill=0
)




# TEXT TITLES:
pdf.drawString(
    390, # X
    750, # Y
    "MON. WEATHER CITY" # STR
)



# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS - right side
fillpdfs.place_text_box( # crossroad 1
    'FieldName', 
    'SUMMARY OF AVG. TEMPERATURES AND WEATHER FOR THE MONTH OF TRAVEL WITH IMPACT STATEMENT.', 
    368, 
    80, 
    'base.pdf', 
    'blank.pdf', 
    1, 
    width=220, 
    height=140, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

# TEXT BOXS - left side
fillpdfs.place_text_box( # upper - impact level
    'FieldName1', 
    'IMPACT LEVEL', 
    260, 
    318, 
    'blank.pdf', 
    'blank1.pdf', 
    1, 
    width=90, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # upper - amount
    'FieldName2', 
    'AMOUNT', 
    113, 
    358, 
    'blank1.pdf', 
    'blank2.pdf', 
    1, 
    width=60, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # upper - type
    'FieldName3', 
    'TYPE', 
    220, 
    358, 
    'blank2.pdf', 
    'blank3.pdf', 
    1, 
    width=35, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # amount
    'FieldName4', 
    'AMOUNT', 
    103, 
    378, 
    'blank3.pdf', 
    'blank4.pdf', 
    1, 
    width=60, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # type
    'FieldName5', 
    'TYPE', 
    210, 
    378, 
    'blank4.pdf', 
    'blank5.pdf', 
    1, 
    width=35, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # amount
    'FieldName6', 
    'AMOUNT', 
    134, 
    398, 
    'blank5.pdf', 
    'blank6.pdf', 
    1, 
    width=60, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # type
    'FieldName7', 
    'TYPE', 
    243, 
    398, 
    'blank6.pdf', 
    'blank7.pdf', 
    1, 
    width=35, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # amount
    'FieldName8', 
    'AMOUNT', 
    134, 
    418, 
    'blank7.pdf', 
    'blank8.pdf', 
    1, 
    width=60, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # type
    'FieldName9', 
    'TYPE', 
    243, 
    418, 
    'blank8.pdf', 
    'blank9.pdf', 
    1, 
    width=35, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # amount
    'FieldName10', 
    'AMOUNT', 
    138, 
    438, 
    'blank9.pdf', 
    'blank10.pdf', 
    1, 
    width=60, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # type
    'FieldName11', 
    'TYPE', 
    246, 
    438, 
    'blank10.pdf', 
    'blank11.pdf', 
    1, 
    width=35, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # amount
    'FieldName12', 
    'AMOUNT', 
    15, 
    478, 
    'blank11.pdf', 
    'blank12.pdf', 
    1, 
    width=60, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # type
    'FieldName13', 
    'TYPE', 
    128, 
    478, 
    'blank12.pdf', 
    'blank13.pdf', 
    1, 
    width=35, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # amount
    'FieldName14', 
    'AMOUNT', 
    184, 
    478, 
    'blank13.pdf', 
    'blank14.pdf', 
    1, 
    width=60, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # type
    'FieldName15', 
    'TYPE', 
    300, 
    478, 
    'blank14.pdf', 
    'Slide3.pdf', 
    1, 
    width=35, 
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
final_pdf = 'blank15.pdf'
print("\n PDF Generated : " + final_pdf)
