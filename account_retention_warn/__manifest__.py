# -*- coding: utf-8 -*-
{
    'name': 'Tax Retention Warning',
    'version': '15.0.0.1',
    'category': 'Accounting',
    'summary': """
        Tax Retention Warning on Invoice""",
    'depends': ['account'],
    'data': [
        'views/account_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}