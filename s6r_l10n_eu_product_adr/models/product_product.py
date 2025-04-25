#  Copyright 2025 Scalizer (<https://www.scalizer.fr>)
#  License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    nos_supplement_ids = fields.Many2many('adr.nos.supplement', 'product_nos_supplement_rel', 'product_id',
                                          'supplement_id', string="N.O.S Supplements",
                                          help="Supplements to the dangerousness")
    adr_goods_is_nos_entry = fields.Boolean(related="adr_goods_id.is_nos_entry")

    @api.model_create_multi
    def create(self, vals_list):
        """Propagate the template's adr settings when creating variants"""
        for vals in vals_list:
            if "product_tmpl_id" in vals and "nos_supplement_ids" not in vals:
                template = self.env["product.template"].browse(vals["product_tmpl_id"])
                vals.update(nos_supplement_ids=template.nos_supplement_ids.ids)
        return super().create(vals_list)
