# -*- coding: utf-8 -*-
{
    'name': "kursusku",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/python_view.xml',
        'views/tingkatan_view.xml',
        'views/inggris_view.xml',
        'views/jawa_view.xml',
        'views/bahasalain_view.xml',
        'views/penyelenggara_view.xml',
        'views/peserta_view.xml',
        'views/pengajar_view.xml',
        'views/sesionpy_view.xml',
        'views/sesionlain_view.xml',
        'views/sesioninggris_view.xml',
        'views/sesionjawa_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
