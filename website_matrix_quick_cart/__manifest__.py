# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

{
    'name': 'Website matrix quick cart',
    'version': '15.0.1.0',
    'summary': 'This module allow to show Product Variant in matrix view in website sale and user directly add product in cart from matrix view.',
    'description': "",
    'license': 'OPL-1',
    'author': 'Kanak Infosystems LLP.',
    'website': 'https://www.kanakinfosystems.com',
    'category': 'Tools',
    'depends': ['website_sale'],
    'data': [
        'views/matrix_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_matrix_quick_cart/static/src/js/website_sale.js',
        ],
    },
    'sequence': 1,
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 30,
    'currency': 'EUR',
    'images': ['static/description/banner.gif'],
}
