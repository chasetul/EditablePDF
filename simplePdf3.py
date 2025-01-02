from fillpdf import fillpdfs
import os

# This version essentially works the best, as it just removes the unnecessary 
# copy of the pdf and keeps final pdf with 2 textboxes. For 2+ textboxes it 
# will have to delete more temp pdf files.


# Define file paths
input_pdf = 'fillable_form.pdf'
intermediate_pdf = 'intermediate.pdf'
final_pdf = 'final_with_two_textboxes.pdf'

# Step 1: Apply the first text box and save to an intermediate file
fillpdfs.place_text_box(
    'FieldName',
    'prefilled_text_here',
    200, 169,
    input_pdf,
    intermediate_pdf,
    1,
    width=100,
    height=40,
    font_size=12,
    font_name=None,
    fill_color=(0.8, 0.8, 0.8),
    font_color=(0, 0, 0)
)

# Step 2: Apply the second text box to the intermediate file and save to the final file
fillpdfs.place_text_box(
    'FieldName2',
    'prefilled_text_here2',
    200, 269,
    intermediate_pdf,
    final_pdf,
    1,
    width=100,
    height=40,
    font_size=12,
    font_name=None,
    fill_color=(0.8, 0.8, 0.8),
    font_color=(0, 0, 0)
)

# Optional: Clean up intermediate file
os.remove(intermediate_pdf)

print(f"Final PDF with both text boxes saved to: {final_pdf}")
