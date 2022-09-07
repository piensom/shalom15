
{
    'name': 'Payment Widget Extra',
    'version': '14.0',
    'summary': """
        Payment custom fields on register payment widget.
    """,

    'description': """
        Payment custom fields on register payment widget.
    """,

    'author': 'Piensom',
    'website': 'https://www.piensom.com',
    'price': 19.99,
    'currency': 'USD',
    
    'depends': [
        'account_accountant',
    ],

    'data': [
        'wizard/account_payment_register_views.xml',
    ],

    
    'installable': True,
    'application': True,
    'auto_install': False,
}
