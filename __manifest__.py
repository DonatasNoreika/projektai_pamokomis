# -*- coding: utf-8 -*-
{
    'name': "Donato Projektai",

    'summary': """Manage projects""",

    'summary': """Projektų valdymo programa""",

    'description': """
        Projektų valdymo programa leidžia:
            - sukurti projektus
            - priskirti projektams darbus
            - priskirti klientams projektus
            - išrašyti sąskaitas
    """,

    'author': "Donatas Noreika",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/work_view.xml',
        'views/invoice_view.xml',
        'views/partner_inherited_view.xml',
        'views/employee_inherited_view.xml',
        'reports/project_report.xml',
        'reports/invoice_report.xml',
        'views/project_board.xml',
        'mail_templates.xml',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}