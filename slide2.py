from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# === SLIDE 10 ===

file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

# PART I - SETUP PDF FIELDS / BOXES

# RIGHT SIDE TEXT
# pdf.drawString(370, 695, "SUMMARY OF AVG. TEMPERATURES")
# pdf.drawString(370, 675, "AND WEATHER FOR THE MONTH")
# pdf.drawString(370, 655, "OF TRAVEL WITH IMPACT")
# pdf.drawString(370, 635, "STATEMENT. All in text format")

# pdf.drawString(370, 435, "AVERAGE PRECIPITATION FOR")
# pdf.drawString(370, 415, "DESTINATION GRAPHIC")





# LEFT SIDE TEXT
# pdf.drawString(20, 720, "CLIMATE AND WEATHER AVERAGES GRAPHIC FOR")
# pdf.drawString(20, 700, "DESTINATION CITY")

# pdf.drawString(20, 580, "MONTH CLIMATE AND WEATHER AVERAGES FOR")
# pdf.drawString(20, 560, "DESTINATION CITY")

# pdf.drawString(20, 460, "ASSESSMENT: Weather will have an overall IMPACT LEVEL")

# pdf.drawString(20, 440, "ENVIRONMENTAL EFFECTS")
# pdf.line( # line from (x1,y1) -> (x2, y2)
#     20, # X1
#     438, # Y1
#     180, # X2
#     438  # Y2
# )

# pdf.drawString(20, 420, "Visibility will have AMOUNT effect on TYPE assets")
# pdf.drawString(20, 400, "Winds will have AMOUNT effect on TYPE assets")
# pdf.drawString(20, 380, "Precipitation will have AMOUNT effect on TYPE assets")
# pdf.drawString(20, 360, "Cloud Cover will have AMOUNT effect on TYPE assets")
# pdf.drawString(20, 340, "Temperature will have AMOUNT effect on TYPE assets")

# pdf.drawString(20, 320, "OPERATIONAL IMPACTS")
# pdf.line( # line from (x1,y1) -> (x2, y2)
#     20, # X1
#     318, # Y1
#     160, # X2
#     318  # Y2
# )

# pdf.drawString(20, 300, "AMOUNT impact on TYPE and AMOUNT impact on TYPE")






# RIGHT SIDE TEXT
pdf.drawString(250, 700, "Satellite Level")
pdf.drawString(233, 680, "Image of Destination")

pdf.drawString(370, 700, "Satellite Level")
pdf.drawString(353, 680, "Image of Destination")

pdf.drawString(490, 700, "Satellite Level")
pdf.drawString(473, 680, "Image of Destination")

pdf.drawString(273, 560, "Climate and Weather Averages for Destination City")

pdf.drawString(330, 505, "TRAVEL SAFETY TIPS")

pdf.drawString(230, 488, "TRAVELLING:")

pdf.drawString(230, 458, "MAKE COPIES OF")
pdf.drawString(230, 448, "YOUR DOCUMENTS:")

pdf.drawString(230, 418, "SECURE YOUR ITEMS:")

pdf.drawString(230, 378, "SECURE DEVICES:")

pdf.drawString(230, 338, "DON'T ACCEPT DRINKS")
pdf.drawString(230, 328, "FROM STRANGERS:")

pdf.drawString(430, 488, "EMERGENCY NUMBERS:")

pdf.drawString(430, 448, "BE ON THE LOOKOUT:")

pdf.drawString(430, 408, "SCAMS:")

pdf.drawString(430, 368, "SECURE YOUR ROOM:")

pdf.drawString(430, 328, "DON'T OVERSHARE INFO:")



#LEFT SIDE TEXT
pdf.drawString(15, 600, "Destination Name")
pdf.drawString(15, 580, "1-XXX-XXX-XXXX")
pdf.drawString(15, 560, "Street Name,")
pdf.drawString(15, 540, "City, Zip Code")

pdf.drawString(20, 750, "Turn by Turn")
pdf.drawString(20, 730, "Directions")
pdf.drawString(20, 710, "written out")

pdf.drawString(120, 710, "Street Map with")
pdf.drawString(120, 690, "route from arrival")
pdf.drawString(120, 670, "point to final")
pdf.drawString(120, 650, "destination")

pdf.drawString(25, 460, "Threat Risk")
pdf.drawString(25, 440, "List w/ Color")

pdf.drawString(102, 500, "Venue Reservations:")
pdf.drawString(102, 485, "XXX-XXX-XXXX")

pdf.drawString(102, 475, "Venue Concierge:")
pdf.drawString(102, 460, "XXX-XXX-XXXX")

