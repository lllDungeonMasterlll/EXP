from odoo import models, api, _
from odoo.exceptions import UserError

class PartnerArchive(models.Model):
    _inherit = 'res.partner'

    @api.model
    def archive_partner(self):
        for partner in self:
            # Перевірка на угоди
            linked_deals = self.env['sale.order'].search([('partner_id', '=', partner.id)])
            if linked_deals:
                raise UserError(
                    _("Cannot archive partner %s because it has related deals.") % partner.name
                )
            # Якщо угод немає, виконуємо стандартне архівування
            return super(PartnerArchive, self).archive_partner()
