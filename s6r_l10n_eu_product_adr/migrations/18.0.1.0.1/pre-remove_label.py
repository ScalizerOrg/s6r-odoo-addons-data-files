#  Copyright 2025 Scalizer (<https://www.scalizer.fr>)
#  License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, SUPERUSER_ID

def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})

    record = env.ref('s6r_l10n_eu_product_adr.adr_label_environmentally_hazardous', raise_if_not_found=False)
    if record:
        record.unlink()
