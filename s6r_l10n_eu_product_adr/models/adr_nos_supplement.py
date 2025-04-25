#  Copyright 2025 Scalizer (<https://www.scalizer.fr>)
#  License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class AdrNosSupplement(models.Model):
    _name = 'adr.nos.supplement'
    _description = 'N.O.S Entry Supplement'

    name = fields.Char(translate=True)
