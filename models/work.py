from odoo import models, fields, api


class Work(models.Model):
    _name = 'projektai.work'

    name = fields.Char(string="Name", required=True)
    project_id = fields.Many2one('projektai.project')
