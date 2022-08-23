{
    'name': 'Hide Fields to Invoice',
    'version': '1.0',
    'author': "Wellington Cua -> wellington.cua@solucionesabacus.com",
    'summary': """ This module hide invoice fields """,
    'description': """
        This module hide invoice fields  
    """,
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'views/hide_invoice_fields.xml',
        'views/payment_register_inherit.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
