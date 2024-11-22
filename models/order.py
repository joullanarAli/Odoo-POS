from odoo import fields,models, _, api
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class Order(models.Model):
    _name = "meal.order"
    _description = "Meal Order"

    #name, sequence, active, state محجوز
    #type مانو محجوز
    #name + char :  search
    #sequence + Integer: ترتيب
    #active + boolean : أرشفة
    #state + selection
    name = fields.Char("Name",required=True, default=lambda self: _('New')) # default="New" "جديد" 
    #default: read only = false, when compute: read only = true 
    #default: store = true, when compute: store = false
    #default: copy = true, when compute: copy = false
    #(default: required = false, when compute: required = false )+ translate + ondelete 
    total_price = fields.Float("Total Price", compute="_compute_total_price", store=True, readonly=True)#store = true --> readonly=false 
    order_type=fields.Selection([('internal','Internal'),('external','External')],
                                string='Type',
                                default='internal',
                                required=True)  #key is unique, technically, changing it will cause problems
    order_date = fields.Date("Order Date", copy=False,default=fields.datetime.now().date())
    note = fields.Text("NOTE")
    customer_id = fields.Many2one("res.partner",string="Customer")
    is_urgent = fields.Boolean("Is Urgent", copy = False)
    # Dafault value for active(or any boolean variable) in odoo is false
    # unarchive ---> active = True
    active = fields.Boolean(default=True) #? display the order : (display when filter on active is not set)
    table_number = fields.Integer("Table Number")
    expected_duration = fields.Float("Expected Duration")
    expected_date = fields.Datetime("Expected Date", compute='_compute_expected_date',inverse='_inverse_expected_date', readonly=False)
    order_tag_ids=fields.Many2many("order.tag","Tags")
    item_ids = fields.One2many('order.item', 'order_id', string="Items")
    state = fields.Selection([('draft','Draft'),
                              ('confirmed','Confirmed'),
                              ('in_process','In process'),
                              ('delivered','Delivered'),
                              ('cancelled','Cancelled')],
                              string = "State", default='draft') #the order of selection tuples is important (for presenting)
    external_item_ids = fields.Many2many('external.item',"External_Item", readonly=True)

    _sql_constraints=[
        ('unique_name', 'unique (name)', 'Order name already exists!'),
    ]
    #decorator
    @api.constrains('order_date') #api constrains affects only when saving (commiting) into postgres (Data Tier)
    def check_order_date(self): #object in oop, record in ORM (self) 
        for record in self:# (self either an object or a list of objects)
            if record.order_date and record.order_date > datetime.now().date():
                raise ValidationError("Order date must be in present or past")

    @api.depends('item_ids','item_ids.total_price') #item_ids if I add item or delete item and the total_price of it
    def _compute_total_price(self):
        for record in self: # it's necessary to go into every record in computed method
            total_price = 0
            for item in record.item_ids: #item_ids is iterable
                total_price += item.total_price
            record.total_price= total_price
        # we can use the map and sum to reduce the complexity

    @api.depends('order_date','expected_duration')
    def _compute_expected_date(self):
        for record in self:
            record.expected_date =record.order_date + timedelta(
                days=record.expected_duration)

    
    def _inverse_expected_date(self):
        for record in self:
            record.expected_duration = (record.expected_date.date() - record.order_date).days
    #on change is working only on api not if I change in the code
    def action_confirm(self):
        self.state='confirmed'
        self.order_date=datetime.now().date()

    def action_in_process(self):
        self.state='in_process'
    
    def action_delivered(self):
        self.state='delivered'

    def action_cancelled(self):
        self.state='cancelled'
    
    def check_urgent_order(self):
        for record in self:
            expected = record.expected_date - timedelta(days=1)
            if expected.date() == datetime.now().date() :
                record.is_urgent = True

