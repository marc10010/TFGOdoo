# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ProjectTemplate(models.Model):
    _inherit = 'project.project'
    backup = fields.Many2one('res.users', string='Backup', default=lambda self: self.env.user, tracking=True)
    responsable_tecnico = fields.Many2one('res.users', string='Responsable técnico', default=lambda self: self.env.user, tracking=True)
    sprint_id = fields.One2many('project.sprint', 'sprint_name')
    sprint_count = fields.Integer(compute= '_compute_sprint_count', String="Sprints")

    sprint_type_ids = fields.Many2many('project.sprint.type', 'project_sprint_type_rel', 'project_id', 'type_id', string='Sprint Stages')

    def sprint_action(self):
        view_kanban_id = self.env.ref('project_update.sprint_kanban').id
        """ctx opcional"""
        ctx = dict(self.env.context or {})
        ctx['search_default_project_id'] = self.id
        ctx['default_project_id'] = self.id
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

        ### type_ids = fields.Many2many('project.task.type', 'project_task_type_rel', 'project_id', 'type_id', string='Tasks Stages')
        project.type_ids = [(4, self.env.ref('project_update.type_backlog').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_backlog_sprint').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_client').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_planning').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_develop').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_validationpm').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_validationclient').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_completed').id)]
        project.type_ids = [(4, self.env.ref('project_update.type_inprod').id)]

        ## sprint_type_ids = fields.Many2many('project.sprint.type', 'project_sprint_type_rel', 'project_id', 'type_id', string='Sprint Stages')
        project.sprint_type_ids = [(4, self.env.ref('project_update.type_backlog_1').id)]



        return project


    def _compute_sprint_count(self):
        task_data = self.env['project.sprint'].read_group([ ('project_id', 'in', self.ids)], ['project_id'], ['project_id'])
        result = dict((data['project_id'][0], data['project_id_count']) for data in task_data)
        for project in self:
            project.sprint_count = result.get(project.id, 0)
