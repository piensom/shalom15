# -*- coding: utf-8 -*-
{
    'name': 'Impuesto Global',
    'version': '14.0.0.1',
    'sequence': 70,
    'summary': 'Impuesto por monto Global de Factura',
    'description': """""",
    'depends': ['account','purchase'],
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
