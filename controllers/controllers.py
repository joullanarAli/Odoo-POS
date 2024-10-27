# -*- coding: utf-8 -*-
# from odoo import http


# class TechOrder1(http.Controller):
#     @http.route('/tech_order1/tech_order1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_order1/tech_order1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_order1.listing', {
#             'root': '/tech_order1/tech_order1',
#             'objects': http.request.env['tech_order1.tech_order1'].search([]),
#         })

#     @http.route('/tech_order1/tech_order1/objects/<model("tech_order1.tech_order1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_order1.object', {
#             'object': obj
#         })

