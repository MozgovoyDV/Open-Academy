from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean('Instructor')
    Учитель_Уровень1  = fields.Boolean('Учитель_Уровень1')
    Учитель_Уровень2  = fields.Boolean('Учитель_Уровень2')

    session_ids = fields.Many2many('open_academy.session')