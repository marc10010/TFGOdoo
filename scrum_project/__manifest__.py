# -*- coding: utf-8 -*-
{
    'name': "ScrumProject",

    'summary': """
        Este modulo es una actualizacion del modulo Proyectos de Odoo que nos permite llevar una seguimiento scrum de los proyectos.
        """,

    'description': """
        Este modulo es una actualizacion del modulo Proyectos de Odoo que nos permite llevar una seguimiento scrum de los proyectos.
    """,

    'author': "Marc Cortadellas",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom',
    'version': '0.1',
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['project.task'],

    # always loaded
    'data': [
    ],
}
