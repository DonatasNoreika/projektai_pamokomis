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

    status = fields.Selection([
        ('draft', "Draft"),
        ('started', "Started"),
        ('done', "Done"),
        ('cancelled', "Cancelled"),
    ], string="Progress", default='draft', translate=True)

    image = fields.Binary("Image", attachment=True)
    document_ids = fields.One2many('projektai.document', 'project_id', string='Documents')

    @api.depends('employees_ids')
    def _get_employees_percentage(self):
        total_sum = self.env['hr.employee'].search_count([])
        for r in self:
            r.employees_percentage = (len(r.employees_ids) / total_sum) * 100.0

    @api.depends('employees_ids.name')
    def _get_employees_count(self):
        for r in self:
            r.employees_count = len(r.employees_ids)

    def send_project_report(self):
        # Find the e-mail template
        template = self.env.ref('projektai.project_info_mail_template')
        # You can also find the e-mail template like this:
        # template = self.env['ir.model.data'].get_object('send_mail_template_demo', 'example_email_template')

        # Send out the e-mail template to the user
        self.env['mail.template'].browse(template.id).send_mail(self.id)

class ProjectDocument(models.Model):
    _name = 'projektai.document'

    name = fields.Char(string='Filename')
    file = fields.Binary(string='File', attachment=True)
    comment = fields.Text(string='Notes')

    project_id = fields.Many2one('openacademy.session')
