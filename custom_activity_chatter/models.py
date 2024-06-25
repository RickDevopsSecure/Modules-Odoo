from odoo import models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'mail.activity'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super(ResConfigSettings, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'form' and result.get('toolbar', False):
            for element in result['toolbar']['action']:
                if element.get('name', '') == 'action_cancel':
                    result['toolbar']['action'].remove(element)
        return result
