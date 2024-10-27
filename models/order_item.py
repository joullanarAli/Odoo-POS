from odoo import fields,models, api
from odoo.exceptions import ValidationError
class OrderItem(models.Model):
    _name = 'order.item'
    _description = 'Order Item'
    _rec_name = 'meal_id'

    order_id = fields.Many2one('meal.order', string ="Order", readonly=True, copy = False)
    meal_id = fields.Many2one ('order.meal', string ="Meal", copy=False)
    quantity = fields.Float("Quantity")
    price = fields.Float("Price")
    total_price = fields.Float("Total Price")


    @api.onchange('meal_id')
    def set_price(self):
        for record in self:
            if record.meal_id:
                record.price = record.meal_id.price

    @api.onchange('price','quantity')
    def calculate_total_price(self):
        for record in self:
            if record.quantity and record.price:
                record.total_price = record.quantity * record.price

    @api.constrains('price')
    def check_price_value(self):
        if self.price and self.price<=0:
            raise ValidationError('Price must be bigger than zero')