
from odoo import models, fields, api, _

class AccountPaymentRegister(models.Model):
    _inherit = "account.payment.register"

    reciboInterno = fields.Char(string="No. Recibo Interno")
    noLiquidacion = fields.Char(string="No. De Liquidación")
    noDeposito = fields.Char(string="Depósito Bancario")