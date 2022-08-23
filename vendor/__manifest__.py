{
    'name': 'Vendor',
    'summary': """Vendors""",
    'description': """
        Record Vendors""",
    'author': "Wellington Cuá -> wellington.cua@solucionesabacus.com",
    'category': ' Sale ',
    'version': '1.0',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/vendor_model_view.xml',
        'views/sale_views_extends.xml',
        'views/res_partner_extends_view.xml',
        'views/view_quotation_tree_extends.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}