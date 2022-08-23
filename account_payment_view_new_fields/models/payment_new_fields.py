from odoo import models, fields, api, _

class AccountPayment(models.Model):
    _inherit = "account.payment"

    no_recibo_interno = fields.Char(string="No. Recibo Interno")
    no_de_liquidacion = fields.Char(string="No. De Liquidación")
    deposito_bancario = fields.Char(string="Depósito Bancario")