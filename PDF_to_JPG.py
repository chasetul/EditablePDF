from pdf2image import convert_from_path

inpFile = "baseDoc.pdf"
# Convert PDF to images
images = convert_from_path(inpFile)

# Save each page as a JPG file
for i, image in enumerate(images):
    image.save(f"output_jpg_page_{i+1}.jpg", "JPEG")
