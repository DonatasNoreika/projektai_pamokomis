from odoo import models, fields, api


class Invoice(models.Model):
    _name = 'projektai.invoice'

    number = fields.Char(string="Number", required=True)
    date = fields.Date(string="Start Date", default=fields.Date.today)
    project_id = fields.Many2one('projektai.project')

    line_ids = fields.One2many('projektai.invoiceline', 'invoice_id', string="Lines")

    total = fields.Float("Total", compute='_get_total', store=True)

    status = fields.Selection([
        ('draft', "Draft"),
        ('started', "Started"),
        ('done', "Done"),
        ('cancelled', "Cancelled"),
    ], string="Progress", default='draft', translate=True)

    @api.depends('line_ids.suma')
    def _get_total(self):
        total = 0
        for record in self:
            for line in record.line_ids:
               total += line.suma
            record.total = total



class InvoiceLine(models.Model):
    _name = 'projektai.invoiceline'

    work_id = fields.Many2one('projektai.work')
    suma = fields.Float("Sum")
    invoice_id = fields.Many2one('projektai.invoice')

