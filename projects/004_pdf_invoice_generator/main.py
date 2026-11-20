# -*- coding: utf-8 -*-
"""
4. PDF Invoice Generator
Generate professional invoices from a JSON order file.
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import json

def generate_invoice(order_file="order.json", output_pdf="invoice.pdf"):
    with open(order_file, "r", encoding="utf-8") as f:
        order = json.load(f)
    doc = SimpleDocTemplate(output_pdf, pagesize=A4, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    story = [
        Paragraph("<b>INVOICE</b>", styles["Title"]),
        Paragraph(f"<b>Customer:</b> {order['customer']}", styles["Normal"]),
        Spacer(1, 15)
    ]
    rows = [["Item", "Qty", "Price", "Amount"]]
    total = 0
    for x in order["items"]:
        amount = x["qty"] * x["price"]
        total += amount
        rows.append([x["name"], str(x["qty"]), f"${x['price']:.2f}", f"${amount:.2f}"])
    rows.append(["", "", "TOTAL", f"${total:.2f}"])
    t = Table(rows, colWidths=[230, 50, 80, 90])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.black),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")
    ]))
    story += [t, Spacer(1, 20), Paragraph("Thank you for your business.", styles["Normal"])]
    doc.build(story)
    print(f"[+] {output_pdf} created successfully for {order['customer']}.")

if __name__ == "__main__":
    generate_invoice()
