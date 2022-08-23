from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vendors = fields.Many2one(string='Vendedor', comodel_name='vendor.model')

