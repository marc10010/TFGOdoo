# -*- coding: utf-8 -*-
{
    'name': "project_update",

    'summary': """
        Texto molon""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Marc Cortadellas",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        'views/project_view.xml',
    ],
}
