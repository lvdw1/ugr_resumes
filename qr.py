import os
import qrcode

# Directory where your PDFs are located
PDF_DIR = "pdfs"

# Directory to store generated QR code images
QR_DIR = "qr_codes"

# Base URL to your GitHub Pages site
# Note: adjust if your repo name or path is different
BASE_URL = "https://lvdw1.github.io/ugr_resumes/pdfs/"

# Ensure the output folder for QR codes exists
os.makedirs(QR_DIR, exist_ok=True)

# Loop through every file in the "pdfs" directory
for filename in os.listdir(PDF_DIR):
    if filename.endswith(".pdf"):
        # Construct the direct link to the PDF
        pdf_url = BASE_URL + filename

        # Create the QR code
        qr = qrcode.QRCode(
            version=1,  # controls the size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(pdf_url)
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color="blue", back_color="white")

        # Construct a filename for the QR code image (replace .pdf with .png)
        qr_filename = os.path.splitext(filename)[0] + ".png"
        qr_path = os.path.join(QR_DIR, qr_filename)

        # Save the QR code image
        img.save(qr_path)

        print(f"Generated QR code for: {filename} -> {qr_path}")
