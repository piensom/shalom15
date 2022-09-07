from odoo import api, fields, models


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    no_recibo_interno = fields.Char(string='No. Recibo Interno')
    no_de_liquidacion = fields.Char(string='No. de Liquidación')
    deposito_bancario = fields.Char(string='Depósito Bancario')

    def _create_payment_vals_from_wizard(self):
        payment_vals = super(AccountPaymentRegister, self)._create_payment_vals_from_wizard()
        payment_vals['no_recibo_interno'] = self.no_recibo_interno
        payment_vals['no_de_liquidacion'] = self.no_de_liquidacion
        payment_vals['deposito_bancario'] = self.deposito_bancario
        return payment_vals
