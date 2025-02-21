from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf(output_filename="interactive.pdf"):
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter

    # Draw text
    c.drawString(100, height - 100, "Click the button below to open a Tkinter modal:")

    # Define button position
    x, y, w, h = 100, height - 150, 200, 30

    # Draw a rectangle to simulate a button
    c.rect(x, y, w, h, stroke=1, fill=0)

    # Add button label
    c.drawString(x + 60, y + 10, "Open Tkinter")

    # Add an annotation that acts as a button
    js_code = "app.launchURL('file:///Users/chase/Desktop/AlphaRecon/juptyterbooks/EditablePDF/open_tkinter.py', true);"
    
    c.linkURL("javascript:" + js_code, (x, y, x + w, y + h), relative=0)

    c.save()
    print(f"PDF created: {output_filename}")

create_pdf()
