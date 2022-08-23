{
    'name': 'New Fields Register Payent',
    'summary': """Add new field""",
    'description': """
        Add field named, No.Recibo interno, No. de liquidación, Depósito bancario"
    """,
    'author': "Cesar Ajche -> cesar.ajche@solucionesabacus.com",
    'category': 'Accounting ',
    'version': '1.0',
    'depends': ['account'],
    'data': [
        'views/new_fields.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
