# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import datetime
import logging

class AccountMove(models.Model):
    _inherit = "account.move"

    impuestos_globales = fields.Many2many('impuesto_global.taxes.lines', string='Impuestos Globales')

    def global_tax(self):
        for record in self:
            impuestos = self.env['impuesto_global.taxes'].search([('active', '=', True)])
            if record.move_type == 'out_invoice' or record.move_type == 'out_refund':
                impuestos = impuestos.filtered(lambda x: x.tipo == 'venta')

            for i in impuestos:
                if i.rangos:
                    for r in i.rangos_ids:
                        #if r.range_from <= record.amount_untaxed <= r.range_to:
                        if r.range_from <= record.amount_total <= r.range_to:
                            lines_dict = {
                                'move_id': record.id,
                                'impuesto': r.id,
                                'total_impuesto': record.amount_untaxed * (r.porcentaje / 100),
                                }
                            linea_impuesto = self.env['impuesto_global.taxes.lines'].create(lines_dict)
                            record.impuestos_globales = [(4, linea_impuesto.id), (4, linea_impuesto.id)]
                else:
                    lines_dict = {
                        'move_id': record.id,
                        'impuesto': i.id,
                        'total_impuesto': record.amount_untaxed * (i.porcentaje / 100),
                        }
                    linea_impuesto = self.env['impuesto_global.taxes.lines'].create(lines_dict)
                    record.impuestos_globales = [(4, linea_impuesto.id), (4, linea_impuesto.id)]    



class GlobalTaxes(models.Model):
    _name = "impuesto_global.taxes"
    _description = "Impuestos Globales"

    name = fields.Char('Nombre')
    active = fields.Boolean('Activo')
    tipo = fields.Selection([('compra', 'Compra'),('venta', 'Venta')])
    impuesto_global = fields.Boolean('Impuesto Global')
    porcentaje = fields.Float('Porcentaje')
    rangos = fields.Boolean('Rangos')
    rangos_ids = fields.One2many('impuesto_global.taxes.ranges','tax_id', string='Rangos')

class TaxesRanges(models.Model):
    _name = "impuesto_global.taxes.ranges"
    _description = "Rangos de Impuestos"

    tax_id = fields.Many2one('impuesto_global.taxes', 'Impuesto Global')
    range_from = fields.Float('Desde')
    range_to = fields.Float('Hasta')
    porcentaje = fields.Float('Porcentaje')

class GlobalTaxesLines(models.Model):
    _name = "impuesto_global.taxes.lines"
    _description = "Lineas de Impuestos Globales"

    move_id = fields.Many2one('account.move', string='Asiento')
    impuesto = fields.Many2one('impuesto_global.taxes', string='Impuesto')
    total_impuesto = fields.Float(string='Total')
    
class AccountMove(models.Model):
    _inherit = "account.move"
    
    retencion_isr = fields.Float(string='Retencion ISR', compute='_compute_retencion_isr')
    retencion_iva = fields.Float(string='Retencion IVA', compute='_compute_retencion_iva')

    @api.onchange('amount_untaxed')
    def _compute_retencion_isr(self):
        for record in self:
            impuestos = self.env['impuesto_global.taxes'].search([('active', '=', True),('name', '=', 'ISR')])

            for i in impuestos:
                if i.rangos:
                    for r in i.rangos_ids:
                        if r.range_from <= record.amount_total <= r.range_to:
                            record.retencion_isr = record.amount_untaxed_signed * (r.porcentaje / 100)
                            break
                        else:
                            record.retencion_isr = 0

    @api.onchange('amount_untaxed')
    def _compute_retencion_iva(self):
        for record in self:
            impuestos = self.env['impuesto_global.taxes'].search([('active', '=', True),('name', '=', 'IVA')])

            for i in impuestos:
                if i.rangos:
                    for r in i.rangos_ids:
                        if r.range_from <= record.amount_total <= r.range_to:
                            record.retencion_iva = record.amount_untaxed_signed * (r.porcentaje / 100)
                            break
                        else:
                            record.retencion_iva = 0                        
                else:
                    record.retencion_iva = record.amount_untaxed_signed * (i.porcentaje/100)
