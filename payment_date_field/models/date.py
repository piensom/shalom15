# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import timedelta
from datetime import datetime

class AccountPayment(models.Model):
    _inherit = "account.payment"

    payment_date_difference = fields.Integer(string="Días hábiles de pago", compute="_compute_payment_date_difference", readonly=True, default=0)

    @api.depends('date', 'create_date')
    def _compute_payment_date_difference(self):
        for payment in self:
            fechas = []

            if payment.date and payment.create_date:
                if payment.date > payment.create_date.date():
                    if (payment.date - payment.create_date.date()).days <= 60:
                        # payment.payment_date_difference = (payment.date - payment.create_date.date()).days
                        dif = (payment.date - payment.create_date.date()).days + 1
                        for i in range(dif):
                            fechas.append(payment.create_date.date() + timedelta(days=i))
                        for fecha in fechas:
                            if fecha.weekday() != 5:
                                if fecha.weekday() != 6:
                                    payment.payment_date_difference += 1
                                    # payment.payment_date_difference -= 1
                    else:
                        payment.payment_date_difference = 0
                elif payment.date == payment.create_date.date():
                    payment.payment_date_difference = 1
                elif payment.date < payment.create_date.date():
                    payment.payment_date_difference = 0
            else:
                payment.payment_date_difference = 0

            # if payment.date:
            #     if payment.date > payment.create_date.date():
            #         if (payment.date - payment.create_date.date()).days < 60:
            #             while payment.create_date.date() != payment.date:
            #                 if payment.create_date.date().weekday() != 5 and payment.create_date.date().weekday() != 6:
            #                     dias += 1
            #                     payment.create_date += timedelta(days=1)
            #             payment.payment_date_difference = dias
            # elif payment.date == payment.create_date.date():
            #     payment.payment_date_difference = 1
            # else:
            #     payment.payment_date_difference = 0



            # if payment.date:
            #     payment.payment_date_difference = (payment.date - payment.create_date.date()).days
            # else:
            #     payment.payment_date_difference = 0

