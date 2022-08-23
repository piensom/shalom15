# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    payment_status = fields.Selection([('fully_paid', 'Fully Paid'),
                                        ('not_paid', 'Not Paid'),
                                        ('no_invoice', 'No Invoice'),
                                        ('partial_paid', 'Partial Paid')], 'Payment Status', compute="_compute_invoice_state")
    amount_due = fields.Float(string="Amount Due", compute='_compute_invoice_state')

    @api.depends('state', 'invoice_ids')
    def _compute_invoice_state(self):
        for order in self:
            if order.invoice_ids:
                if all([invoice_id.payment_state == "paid" for invoice_id in order.invoice_ids]):
                    order.payment_status = "fully_paid"
                    order.amount_due = 0.0
                elif all([invoice_id.payment_state == "not_paid" for invoice_id in order.invoice_ids]):
                    order.payment_status = "not_paid"
                    order.amount_due = sum(order.invoice_ids.mapped('amount_residual'))            
                else:
                    order.payment_status = "partial_paid"
                    order.amount_due = sum(order.invoice_ids.mapped('amount_residual'))
            else:
                order.payment_status = "no_invoice"
                order.amount_due = 0.0

