# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'open_academy.course'

    name = fields.Char()
    description = fields.Text()
    responsible_id = fields.Many2one('res.users')
    session_id = fields.One2many('open_academy.session', 'course_id')

class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'open_academy.session'

    name = fields.Char()
    start_date = fields.Date(default=fields.Date.today())
    duration = fields.Integer()
    seats = fields.Integer()
    active = fields.Boolean(default=True)
    instructor_id = fields.Many2one('res.partner', domain="[('instructor', '=', True)]")
    course_id = fields.Many2one('open_academy.course')
    attendee_ids=fields.Many2many('res.partner')
    attendee_count=fields.Integer(compute='get_attendee_count', store='True')
    taken_seats = fields.Float(compute='_taken_seats')
    date_end = fields.Date()
    color = fields.Integer()

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0
            else:
                r.taken_seats = 100 * len(r.attendee_ids) / r.seats

    @api.depends('attendee_ids')
    def get_attendee_count(self):
        for r in self:
            r.attendee_count = len(r.attendee_ids)

    @api.onchange('seats', 'attendee_ids')
    def _verity_valid_seats(self):
        if self.seats<0:
            return {
            'warning': {
                'title': "Некоректно заполненно значение Количество мест",
                'message': "Данное значение не может быть отрицательным",
            }
        }
        if self.seats < len(self.attendee_ids):
            return {
            'warning': {
                'title': "Ошибка",
                'message': "Количество мест меньше кол-ва присутвующих",
            }
        }

    @api.constrains('instructor_id','attendee_ids')
    def _check_something(self):
        for record in self:
            if record.instructor_id and record.instructor_id in record.attendee_ids:
                raise ValidationError("Инструктор не может быть среди присутвующих")

    def action_fill_attendee(self, attendee_ids):
        self.attendee_ids = attendee_ids


