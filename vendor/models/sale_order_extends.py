from odoo import fields, models, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_id')
    def _onchange_customer_vendor(self):
        for rec in self:
            rec.seller = rec.partner_id.vendors

    seller = fields.Many2one(string='Vendedor', comodel_name='vendor.model')
