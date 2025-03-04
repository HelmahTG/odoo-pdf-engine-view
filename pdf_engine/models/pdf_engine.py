from odoo import models, fields

class PdfEngine(models.Model):
    _name = "pdf.engine"
    _description = "PDF Engine"

    name = fields.Char("File Name", required=True)
    pdf_file = fields.Binary("PDF File", required=True)
