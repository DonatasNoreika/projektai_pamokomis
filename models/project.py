from odoo import models, fields, api


class Project(models.Model):
    _name = 'projektai.project'

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date")
