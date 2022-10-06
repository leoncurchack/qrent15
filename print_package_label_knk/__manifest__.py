# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).
{
    'name': 'Print Package Label ZPL',
    'version': '1.0',
    "summary": 'Print Package Label ZPL module allows user to print ZPL Package Label',
    'description': """
Print Package Label ZPL
======================================
06/10/2022:[ADD][VSC]: Added Print Package Label ZPL Report in Tranfers Form View
""",
    'category': 'Inventory/Inventory',
    'author': 'Kanak Infosystems LLP.',
    'website': 'https://www.kanakinfosystems.com',
    'images': ['static/description/banner.jpg'],
    'depends': ['stock'],
    'data': [
        'report/package_label_zpl_views.xml',
        'report/reports.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'currency': 'EUR',
    'price': '00',
}
