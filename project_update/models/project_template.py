# -*- coding: utf-8 -*-


from odoo import fields, models


class ProjectTemplate(models.Model):
    _inherit = 'project.project'
    backup = fields.Many2one('res.users', string='Backup', default=lambda self: self.env.user, tracking=True)
    responsableTecnico = fields.Many2one('res.users', string='Responsable técnico', default=lambda self: self.env.user, tracking=True)
    sprint_count = fields.Integer(string="Sprint Count")

    def sprintAction(self):
        view_kanban_id = self.env.ref('project_update.view_sprint_form2').id
        """ctx opcional"""
        ctx = dict(self.env.context or {})
        action = {
            'type': 'ir.actions.act_window',
            #'domain': [('projectId', 'in', self.ids)],
            'views': [(view_kanban_id, 'form')],
            'view_mode': 'form',
            'name': 'Sprints',
            'res_model': 'project.sprint',
            'context': ctx
        }
        return action


class ProjectSprint(models.Model):
    _name = "project.sprint"
    _description = "Sprint"
    _rec_name = "sprintName"

    projectId = fields.Many2one('project.project', string= "Project")
    sprintState = fields.Selection(
        [('standBy', 'Stand By'),
        ('inProgress', 'In Progress'),
        ('done', 'Done')],
        string= "Estado")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Important'),
    ], default='0', index=True, string="Priority")

    active = fields.Boolean(default = True)

    kanban_state = fields.Selection([
        ('normal', 'Grey'),
        ('done', 'Green'),
        ('blocked', 'Red')], string='Kanban State',
        copy=False, default='normal', required=True)
    sprintName = fields.Char('Name', index=True, required=True, tracking=True)
    userId = fields.Many2one('res.users', string='Project Manager', default=lambda self: self.env.user, tracking=True)
    project_id = fields.Many2one('project.project', string='Project', default=lambda self: self.env.context.get('default_project_id'),
        index=True, tracking=True, check_company=True, change_default=True)
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)

    backup = fields.Many2one('res.users', string='Backup', default=lambda self: self.env.user, tracking=True)
    responsableTecnico = fields.Many2one('res.users', string='Responsable técnico', default=lambda self: self.env.user, tracking=True)



    candidat_age = fields.Integer(String=" age")

