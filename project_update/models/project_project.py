# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ProjectTemplate(models.Model):
    _inherit = 'project.project'
    backup = fields.Many2one('res.users', string='Backup', default=lambda self: self.env.user, tracking=True)
    responsable_tecnico = fields.Many2one('res.users', string='Responsable técnico', default=lambda self: self.env.user, tracking=True)
    sprint_count = fields.Integer(string="Sprint Count")

    def sprint_action(self):
        view_kanban_id = self.env.ref('project_update.sprint_kanban').id
        """ctx opcional"""
        ctx = dict(self.env.context or {})
        action = {
            'type': 'ir.actions.act_window',
            'domain': [('project_id', 'in', self.ids)],
            #'views': [(view_kanban_id, 'kanban')],
            'view_mode': 'kanban,form',
            'name': 'Sprints',
            'res_model': 'project.sprint',
            'context': ctx
        }
        return action

    @api.model
    def create(self, vals):
        project = super(ProjectTemplate, self).create(vals)

        project.type_ids = [(4, self.env.ref('project_update.type_backlog').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_inprogres').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_validationpm').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_develop').id)]

#        if etapas:
#            for etapa in etapas:
#                project.type_ids = [(4, etapa.id)]
        return project