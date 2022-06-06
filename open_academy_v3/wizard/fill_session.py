from odoo import models, fields, api


class FillSession(models.TransientModel):
    _name = 'openacademy.session.fill'
    _description = 'Session fill wizard'
    session_ids = fields.Many2many(comodel_name="open_academy.session", string="Session", )
    attendee_ids = fields.Many2many(comodel_name="res.partner", string="Attendees")

    @api.model
    def default_get(self, _fields):
        """ Use active_ids from the context to fetch the leads/opps to merge.
            In order to get merged, these leads/opps can't be in 'Dead' or 'Closed'
        """
        result = super(FillSession, self).default_get(_fields)
        result['session_ids'] = self.env['open_academy.session'].browse(self._context.get('active_id'))
        return result

    def action_fill_attendees(self):
        return self.session_ids.action_fill_attendee(attendee_ids=self.attendee_ids)