# -*- coding: utf-8 -*-
{
    'name': "project_update",

    'summary': """
        Texto molon de verdad
        """,

    'description': """
        Esto es una extension para el modulo de proyectos
    """,

    'author': "Marc Cortadellas",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project', 'base'],

    # always loaded
    'data': [
        'views/project_view.xml',
    ],
}
