# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
    
class AccountMove(models.Model):
    _inherit = "account.move"
    
    retention_warning = fields.Char(string="Warning", compute='_check_retention')
    retention_amount = fields.Float(string="Retention Amount", compute='_check_retention')
    has_retention = fields.Boolean(string="Has Retention", compute='_check_retention')

    @api.depends('fiscal_position_id')
    def _check_retention(self):
        if self.fiscal_position_id:
            if self.fiscal_position_id.retention_type == 'IVA':
                self.retention_warning = 'El documento tiene retención de IVA'
                self.retention_amount = self.amount_untaxed * 0.12
                self.has_retention = True
            elif self.fiscal_position_id.retention_type == 'ISR':
                self.retention_warning = 'El documento tiene retención de ISR'
                if self.amount_untaxed >= 0.01 and self.amount_untaxed <= 30000:
                    self.retention_amount = self.amount_untaxed * 0.05
                elif self.amount_untaxed >= 30001:
                    self.retention_amount = 1500+((self.amount_untaxed-30000)*0.07)
                self.has_retention = True
            else:
                self.retention_warning = ''
                self.retention_amount = 0.0  
                self.has_retention = False  
        else:
            self.retention_warning = ''
            self.retention_amount = 0.0  
            self.has_retention = False

class AccountFiscalPosition(models.Model):
    _inherit = "account.fiscal.position"

    retention_type = fields.Selection([('IVA', 'Retencion IVA'), ('ISR', 'Retencion ISR')], string='Retention Type')

class AccountGenerateRetention(models.TransientModel):
    _name = 'account.generate.retention'
    _description = "Wizard Generate Retention"

    debit_account_id = fields.Many2one('account.account', string='Debit Account', required=False)
    credit_account_id = fields.Many2one('account.account', string='Credit Account', required=False)
    numero_retencion = fields.Char(string='Numero de Retencion', required=False)

    #Create journal entry for retention with wizard accounts
    def generate_retention(self):
        debit_account = self.env['account.move'].browse(self._context.get('active_id')).partner_id.property_account_receivable_id.id
        #credit_account = self.env['account.move'].browse(self._context.get('active_id')).partner_id.property_account_payable_id.id
        credit_account = self.env['account.account'].search([('code', '=', '1.1.03.02')], limit=1).id
        
        retention_move = self.env['account.move'].create({
            'move_type': 'entry',
            'journal_id': self.env['account.journal'].search([('type', '=', 'general')], limit=1).id,
            'date': fields.Date.today(),
            'ref':  'Retencion' + self.env['account.move'].browse(self._context.get('active_id')).name,
            #'branch_id': self.env['account.move'].browse(self._context.get('active_id')).branch_id.id,
            'line_ids': [(0, 0, {
                'name': self.env['account.move'].browse(self._context.get('active_id')).name,
                #'account_id': self.debit_account_id.id,
                'account_id': credit_account,
                'debit': self.env['account.move'].browse(self._context.get('active_id')).retention_amount,
                'credit': 0.0,
                'partner_id': self.env['account.move'].browse(self._context.get('active_id')).partner_id.id,
            }), (0, 0, {
                'name': self.env['account.move'].browse(self._context.get('active_id')).name,
                #'account_id': self.credit_account_id.id,
                'account_id': debit_account,
                'debit': 0.0,
                'credit': self.env['account.move'].browse(self._context.get('active_id')).retention_amount,
                'partner_id': self.env['account.move'].browse(self._context.get('active_id')).partner_id.id,
            })],
        })
        retention_move.action_post()
