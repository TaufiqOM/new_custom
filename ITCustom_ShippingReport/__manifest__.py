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
        'reports/invoice_doc_buyer_bern.xml',
        'reports/packing_list_buyer_bern.xml',
        'reports/shipping_plan_bernhardt.xml',
        'reports/report_actions.xml',
    ],
    'assets': {},
    'installable': True,
    'application': False,
}
