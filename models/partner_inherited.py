from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    project_ids = fields.One2many('projektai.project', 'client_id', string="Projects", readonly=True)
