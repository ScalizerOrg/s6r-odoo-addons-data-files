# Copyright 2025 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Scalizer Scalizer l10n Eu Product Adr Dangerous Goods',
    'version': '18.0.1.0.0',
    'author': 'Scalizer',
    'website': 'https://www.scalizer.fr',
    'summary': "Improved l10n Eu Product Adr Dangerous Goods",
    'sequence': 0,
    'license': 'LGPL-3',
    'depends': [
        'l10n_eu_product_adr_dangerous_goods',
    ],
    'category': 'Generic Modules/Scalizer',
    'complexity': 'easy',
    'description': '''
This module customized and fixes the OCA module "l10n Eu Product Adr Dangerous Goods".
    ''',
    'qweb': [
    ],
    'demo': [
    ],
    'images': [
    ],
    'data': [
        # Security
        # Data
        'data/adr_label.xml',
        # Views
        'views/product_template_views.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
