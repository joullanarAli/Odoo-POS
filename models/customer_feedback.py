from odoo import fields,models

class CustomerFeedback(models.Model):
    _name= 'customer.feedback'
    _description = 'Customer Feedback'

    name=fields.Char('Name', required=True)
    meal_id = fields.Many2one('order.meal', string="Meal",required=True, copy=False)
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    rate = fields.Selection([('0','0'),
                             ('1','1'),
                             ('2','2'),
                             ('3','3')],
                             string="Rates", default='0'
                             )
    
    comment = fields.Char('Comment')
    state= fields.Selection([('new','New'),
                             ('approved','Approved'),
                             ('rejected','Rejected')],
                             string="State", default='new',readonly=True)
    
    
    def action_approve(self):
        if self.state=='new':
            self.state='approved'
    
    def action_reject(self):
        self.state='rejected'