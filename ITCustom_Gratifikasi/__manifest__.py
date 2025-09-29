{
    'name': 'ITCustom Gratifikasi',
    'version': '1.0',
    'depends': ['web'],
    'category': 'Customization',
    'summary': 'Add anti-gratification statement above footer in all PDF reports',
    'description': 'This module adds a statement "Tidak menerima gratifikasi / suap dalam bentuk apapun" above the footer in every PDF report in Odoo.',
    'data': [
        'views/report_layout_inherit.xml',
    ],
    'installable': True,
    'application': False,
}
