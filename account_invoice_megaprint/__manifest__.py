# -*- coding: utf-8 -*-

{
    'name': 'Connector FEL Megaprint - Odoo',
    'version': '1.0.1',
    'author': 'Abacus Solutions',
    'website': 'https://www.abacussolutions.com', 
    'support': 'Abacus Solutions', 
    'category': 'Accounting',
    'depends': ['account','num_to_words'],
    'summary': 'Connector FEL Megaprint - Odoo',
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/account_invoice.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/satdte_frases.xml',
        'views/account_journal_views.xml',
        'views/satdte_frases_data.xml',
        'wizard/wizard_cancel_view.xml',
        'reports/account_invoice_fel_format.xml',
        'reports/report_fel_format.xml'        
        
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
