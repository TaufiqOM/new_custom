{
    'name': 'IT Custom Report MTO',
    'version': '1.0',
    'summary': 'Add MTO Report to Sale Orders',
    'description': '''
        This module adds an MTO report to sale orders with custom fields and print button.
    ''',
    'author': 'A Yazid Bustomi',
    'website': 'https://www.bustomi.my.id/',
    'license': 'LGPL-3',
    'depends': ['sale', 'account'],
    'data': [
        'reports/mto_reports.xml',
        'reports/report_mto_template.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
