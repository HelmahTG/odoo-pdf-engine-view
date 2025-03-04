{
    "name": "PDF Engine for Odoo",
    "summary": "A custom PDF Engine for handling large drawing files in Odoo",
    "description": """Handling large drawing files in Odoo. 
        This module integrates a custom PDF Engine into Odoo, allowing users to upload 
        and review large PDF drawings efficiently. Optimized for architecture and 
        engineering firms working with large blueprint PDFs.""",
    "author": "Helmah",
    "website": "https://rayka-soft.com/",
    "category": "Tools",
    "version": "1.0",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/pdf_viewer_view.xml",
    ],
    "assets": {},
    "installable": True,
    "application": True,
}
