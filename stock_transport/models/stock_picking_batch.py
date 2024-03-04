from traitlets import default
from odoo import api, models,fields
class StockPickingBatch(models.Model):
  _inherit = "stock.picking.batch"
  
  vehicle_id = fields.Many2one('fleet.vehicle')
  category_id = fields.Many2one('fleet.vehicle.model.category')
  weight = fields.Float(compute='_compute_weight',default=500 , store=True)
  volume = fields.Float(compute='_compute_volume',default=500, store=True)
  
  @api.depends('picking_ids')
  def _compute_weight(self):
    total_weight=0.0
    
    for record in self.picking_ids.move_line_ids:
      total_weight = (total_weight + (record.product_id.weight * record.quantity))
    print(self.weight)
    # self.weight = total_weight
    # self.weight = total_weight/self.category_id.max_weight
    
  @api.depends('picking_ids')
  def _compute_volume(self):
    total_volume=0.0
    
    for record in self.picking_ids.move_line_ids:
      total_volume = (total_volume + (record.product_id.volume * record.quantity))
    print(self.volume)
    # self.volume = total_volume
    # self.volume = total_volume/self.category_id.max_volume
    