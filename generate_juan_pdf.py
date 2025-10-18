from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

# Create PDF
pdf_path = "/workspace/Juan_Lomeli_Info.pdf"
c = canvas.Canvas(pdf_path, pagesize=A4)

# Define margins
margin = 0.25 * inch
width, height = A4

# Title: "Juan Lomeli"
c.setFont("Times-Bold", 20)
c.drawCentredString(width / 2, height - margin - 20, "Juan Lomeli")

# Contact Info
c.setFont("Times-Roman", 12)
y_position = height - margin - 50

# Left side text: Address and phone
c.drawString(margin, y_position, "Dallas, Texas, 75241     (469) 781-0650")

# Right side text: Email and LinkedIn
right_text = "Juanlomeli1011@gmail.com     www.linkedin.com/in/juan-lomeli-888109247"
text_width = c.stringWidth(right_text, "Times-Roman", 12)
c.drawString(width - margin - text_width, y_position, right_text)

# Save PDF
c.save()

print(pdf_path)
