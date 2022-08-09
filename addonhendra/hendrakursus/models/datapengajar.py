from odoo import fields, models, api


class datapengajar(models.Model):
    _name = 'pengajarku.pengajar'
    _description = 'pengajarKU'

    name = fields.Selection(
        string='Nama',
        selection=[('sucipto','Sucipto'),('icikiwir','Icikiwir'),('dudul','Dudul'),('abduldul','Abduldul')],
        required=False)
    
    alamat = fields.Char(
        string='Alamat',
        required=False)
