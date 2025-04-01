from odoo import models, fields

class DuplicateArchiveLog(models.Model):
    _name = 'duplicate.archive.log'
    _description = 'Log of Archived Duplicate Partners'

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    archived = fields.Boolean(string='Archived', default=True)
    archive_date = fields.Datetime(string='Archive Date', default=fields.Datetime.now)
