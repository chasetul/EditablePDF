from fillpdf import fillpdfs

# Extract fields from the PDF to inspect available form fields
fillpdfs.get_form_fields('fillable_form.pdf')

# Prepare data to populate the fields
# data = {
#     'FieldName': 'Value for field1',
#     'field2': 'Value for field2',
# }

# Fill the PDF with the data
#fillpdfs.write_fillable_pdf('fillable_form.pdf', 'output_filled.pdf', data)

# WORKS BEST - Place text box
fillpdfs.place_text_box('FieldName', 'prefilled_text_here', 200, 169, 'fillable_form.pdf', 'blank.pdf', 1, width=100, height=40, font_size=12, font_name=None, fill_color=(0.8,0.8,0.8), font_color=(0,0,0))
#fillpdfs.place_text_box('FieldName2', 'prefilled_text_here2', 200, 269, 'fillable_form.pdf', 'blank.pdf', 1, width=100, height=40, font_size=12, font_name=None, fill_color=(0.8,0.8,0.8), font_color=(0,0,0))


# TRIAL - Use blank.pdf to overlay second text_box onto blank2.pdf: ----------------
#fillpdfs.get_form_fields('blank.pdf')

# data = {
#     'FieldName': 'Value for field1',
#     'field2': 'Value for field2',
# }
#fillpdfs.write_fillable_pdf('blank.pdf', 'blank2.pdf', data)

fillpdfs.place_text_box('FieldName2', 'prefilled_text_here2', 200, 269, 'blank.pdf', 'blank2.pdf', 1, width=100, height=40, font_size=12, font_name=None, fill_color=(0.8,0.8,0.8), font_color=(0,0,0))
# TRIAL - END ----------------------------------------------------------------------



# Place text
#fillpdfs.place_text('Alpha Recon', 10, 10, 'fillable_form.pdf', 'blank.pdf', 1, font_size=12, font_name="helv", color=None)

# WORKS WELL - Dropdown
#fillpdfs.place_dropdown('FieldName', ["Option1", "Option2"], 250, 250, 'fillable_form.pdf', 'blank.pdf', 1, width=100, height=40, font_size=12, font_name=None, fill_color=(0.8,0.8,0.8), font_color=(0,0,0))

# flatten the PDF (make it non-editable)
#fillpdfs.flatten_pdf('output_filled.pdf', 'output_flattened.pdf')

# Open in Preview
import subprocess
def open_in_preview(file_path):
    subprocess.call(["open", "-a", "Preview", file_path])
open_in_preview('blank2.pdf')
