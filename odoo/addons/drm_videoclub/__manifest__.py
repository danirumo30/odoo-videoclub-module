# -*- coding: utf-8 -*-
{
    'name': "drm_videoclub",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'reports/report_actor.xml',
        'reports/report_director.xml',
        'reports/report_pelicula.xml',
        'views/menus.xml',
        'views/pelicula.xml',
        'views/categoria.xml',
        'views/director.xml',
        'views/actor.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

