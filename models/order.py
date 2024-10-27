from odoo import fields,models, _, api
from datetime import date, datetime
from odoo.exceptions import ValidationError

class Order(models.Model):
    _name = "meal.order"
    _description = "Meal Order"

    #name, sequence, active محجوز
    #type مانو محجوز
    #name + char :  search
    #sequence + Integer: ترتيب
    #active + boolean : أرشفة
    name = fields.Char("Name",required=True, default=lambda self: _('New')) # default="New" "جديد" 
    total_price = fields.Float("Total Price", copy=False)
    order_type=fields.Selection([('internal','Internal'),('external','External')],
                                string='Type',
                                default='internal',
                                required=True)
    order_date = fields.Date("Order Date", copy=False,default=fields.datetime.now().date())
    note = fields.Text("NOTE")
    customer_id = fields.Many2one("res.partner",string="Customer")
    is_urgent = fields.Boolean("Is Urgent", copy = False)
    # Dafault value for active(or any boolean variable) in odoo is false
    # unarchive ---> active = True
    active = fields.Boolean(default=True) #? display the order : (display when filter on active is not set)
    table_number = fields.Integer("Table Number")
    expected_duration = fields.Float("Expected Duration")
    order_tag_ids=fields.Many2many("order.tag","Tags")
    item_ids = fields.One2many('order.item', 'order_id', string="Items")
    _sql_constraints=[
        ('unique_name', 'unique (name)', 'Order name already exists!'),
    ]
    #decorator
    @api.constrains('order_date') #api constrains affects only when saving (commiting) into postgres (Data Tier)
    def check_order_date(self): #object in oop, record in ORM (self) 
        for record in self:# (self either an object or a list of objects)
            if record.order_date and record.order_date > datetime.now().date():
                raise ValidationError("Order date must be in present or past")

