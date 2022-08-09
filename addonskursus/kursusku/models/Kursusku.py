from odoo import fields, models, api


class Kursusku(models.Model):
    _name = 'kursusku.kategorikursus'
    _description = 'Kategori Kursusku'

    name = fields.Char(string="Kategori kursus")
