# -*- coding: utf-8 -*-

from odoo import models, fields


class scrum_project(models.Model):
    _inherit = "project.task"

#     _name = 'scrum_project.scrum_project'
#     _description = 'scrum_project.scrum_project'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
#