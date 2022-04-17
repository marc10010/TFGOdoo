# -*- coding: utf-8 -*-

from odoo import models, fields


class ProjectTemplate(models.Model):
    _inherit = 'project.project'
    backup = fields.Many2one('res.users', string='Backup', default=lambda self: self.env.user, tracking=True)
    responsableTecnico = fields.Many2one('res.users', string='Responsable técnico', default=lambda self: self.env.user, tracking=True)
    sprint_count = fields.Integer(string="Task Count")
