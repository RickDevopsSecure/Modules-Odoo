from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    date_order = fields.Datetime(string='Order Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now)

    @api.constrains('date_order')
    def _check_date_order(self):
        for record in self:
            if record.date_order.date() < datetime.now().date():
                raise UserError("No puedes elegir una fecha anterior en la cotización.")

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    invoice_date = fields.Date(string='Invoice Date', required=True, index=True, copy=False, default=fields.Date.context_today)

    @api.constrains('invoice_date')
    def _check_invoice_date(self):
        for record in self:
            if record.invoice_date < fields.Date.today():
                raise UserError("No puedes elegir una fecha anterior en la factura.")

class Activity(models.Model):
    _inherit = 'mail.activity'

    date_deadline = fields.Date(string='Deadline', index=True, help="Deadline for the next activity of this record")

    @api.constrains('date_deadline')
    def _check_date_deadline(self):
        for record in self:
            if record.date_deadline < fields.Date.today():
                raise UserError("No puedes elegir una fecha anterior en la actividad.")

from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    date_order = fields.Datetime(string='Order Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now)

    @api.constrains('date_order')
    def _check_date_order(self):
        for record in self:
            if record.date_order.date() < datetime.now().date():
                raise UserError("No puedes elegir una fecha anterior en la cotización.")

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    invoice_date = fields.Date(string='Invoice Date', required=True, index=True, copy=False, default=fields.Date.context_today)

    @api.constrains('invoice_date')
    def _check_invoice_date(self):
        for record in self:
            if record.invoice_date < fields.Date.today():
                raise UserError("No puedes elegir una fecha anterior en la factura.")

class Activity(models.Model):
    _inherit = 'mail.activity'

    date_deadline = fields.Date(string='Deadline', index=True, help="Deadline for the next activity of this record")

    @api.constrains('date_deadline')
    def _check_date_deadline(self):
        for record in self:
            if record.date_deadline < fields.Date.today():
                raise UserError("No puedes elegir una fecha anterior en la actividad.")
