import qrcode

# URL to the PDF resume
pdf_url = "https://github.com/lvdw1/ugr_resumes/louis_vandewalle.pdf"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data (the PDF URL) to the QR code
qr.add_data(pdf_url)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("louis_vandewalle.png")
