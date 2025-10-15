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
    'depends': ['stock_picking_batch'],
    'data': [
        'reports/pre_shipping_report.xml',
        'reports/commercial_invoice.xml',
        'reports/packing_list.xml',
        'reports/invoice_doc.xml',
        'reports/report_actions.xml',
        'views/stock_picking_batch_views.xml',
    ],
    'assets': {
        'web.report_assets_pdf': [
            'ITCustom_ShippingReport/static/src/img/SICS.png',
        ],
    },
    'installable': True,
    'application': False,
}
