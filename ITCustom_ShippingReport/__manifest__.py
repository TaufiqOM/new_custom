{
    'name': 'ITCustom Shipping Report',
    'version': '1.0',
    'summary': 'Add Pre Shipping report functionality to Batch Transfers',
    'description': '''
        This module adds Pre Shipping report capabilities to Batch Transfers.
        - Adds print button for Pre Shipping report
        - Integrates with existing stock_picking_batch module
    ''',
    'author': 'ITCustom',
    'website': 'https://www.itcustom.my.id/',
    'license': 'LGPL-3',
    'depends': ['stock_picking_batch', 'ITCustom_ShippingField'],
    'data': [
        'reports/pre_shipping_report.xml',
        'reports/pre_shipping_no_image_m3.xml',
        'reports/invoice_m3.xml',
        'reports/pre_stuffing_report.xml',
        'reports/report_actions.xml',
    ],
    'assets': {},
    'installable': True,
    'application': False,
}
