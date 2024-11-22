from odoo import fields,models


import logging
_logger = logging.getLogger(__name__)
#wizards are stored temporarely in the database
class FeedbackReason(models.TransientModel):
    _name='feedback.reason'
    _description='Feedback Reason'

    reason=fields.Char('Reason',required=True)

    def add_reason(self):
        #feedback = self.env['customer.feedback'].search([('id','=',self.env.context.get('active_id'))]) returns object or List of objects
        feedback = self.env['customer.feedback'].browse(self.env.context.get('active_id')) #returns object or List of objects
        #feedback.reason = self.reason
        #feedback.state = 'rejected'
        feedback.update({'reason':self.reason, 'state':'rejected'})