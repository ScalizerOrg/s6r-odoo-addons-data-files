#  Copyright 2025 Scalizer (<https://www.scalizer.fr>)
#  License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models


class PackagingType(models.Model):
    _inherit = "packaging.type"

    description = fields.Char()
    is_adr_approved = fields.Boolean("ADR Approved")
