import fitz  # PyMuPDF
import os

# Configuration - Update these paths before running
input_folder_path = # Folder containing the PDFs to watermark
output_folder_path = # Folder where watermarked PDFs will be saved
watermark_file_path = # A4 PNG watermark system file path

# Ensure output folder exists
os.makedirs(output_folder_path, exist_ok=True)

def add_a4_png_watermark(pdf_path, watermark_path, output_path):
    """
    Overlays an A4-sized PNG watermark onto each page of a PDF.
    The watermark is scaled to match the dimensions of each page.
    
    :param pdf_path: Path to the input PDF file.
    :param watermark_path: Path to the PNG watermark file (A4 size).
    :param output_path: Path to save the watermarked PDF.
    """
    doc = fitz.open(pdf_path)

    for page in doc:
        rect = page.rect  # Get the dimensions of the page

        # Set watermark dimensions to cover the entire page (A4 matching)
        watermark_rect = fitz.Rect(0, 0, rect.width, rect.height)

        # Insert the PNG watermark covering the entire page
        page.insert_image(watermark_rect, filename=watermark_path, overlay=True)

    doc.save(output_path)
    doc.close()

# Process all PDFs in the input folder
for filename in os.listdir(input_folder_path):
    if filename.lower().endswith(".pdf"):
        input_pdf_path = os.path.join(input_folder_path, filename)
        output_pdf_path = os.path.join(output_folder_path, filename)

        add_a4_png_watermark(input_pdf_path, watermark_file_path, output_pdf_path)
        print(f"Watermarked: {filename}")

print("Batch A4 watermarking complete!")