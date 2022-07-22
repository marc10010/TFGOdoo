
from odoo import api, fields, models

class TaskTemplate(models.Model):
    _name = "project.sprint.stage"
    _order = 'sequence,id'
    _description = 'Etapa del sprint'

    sequence = fields.Integer(string='Sequence', default=1)
    name = fields.Char(string="Nombre de la Etapa")
