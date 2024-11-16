from odoo import fields,models


import logging
_logger = logging.getLogger(__name__)

class FeedbackReason(models.TransientModel):
    _name='feedback.reason'
    _description='Feedback Reason'

    reason=fields.Char('Reason',required=True)

    def add_reason(self):
        _logger.info("Hello World!")