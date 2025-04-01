from odoo import models, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, vals):
        phone = vals.get('phone')
        if phone:
            existing_partner = self.env['res.partner'].search([('phone', '=', phone)], limit=1)
            if existing_partner:
                vals['partner_id'] = existing_partner.id
        return super(CrmLead, self).create(vals)
