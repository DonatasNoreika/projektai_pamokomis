from odoo import models, fields, api


class Invoice(models.Model):
    _name = 'projektai.invoice'

    number = fields.Char(string="Number", required=True)
    date = fields.Date(string="Start Date", default=fields.Date.today)
    project_id = fields.Many2one('projektai.project')

    line_ids = fields.One2many('projektai.invoiceline', 'invoice_id', string="Lines")


class InvoiceLine(models.Model):
    _name = 'projektai.invoiceline'

    work_id = fields.Many2one('projektai.work')
    suma = fields.Float("Sum")
    invoice_id = fields.Many2one('projektai.invoice')

