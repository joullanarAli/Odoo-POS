from odoo import fields,models

class Meal(models.Model):
    _name = 'order.meal'
    _description = 'Order Meal'

    name = fields.Char("Name", required=True)
    price = fields.Float("Price", copy=False)
    category_id = fields.Many2one("order.meal.category", string="Category", ondelete="restrict") # ondelete= "restrict","set_null" Default: "set_null"
    ingredient_ids = fields.One2many('meal.ingredient', 'meal_id', string="Ingredients")



class OrderMealCategory(models.Model):
    _name = "order.meal.category"
    _description = "Order Meal Category"
    _order = "name"
    # _rec_name = "test"   advantage: to display the important field (not the name of the record)
    
    name = fields.Char("Name", required=True) 

