#  Copyright 2025 Scalizer (<https://www.scalizer.fr>)
#  License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models
from odoo.exceptions import UserError

ADR_FIELDS = ['envir_hazardous']


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    envir_hazardous = fields.Selection(related='product_variant_ids.envir_hazardous', readonly=False)
    adr_label_ids = fields.Many2many(related="product_variant_ids.adr_label_ids")  # Override

    @api.depends(*(f'product_variant_ids.{fname}' for fname in ADR_FIELDS))
    def _compute_adr_goods_on_variants(self):
        """ Override to consider added fields. """
        super()._compute_adr_goods_on_variants()
        for template in self:
            first_product = template.product_variant_ids[:1]
            template.adr_goods_on_variants |= not all(
                product[fname] == first_product[fname]
                for fname in ADR_FIELDS
                for product in template.product_variant_ids[1:]
            )

    def write(self, values):
        """Delegate dangerous goods fields to variants

        while preventing a sweeping change over variants with different settings
        """
        values = values.copy()
        variant_vals = {}
        for field in ADR_FIELDS:
            if field in values:
                variant_vals[field] = values.pop(field)
        res = super().write(values)
        if variant_vals:
            if any(template.adr_goods_on_variants for template in self):
                raise UserError(
                    self.env._(
                        "There are different dangerous goods configured on this product's variant, so you cannot "
                        "update these from here. Please reconfigure each variant separately."
                    )
                )
            self.mapped("product_variant_ids").write(variant_vals)
        return res

    @api.model_create_multi
    def create(self, vals_list):
        """Propagate the template's adr settings on the created variants"""
        res = super().create(vals_list)
        for template, vals in zip(res, vals_list, strict=False):
            variant_vals = {}
            for field in ADR_FIELDS:
                if field in vals:
                    variant_vals[field] = vals[field]
            if variant_vals:
                template.product_variant_ids.write(variant_vals)
        return res
