# -*- coding: utf-8 -*-

from num2words import num2words
from odoo import api, fields, models, _
from odoo.addons.num_to_words.models.numero_letras import numero_a_letras, numero_a_moneda

class AccountInvoice(models.Model):
    _inherit = "account.move"

    text_amount = fields.Char(string="Montant en lettre", required=False, compute="amount_to_words" )

    @api.depends('amount_total')
    def amount_to_words(self):
        if self.journal_id.is_factura_especial:
            self.text_amount = numero_a_moneda(self.amount_total_fe_lines)
        else:
            self.text_amount = numero_a_moneda(self.amount_total)