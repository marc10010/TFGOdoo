# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ProjectSprint(models.Model):
    _name = "project.sprint"
    _description = "Sprint"
    _rec_name = "sprint_name"

    sprint_state = fields.Selection(
        [('standBy', 'Stand By'),
        ('inProgress', 'In Progress'),
        ('done', 'Done')],
        string= "Estado")


    active = fields.Boolean(default = True)

    kanban_state = fields.Selection([
        ('normal', 'Grey'),
        ('done', 'Green'),
        ('blocked', 'Red')], string='Kanban State',
        copy=False, default='normal', required=True)

    sprint_name = fields.Char(placeholder='Name', index=True, required=True, tracking=True)


    project_id = fields.Many2one('project.project', string='Project', default=lambda self: self.env.context.get('active_id'),
        index=True, tracking=True, check_company=True, change_default=True, readonly=True)

    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)

    fecha_inicio = fields.Date(string='Fecha Inicio', index=True, copy=False, tracking=True)
    fecha_fin = fields.Date(string='Fecha Fin', index=True, copy=False, tracking=True)
    horas_planeadas = fields.Float(string="Horas Planeadas", compute ='_compute_planned_hours_count')
    horas_dedicadas = fields.Float(string="Horas Dedicadas", compute ='_compute_completed_hours_count')
    horas_dedicadas_porcentage = fields.Float(string="% Horas Dedicadas", compute = '_compute_progress_hours')
    desarrollo_porcentage = fields.Float(string="% Desarrollo")
    description = fields.Text(translate=True)
    candidat_age = fields.Integer(String="age")

    stage_id = fields.Many2one('crm.stage', string='Stage', ondelete='restrict', tracking=True, index=True, copy=False)
    task_count = fields.Integer(compute='_compute_task_count', string="Task Count")
    task_ids = fields.One2many('project.task', 'sprint', string="tasks", context={'active_test': False})

    def tareas_sprint(self):
        new_context = dict(self.env.context).copy()
        new_context.update( { 'sprint_name' : self.id } )
        ctx = dict(new_context or {})
        action ={
            'type': 'ir.actions.act_window',
            'domain': [ '&',('project_id', 'in', self.project_id.ids), '|', ('sprint', 'in', self.sprint_name),'&', ('stage_id', 'in', self.env.ref('project_update.type_backlog').ids), '|', ('sprint', 'in', self.sprint_name),('sprint', '=',False) ],
            #'views': [(view_kanban_id, 'kanban')],
            'view_mode': 'kanban,form,list',
            'name': 'Tareas',
            'res_model': 'project.task',
            'context': ctx
        }
        return action

    def _compute_task_count(self):
        task_data = self.env['project.task'].read_group(['&', ('project_id', '=', self.project_id.id), ('sprint', 'in', self.project_id.tasks.sprint.ids)], ['sprint'], ['sprint'])
        result = dict((data['sprint'][1], data['sprint_count']) for data in task_data)
        for project in self:
            project.task_count = result.get(project.sprint_name, 0)

    def _compute_planned_hours_count(self):
        for task in self:
            task.horas_planeadas = sum(task.task_ids.mapped('planned_hours'))

    def _compute_completed_hours_count(self):
        for task in self:
            task.horas_dedicadas = sum(task.task_ids.mapped('effective_hours'))

    def _compute_progress_hours(self):
        self.horas_dedicadas_porcentage = (self.horas_dedicadas / self.horas_planeadas)*100



    def gantt_sprint(self):
        new_context = dict(self.env.context).copy()
        new_context.update( { 'sprint_name' : self.id } )
        ctx = dict(new_context or {})
        action ={
            'type': 'ir.actions.act_window',
            'domain': [ '&',('project_id', 'in', self.project_id.ids), '|', ('sprint', 'in', self.sprint_name),'&', ('stage_id', 'in', self.env.ref('project_update.type_backlog').ids), '|', ('sprint', 'in', self.sprint_name),('sprint', '=',False) ],
            #'views': [(view_kanban_id, 'kanban')],
            'view_mode': 'kanban,form,list',
            'name': 'Tareas',
            'res_model': 'project.task',
            'context': ctx
        }
        return action

    def burn_down_chart_sprint(self):
        return self

    def read_all_stage_ids(self, stages, domain, order):
        project_id = self._context.get('default_project_id')

        search_domain = [('project_id', '=', project_id)]

        # perform search
        stage_ids = stages._search(search_domain)
        return stages.browse(stage_ids)
