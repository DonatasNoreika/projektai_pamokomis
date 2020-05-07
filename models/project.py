from odoo import models, fields, api


class Project(models.Model):
    _name = 'projektai.project'

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date")

    client_id = fields.Many2one('res.partner', string="Client")
    manager = fields.Many2one('hr.employee', string="Manager", domain=[('manager', '=', True)])

    employees_ids = fields.Many2many('hr.employee', string="Employees")
    work_ids = fields.One2many('projektai.work', 'project_id', string="Works")
    invoice_ids = fields.One2many('projektai.invoice', 'project_id', string="Invoices")