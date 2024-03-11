from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import shutil
from docx import Document
from docx2pdf import convert

def image_to_pdf(image_path, output_folder):
    # Open the image
    img = Image.open(image_path)

    # Get the size of the image
    width, height = img.size

    # Construct the output PDF filename
    pdf_filename = os.path.splitext(os.path.basename(image_path))[0] + ".pdf"
    pdf_path = os.path.join(output_folder, pdf_filename)

    # Check if the PDF file already exists
    index = 1
    while os.path.exists(pdf_path):
        pdf_filename = os.path.splitext(os.path.basename(image_path))[0] + f"_{index}.pdf"
        pdf_path = os.path.join(output_folder, pdf_filename)
        index += 1

    # Create a canvas object
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add the image to the PDF
    c.drawImage(image_path, 0, 0, width, height)

    # Save the PDF
    c.save()

    print(f"PDF created successfully: {pdf_path}")




def docx_to_pdf(docx_path, output_folder):
    # Open the Word document
    doc = Document(docx_path)

    # Construct the output PDF filename
    pdf_filename = os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"
    pdf_path = os.path.join(output_folder, pdf_filename)

    # Check if the PDF file already exists
    index = 1
    while os.path.exists(pdf_path):
        pdf_filename = os.path.splitext(os.path.basename(docx_path))[0] + f"_{index}.pdf"
        pdf_path = os.path.join(output_folder, pdf_filename)
        index += 1

    # Create a canvas object
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add content from the Word document to the PDF
    for para in doc.paragraphs:
        c.drawString(100, 700, para.text)  # Adjust coordinates as needed

    # Save the PDF
    c.save()

    print(f"PDF created successfully: {pdf_path}")


def move_pdf_files(source_folder, dest_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # List all files in the source folder
    files = os.listdir(source_folder)

    # Move PDF files to the destination folder
    for file in files:
        if file.lower().endswith('.pdf'):
            source_path = os.path.join(source_folder, file)
            dest_path = os.path.join(dest_folder, file)

            # Check if the destination path already exists
            index = 1
            while os.path.exists(dest_path):
                file_name, file_ext = os.path.splitext(file)
                new_file_name = f"{file_name}_{index}{file_ext}"
                dest_path = os.path.join(dest_folder, new_file_name)
                index += 1

            shutil.move(source_path, dest_path)
            print(f"PDF moved successfully: {dest_path}")

# Specify the folder containing the images, docx, and PDFs
source_folder = "050224"

# Specify the folder to save the PDFs
output_folder = "converted"

# Specify the folder to move PDFs
pdf_folder = "converted"

# List all files in the source folder
files = os.listdir(source_folder)

# Convert images and docx to PDF and move PDFs to another directory
for file in files:
    file_path = os.path.join(source_folder, file)
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_to_pdf(file_path, output_folder)
        
    elif file.lower().endswith('.docx'):
        docx_to_pdf(file_path, output_folder)
    else:
        print(file)

# Move PDF files to another directory
move_pdf_files(source_folder, pdf_folder)
