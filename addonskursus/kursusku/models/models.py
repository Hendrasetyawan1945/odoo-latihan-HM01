# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class kursusku(models.Model):
#     _name = 'kursusku.kursusku'
#     _description = 'kursusku.kursusku'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
