{
    'name': 'Hide Button by User',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Hide specific buttons for specific users',
    'description': """
        This module allows hiding specific buttons for specific users based on configuration.
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/hide_button_views.xml',
        'views/res_users_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'texthide_button_user/static/src/js/hide_button.js',
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