pdf.drawString(102, 450, "Location Emergency:")
pdf.drawString(102, 435, "XXX-XXX-XXXX")

pdf.drawString(102, 425, "Venue Emergency:")
pdf.drawString(102, 410, "XXX-XXX-XXXX")

pdf.drawString(102, 400, "Emergency:")
pdf.drawString(102, 385, "911")

pdf.drawString(70, 370, "Venue on site Emergency:")
pdf.drawString(70, 358, "XXX-XXX-XXXX")

pdf.drawString(70, 348, "Local PD Non-Emergency:")
pdf.drawString(70, 335, "XXX-XXX-XXXX")

pdf.drawString(70, 325, "Major PD Non-Emergency:")
pdf.drawString(70, 310, "XXX-XXX-XXXX")

pdf.drawString(70, 300, "Nearest Hospital:")
pdf.drawString(70, 285, "XXX-XXX-XXXX")

pdf.drawString(70, 275, "Local Fire Station:")
pdf.drawString(70, 260, "XXX-XXX-XXXX")

pdf.drawString(70, 250, "Local Fire & Rescue:")
pdf.drawString(70, 235, "XXX-XXX-XXXX")

pdf.drawString(70, 225, "Human Trafficking Line:")
pdf.drawString(70, 210, "XXX-XXX-XXXX")






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
    525, # Y
    200, # width
    250, # height 
    fill=0
)
pdf.rect( # BOX - left lower outline
    15, # X
    200, # Y
    200, # width
    320, # height 
    fill=0
)
pdf.rect( # BOX - low mini left
    15, # X
    525, # Y
    100, # width
    100, # height 
    fill=0
)
pdf.rect( # BOX - high mini left
    15, # X
    640, # Y
    100, # width
    135, # height 
    fill=0
)
pdf.rect( # BOX - lowest sm leftmost
    20, # X
    380, # Y
    80, # width
    135, # height 
    fill=0
)


# RIGHT SIDE BOXES
pdf.rect( # BOX - outline right lg
    220, # X
    290, # Y
    375, # width
    450, # height 
    fill=0
)
pdf.rect( # BOX - lower outline
    225, # X
    295, # Y
    365, # width
    225, # height 
    fill=0
)
pdf.rect( # BOX - higher outline
    225, # X
    525, # Y
    365, # width
    210, # height 
    fill=0
)
pdf.rect( # BOX - higher outline - inside - lowest long
    230, # X
    530, # Y
    355, # width
    80, # height 
    fill=0
)
pdf.rect( # BOX - higher outline - inside - left
    230, # X
    615, # Y
    115, # width
    115, # height 
    fill=0
)
pdf.rect( # BOX - higher outline - inside - mid
    350, # X
    615, # Y
    115, # width
    115, # height 
    fill=0
)
pdf.rect( # BOX - higher outline - inside - right
    470, # X
    615, # Y
    115, # width
    115, # height 
    fill=0
)
pdf.rect( # BOX - lower title card
    225, # X
    500, # Y
    365, # width
    20, # height 
    fill=0
)




# TEXT TITLES:
pdf.drawString(
    310, # X
    750, # Y
    "LOCATION EXECUTIVE HANDOUT" # STR
)



# BIND FIELDS TO PDF
pdf.save()
fillpdfs.get_form_fields('base.pdf')


# PART II - ADD EDITABLE FIELDS


# TEXT BOXS - right side
fillpdfs.place_text_box( # loc
    'FieldName', 
    'LOCATION', 
    308, 
    27, 
    'base.pdf', 
    'blank.pdf', 
    1, 
    width=68, 
    height=20, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)

# TEXT BOXS - left side
fillpdfs.place_text_box( # upper - venue
    'FieldName1', 
    'XXX-XXX-XXXX', 
    101, 
    294, 
    'blank.pdf', 
    'blank1.pdf', 
    1, 
    width=90, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # venue conc
    'FieldName2', 
    'XXX-XXX-XXXX', 
    101, 
    319, 
    'blank1.pdf', 
    'blank2.pdf', 
    1, 
    width=90, 
    height=15, 
    font_size=12, 
    font_name=None, 
    fill_color=(0.8,0.8,0.8), 
    font_color=(0,0,0)
)
fillpdfs.place_text_box( # loc emg
    'FieldName3', 
    'XXX-XXX-XXXX', 
    101, 
    344, 
    'blank2.pdf', 
    'blank3.pdf', 
    1, 
    width=90, 
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
final_pdf = 'blank15.pdf'
print("\n PDF Generated : " + final_pdf)
