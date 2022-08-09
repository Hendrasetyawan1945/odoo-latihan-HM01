# -*- coding: utf-8 -*-
# from odoo import http


# class Hendrakursus(http.Controller):
#     @http.route('/hendrakursus/hendrakursus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hendrakursus/hendrakursus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hendrakursus.listing', {
#             'root': '/hendrakursus/hendrakursus',
#             'objects': http.request.env['hendrakursus.hendrakursus'].search([]),
#         })

#     @http.route('/hendrakursus/hendrakursus/objects/<model("hendrakursus.hendrakursus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hendrakursus.object', {
#             'object': obj
#         })
