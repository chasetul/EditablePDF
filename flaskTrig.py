from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

app = Flask(__name__)

# Configuration for uploaded files
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")  # Create a simple HTML form for uploading

@app.route("/upload", methods=["POST"])
def upload_image():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        regenerate_pdf(filepath)  # Update the PDF with the uploaded image
        return "Image uploaded and PDF updated successfully!", 200
    return "Invalid file type", 400

def regenerate_pdf(image_path):
    # Regenerate the PDF with the new image
    file_name = 'blank7.pdf'
    pdf = canvas.Canvas(file_name, pagesize=letter)
    pdf.drawString(350, 700, "Security Guards:")
    # Other fields here...
    pdf.drawImage(image_path, 10, 600, width=300, height=155)
    pdf.save()

if __name__ == "__main__":
    app.run(port=5000, debug=True)

