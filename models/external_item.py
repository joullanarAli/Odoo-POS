from odoo import fields,models

class ExternalItem(models.Model):
    _name = "external.item"
    _description = "External Item"
    _rec_name = "product_id"

    product_id = fields.Many2one('product.product',string="Product")