from traitlets import default
from odoo import api, models,fields
class Picking(models.Model):
  _inherit = "stock.picking"
  
  volume = fields.Float(compute="_compute_volume",default=0.00)
  
  @api.depends('move_line_ids')
  def _compute_volume(self):
    for record in self:
      self.volume = sum(record.move_line_ids.product_id.mapped('volume'))