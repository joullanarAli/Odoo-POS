from odoo import models,fields

import logging
_logger = logging.getLogger(__name__)
class ExternalItemWizard(models.TransientModel):
    _name='external.item.wizard'
    _description = 'External Item Wizard'

    _transient_max_count = 3 # save just 3 records
    _transient_max_hours = 3 #save the records for 3 hours only
    
    def set_default_item(self): #this default method must be defined before the field and mus return a value and this value should have the type of the field
        items = self.env['external.item'].search([])
        return items

    external_item_ids=fields.Many2many('external.item','External_Items',default =set_default_item)

    def add_external_item(self):
        
        order_id = self.env['meal.order'].browse(self.env.context.get('active_id'))
        order_id.update({'external_item_ids':[(4,item.id) for item in self.external_item_ids]})
        # order_id.update({'external_item_ids':self.external_item_ids.ids})
        # order_id.external_item_ids = self.external_item_ids
