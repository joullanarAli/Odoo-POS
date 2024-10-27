from odoo import fields,models

class MealIngredient(models.Model):
    _name="meal.ingredient"
    _description="Meal Ingredient"

    meal_id = fields.Many2one('order.meal', string="Meal", copy = False)
    product_id = fields.Many2one('product.product', string="Product")
    name = fields.Char("Name", required=True)
    quantity = fields.Float("Quantity")
