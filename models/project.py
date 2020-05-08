from odoo import models, fields, api


class Project(models.Model):
    _name = 'projektai.project'

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date")

    client_id = fields.Many2one('res.partner', string="Client")
    manager = fields.Many2one('hr.employee', string="Manager", domain=[('manager', '=', True)])
    color = fields.Integer()

    employees_ids = fields.Many2many('hr.employee', string="Employees")
    work_ids = fields.One2many('projektai.work', 'project_id', string="Works")
    invoice_ids = fields.One2many('projektai.invoice', 'project_id', string="Invoices")

    employees_percentage = fields.Float('Employees percentage', compute='_get_employees_percentage')
    employees_count = fields.Integer(
        string="Employees count", compute='_get_employees_count', store=True)

    @api.depends('employees_ids')
    def _get_employees_percentage(self):
        total_sum = self.env['hr.employee'].search_count([])
        for r in self:
            r.employees_percentage = (len(r.employees_ids) / total_sum) * 100.0

    @api.depends('employees_ids.name')
    def _get_employees_count(self):
        for r in self:
            r.employees_count = len(r.employees_ids)
