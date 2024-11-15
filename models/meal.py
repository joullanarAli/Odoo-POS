from odoo import fields,models

class Meal(models.Model):
    _name = 'order.meal'
    _description = 'Order Meal'

    name = fields.Char("Name", required=True)
    price = fields.Float("Price", copy=False)
    category_id = fields.Many2one("order.meal.category", string="Category", ondelete="restrict") # ondelete= "restrict","set_null" Default: "set_null"
    ingredient_ids = fields.One2many('meal.ingredient', 'meal_id', string="Ingredients")
    feedback_ids=fields.One2many('customer.feedback','meal_id',string="Feedbacks")

    def action_view_meal_feedback(self):
        # select --> search
        # *  --> ----
        # from -->self.env['Model-Name']
        # where  --> domain
        #feedback_ids=self.env['customer.feedback'].search([('meal_id', '=', self.id)]) #list of objects
        return {
            'type':'ir.actions.act_window',
            'name':'Feedback',
            'view_mode':'tree',
            'res_model':'customer.feedback',
            'target':'current',
            'domain':[('id','in',self.feedback_ids.ids)],
            'context':{ #to not edit the meal feedback in another meal feedback
                'default_meal_id':self.id
            }
            
        }

class OrderMealCategory(models.Model):
    _name = "order.meal.category"
    _description = "Order Meal Category"
    _order = "name"
    # _rec_name = "test"   advantage: to display the important field (not the name of the record)
    
    name = fields.Char("Name", required=True) 

