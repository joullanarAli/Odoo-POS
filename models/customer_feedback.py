from odoo import fields,models

class CustomerFeedback(models.Model):
    _name= 'customer.feedback'
    _description = 'Customer Feedback'

    meal_id = fields.Many2one('order.meal', string="Meal",required=True)
    customer_id = fields.Many2one("res.partner", string="Customer")
    star = fields.Selection([('1','1'),
                             ('2','2'),
                             ('3','3')],
                             string="Feedback", default='1'
                             )
    
    comment = fields.Char('Comment')
    state= fields.Selection([('draft','Draft'),
                             ('approve','Approve'),
                             ('reject','Reject')],
                             string="State", default='draft')