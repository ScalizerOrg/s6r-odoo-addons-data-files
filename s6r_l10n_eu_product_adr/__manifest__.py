# Copyright 2025 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Scalizer ADR Dangerous Goods',
    'version': '18.0.1.0.0',
    'author': 'Scalizer',
    'website': 'https://www.scalizer.fr',
    'summary': "Improved ADR Dangerous Goods handling",
    'sequence': 0,
    'license': 'LGPL-3',
    'depends': [
        'l10n_eu_product_adr',
    ],
    'category': 'Generic Modules/Scalizer',
    'complexity': 'easy',
    'description': '''
This module adds features for handling ADR Dangerous Goods that are missing from the OCA module.
    ''',
    'qweb': [
    ],
    'demo': [
    ],
    'images': [
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Data
        'data/adr.goods.csv',
        'data/adr_label.xml',
        # Views
        'views/adr_goods_views.xml',
        'views/product_template_views.xml',
        'views/adr_label_views.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
