from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_fir_pdf(fir_text: str) -> BytesIO:
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    # Start writing text
    textobject = p.beginText(40, 800)  # (x, y) starting point

    for line in fir_text.split("\n"):
        textobject.textLine(line)

    p.drawText(textobject)
    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer
