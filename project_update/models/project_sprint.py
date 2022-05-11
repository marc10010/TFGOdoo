# -*- coding: utf-8 -*-

from odoo import fields, models

class ProjectSprint(models.Model):
    _name = "project.sprint"
    _description = "Sprint"
    _rec_name = "sprint_name"

    sprint_state = fields.Selection(
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
    sprint_name = fields.Char(placeholder='Name', index=True, required=True, tracking=True)

    project_id = fields.Many2one('project.project', string='Project', default=lambda self: self.env.context.get('active_id'),
        index=True, tracking=True, check_company=True, change_default=True)
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)

    fecha_inicio = fields.Date(string='Fecha Inicio', index=True, copy=False, tracking=True)
    fecha_fin = fields.Date(string='Fecha Fin', index=True, copy=False, tracking=True)
    horas_planeadas = fields.Integer(string="Horas Planeadas")
    horas_dedicadas = fields.Integer(string="Horas Dedicadas")
    horas_dedicadas_porcentage = fields.Integer(string="% Horas Dedicadas")
    desarrollo_porcentage = fields.Integer(string="% Desarrollo")
    description = fields.Text(translate=True)
    candidat_age = fields.Integer(String="age")
