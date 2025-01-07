from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pdfrw import PdfReader, PdfWriter, PageMerge
from pdfrw.objects.pdfname import PdfName

def create_pdf_with_upload_button(output_filename):
    # Step 1: Create a basic PDF with a button
    pdf_path = "base_img.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 700, "Click the button below to upload a photo:")
    
    # Add a button for upload
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    #pdfmetrics.registerFont(TTFont("Helvetica", "Helvetica"))
    c.setFont("Times-Roman", 12)
    c.drawString(130, 680, "Upload Photo")
    
    # Finish the base PDF
    c.showPage()
    c.save()

    # Step 2: Add an interactive button using pdfrw
    template_pdf = PdfReader(pdf_path)
    page = template_pdf.pages[0]

    # Define AcroForm field (button) dictionary
    button = {
        PdfName.FT: PdfName.Btn,
        PdfName.T: "(Upload Button)",
        PdfName.DA: "/Helvetica 12 Tf 0 g",
        PdfName.Rect: [120, 650, 250, 680],  # Button dimensions
        PdfName.H: PdfName.P,  # Push-button type
        PdfName.AA: {
            PdfName.U: {PdfName.S: PdfName.JS, PdfName.JS: "(app.alert('Upload triggered'))"}
        }
    }

    # Append to the page annotations
    if not hasattr(page, "Annots") or page.Annots is None:
        page.Annots = []
    page.Annots.append(button)

    # Save the modified PDF
    PdfWriter(output_filename, trailer=template_pdf).write()

# Create the PDF
output_pdf = "uploadImage.pdf"
create_pdf_with_upload_button(output_pdf)
print(f"Interactive PDF saved to {output_pdf}")
