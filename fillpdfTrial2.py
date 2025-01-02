from fillpdf import fillpdfs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


file_name = 'base.pdf'

pdf = canvas.Canvas(file_name, pagesize=letter)

image_path = "logo copy.png"  # Replace with your image file path
pdf.drawImage(image_path, 100, 500, width=300, height=150)

# Extract fields from the PDF to inspect available form fields
fillpdfs.get_form_fields('fillable_form.pdf')


fillpdfs.place_text_box('FieldName', 'prefilled_text_here', 200, 169, 'fillable_form.pdf', 'blank.pdf', 1, width=100, height=40, font_size=12, font_name=None, fill_color=(0.8,0.8,0.8), font_color=(0,0,0))

fillpdfs.place_text_box('FieldName2', 'prefilled_text_here2', 200, 269, 'blank.pdf', 'blank2.pdf', 1, width=100, height=40, font_size=12, font_name=None, fill_color=(0.8,0.8,0.8), font_color=(0,0,0))

fillpdfs.place_image(file_name, x, y, input_pdf_path, output_map_path, page_number, width=10, height=10)
