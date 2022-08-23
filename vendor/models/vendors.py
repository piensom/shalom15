from odoo import fields, models

class VendorModel(models.Model):
    _name = "vendor.model"

    name = fields.Char(string='Nombre', required=True)
    emergency_contact = fields.Char(string='Contacto de Emergencia')
    pho = fields.Char(string='Telefono')
    bd_day = fields.Date(string='Cumpleaños')

