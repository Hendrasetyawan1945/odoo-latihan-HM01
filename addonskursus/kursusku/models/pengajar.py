from odoo import fields, models, api


class pengajar(models.Model):
    _name = 'pengajarku.pengajar'
    _description = 'Pengajar ku'

    name = fields.Selection(string='Penajar di Kursusku',
                            selection=[('dwi artanto','Dwi artanto'),('icikiwir','Icikiwir'),('sucipto','sucipto','Sucipto')],
                            required=True)
    alamat = fields.Char(string='Alamat',required=True)