# -*- coding: utf-8 -*-

from odoo import fields, models

class TaskTemplate(models.Model):
    _inherit = 'project.task'
    sprint = fields.Many2one('project.sprint', string='Sprint', default=lambda self: self.env.context.get('active_id'),
                             index=True, tracking=True, check_company=True, change_default=True)
    prioridad = fields.Integer(string="Prioridad",min=0, max= 10)
    dependencia = fields.Many2one('project.task', string='Dependencias', default=lambda self: self.env.context.get('active_id'),
                                  index=True, tracking=True, check_company=True, change_default=True)
"""
    def sprint_action(self):
        view_kanban_id = self.env.ref('project_update.sprint_kanban').id
        """"""ctx opcional""""""
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
"""