#  Copyright 2025 Scalizer (<https://www.scalizer.fr>)
#  License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class AdrGoods(models.Model):
    _inherit = "adr.goods"

    is_nos_entry = fields.Boolean("N.O.S. Entry",
                                  help="The dangerousness of products assigned to this entry will have be supplemented")
