# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'open_academy.course'

    name = fields.Char()
    description = fields.Text()
    responsible_id = fields.Many2one('res.users')
    session_id = fields.One2many('open_academy.session', 'course_id')


