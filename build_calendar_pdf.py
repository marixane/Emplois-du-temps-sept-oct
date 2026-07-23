from pathlib import Path

from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


ROOT = Path(__file__).parent
OUTPUT = ROOT / "output" / "pdf" / "calendrier-scolaire-2026-2027.pdf"
PAGE_W, PAGE_H = 842, 595  # A4 landscape in points


def draw_contained(pdf, image_path):
    image_reader = ImageReader(str(image_path))
    width, height = image_reader.getSize()
    scale = min(PAGE_W / width, PAGE_H / height)
    draw_w, draw_h = width * scale, height * scale
    x = (PAGE_W - draw_w) / 2
    y = (PAGE_H - draw_h) / 2
    pdf.drawImage(image_reader, x, y, draw_w, draw_h, preserveAspectRatio=True, mask="auto")


OUTPUT.parent.mkdir(parents=True, exist_ok=True)
pdf = canvas.Canvas(str(OUTPUT), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
for image_name in ("calendrier-semestre-1.png", "calendrier-semestre-2.png"):
    draw_contained(pdf, ROOT / "assets" / image_name)
    pdf.showPage()
pdf.save()
print(OUTPUT)
