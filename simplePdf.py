from fillpdf import fillpdfs
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# Define paths
input_pdf = 'fillable_form.pdf'
output_pdf = 'final_with_two_textboxes.pdf'
overlay1_pdf = 'overlay1.pdf'
overlay2_pdf = 'overlay2.pdf'

# Create the first overlay with a text box
fillpdfs.place_text_box(
    'FieldName',
    'prefilled_text_here',
    200, 169,
    input_pdf,
    overlay1_pdf,
    1,
    width=100,
    height=40,
    font_size=12,
    font_name=None,
    fill_color=(0.8, 0.8, 0.8),
    font_color=(0, 0, 0)
)

# Create the second overlay with a text box
fillpdfs.place_text_box(
    'FieldName2',
    'prefilled_text_here2',
    200, 269,
    input_pdf,
    overlay2_pdf,
    1,
    width=100,
    height=40,
    font_size=12,
    font_name=None,
    fill_color=(0.8, 0.8, 0.8),
    font_color=(0, 0, 0)
)

# Combine overlays with the base PDF
base_pdf = PdfReader(input_pdf)
overlay1 = PdfReader(overlay1_pdf)
overlay2 = PdfReader(overlay2_pdf)

# Prepare writer for final output
pdf_writer = PdfWriter()

# Add base page
base_page = base_pdf.pages[0]
pdf_writer.add_page(base_page)

# Merge overlays onto the first page
pdf_writer.pages[0].merge_page(overlay1.pages[0])  # Add first text box
pdf_writer.pages[0].merge_page(overlay2.pages[0])  # Add second text box

# Save the final combined PDF
with open(output_pdf, 'wb') as output_file:
    pdf_writer.write(output_file)

print(f"Final PDF with both text boxes saved to: {output_pdf}")
