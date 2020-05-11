# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'projektai.wizard'
    _description = "Wizard: Quick Registration of Employees to Projects"

    project_ids = fields.Many2many('projektai.project', string="Project")
    employees_ids = fields.Many2many('hr.employee', string="Employees")

    def add(self):
        for project in self.project_ids:
            project.employees_ids |= self.employees_ids
        return {}