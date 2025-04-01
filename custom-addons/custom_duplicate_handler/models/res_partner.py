
from odoo import models, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def archive_duplicates(self):
        logs = []
        partners_by_phone = self.read_group([('phone', '!=', False)], ['phone'], ['phone'])
        for group in partners_by_phone:
            phone = group['phone']
            duplicates = self.search([('phone', '=', phone)])
            if len(duplicates) > 1:
                # Сортуємо дублікатів за кількістю пов'язаних записів
                sorted_duplicates = sorted(duplicates, key=lambda p: p.linked_records())
                for partner in sorted_duplicates[1:]:
                    partner.active = False
                    logs.append({
                        'partner_id': partner.id,
                        'archived': True,
                    })
        self.env['duplicate.archive.log'].create(logs)

    def linked_records(self):
        return self.env['crm.lead'].search_count([('partner_id', '=', self.id)])
    
class ResPartner(models.Model):
    _inherit = 'res.partner'

    def archive_partner(self):
        for partner in self:
            # Перевіряємо, чи є у партнера угоди
            linked_deals = self.env['sale.order'].search([('partner_id', '=', partner.id)])
            if linked_deals:
                raise UserError(
                    _("Cannot archive partner %s because it has related deals.") % partner.name
                )
            # Виконуємо стандартне архівування
            super(ResPartner, partner).archive_partner()
