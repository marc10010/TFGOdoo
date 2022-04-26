# -*- coding: utf-8 -*-

from odoo import models, fields


class ProjectTemplate(models.Model):
    _inherit = 'project.project'
    backup = fields.Many2one('res.users', string='Backup', default=lambda self: self.env.user, tracking=True)
    responsableTecnico = fields.Many2one('res.users', string='Responsable técnico', default=lambda self: self.env.user, tracking=True)
    sprint_count = fields.Integer(string="Sprint Count")

    def sprintAction(self):
        return {
            'warning': {
                'title': 'Warning!',
                'message': 'The warning text'
            }
        }


class ProjectSprint(models.Model):
    _name = "project.sprint"
    _description = "Sprint"
    _rec_name = "candidat_name"

    candidat_name = fields.Char(string='Name', required=True,  track_visibility="always")
    image = fields.Binary(String="Image", attachment=True)
    candidat_age = fields.Integer(String=" age")

    def open_sprints(self):
        ctx = dict(self._context)
        ctx.update({'search_default_project_id': self.id, 'default_project_id': self.id})
        action = self.env['ir.actions.act_window'].for_xml_id('project', 'act_project_project_2_project_task_all')
        return dict(action, context=ctx)

