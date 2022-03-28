# -*- coding: utf-8 -*-
# from odoo import http


# class ScrumProject(http.Controller):
#     @http.route('/scrum_project/scrum_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scrum_project/scrum_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scrum_project.listing', {
#             'root': '/scrum_project/scrum_project',
#             'objects': http.request.env['scrum_project.scrum_project'].search([]),
#         })

#     @http.route('/scrum_project/scrum_project/objects/<model("scrum_project.scrum_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scrum_project.object', {
#             'object': obj
#         })
