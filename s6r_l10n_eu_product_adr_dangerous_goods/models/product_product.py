#  Copyright 2025 Scalizer (<https://www.scalizer.fr>)
#  License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # Override
    adr_label_ids = fields.Many2many(related=None, compute='_compute_adr_label_ids')

    @api.depends('adr_goods_id', 'envir_hazardous')
    def _compute_adr_label_ids(self):
        dead_fish_label = self.env.ref('s6r_l10n_eu_product_adr_dangerous_goods.adr_label_environmentally_hazardous')
        for product in self:
            labels = product.adr_goods_id.label_ids
            if product.envir_hazardous == "yes":
                labels += dead_fish_label
            product.adr_label_ids = labels
