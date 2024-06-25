from odoo import models, api, _
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def create(self, vals):
        res = super(SaleOrderLine, self).create(vals)
        for rec in res:
            if rec.product_id.qty_available <= 0:
                raise UserError(
                    _("Planeas vender'{}' unidades de este producto {} actualmente no tienes stock {} en el almacen de tu empresa, contacta para reabastecer el producto lo mas rapido posible.".format(
                        rec.product_uom_qty, rec.product_id.qty_available, rec.product_id.name)))
            return res
        
    def write(self, vals):
        for rec in self:
            res = super(SaleOrderLine, self).write(vals)
            if rec.product_id.qty_available <= 0:
                raise UserError(
                    _("Planeas vender'{}' unidades de este producto {} actualmente no tienes stock {} en el almacen de tu empresa, contacta para reabastecer el producto lo mas rapido posible.".format(
                        rec.product_uom_qty, rec.product_id.name, rec.product_id.qty_available)))
            return res
