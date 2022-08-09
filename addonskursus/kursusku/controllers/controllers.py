# -*- coding: utf-8 -*-
# from odoo import http


# class Kursusku(http.Controller):
#     @http.route('/kursusku/kursusku/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kursusku/kursusku/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kursusku.listing', {
#             'root': '/kursusku/kursusku',
#             'objects': http.request.env['kursusku.kursusku'].search([]),
#         })

#     @http.route('/kursusku/kursusku/objects/<model("kursusku.kursusku"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kursusku.object', {
#             'object': obj
#         })
