from odoo import api, models,fields
from odoo.tools.float_utils import float_round
class Picking(models.Model):
  _inherit = "stock.picking"
  
  volume = fields.Float(compute="_compute_volume",default=0.00)
  weight = fields.Float(compute="_compute_weight",default=0.00)
  
  @api.depends('move_line_ids',)
  def _compute_volume(self):
    for record in self:
        volume = 0.0  
        for record_line in record.move_line_ids:
            volume += record_line.product_id.volume * record_line.quantity
        record.volume = float_round(volume,precision_digits=2)  

  @api.depends('move_line_ids')
  def _compute_weight(self):
    for record in self:
        weight = 0.0  
        for record_line in record.move_line_ids:
            weight += record_line.product_id.weight * record_line.quantity
        record.weight = float_round(weight,precision_digits=2)  

