from fillpdf import fillpdfs

# Define the input and output PDF paths
input_pdf = 'fillable_form.pdf'
output_pdf = 'final_with_two_textboxes.pdf'

# Apply the first text box directly to the base PDF and save it temporarily
fillpdfs.place_text_box(
    'FieldName',
    'prefilled_text_here',
    200, 169,
    input_pdf,
    output_pdf,
    1,
    width=100,
    height=40,
    font_size=12,
    font_name=None,
    fill_color=(0.8, 0.8, 0.8),
    font_color=(0, 0, 0)
)

# Apply the second text box on the updated PDF (output_pdf) from the first step
fillpdfs.place_text_box(
    'FieldName2',
    'prefilled_text_here2',
    200, 269,
    output_pdf,
    output_pdf,
    1,
    width=100,
    height=40,
    font_size=12,
    font_name=None,
    fill_color=(0.8, 0.8, 0.8),
    font_color=(0, 0, 0)
)

print(f"Final PDF with both text boxes saved to: {output_pdf}")
