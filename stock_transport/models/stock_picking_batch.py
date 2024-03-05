from dateutil.relativedelta import relativedelta
from traitlets import default
from odoo import api, models,fields
from odoo.tools.float_utils import float_round
class StockPickingBatch(models.Model):
  _inherit = "stock.picking.batch"
  
  vehicle_id = fields.Many2one('fleet.vehicle')
  category_id = fields.Many2one('fleet.vehicle.model.category')
  weight = fields.Float(compute='_compute_weight', store=True,default=0.00)
  total_weight = fields.Float(store=True,default=0.00)
  total_volume = fields.Float(store=True,default=0.00)
  volume = fields.Float(compute='_compute_volume', store=True,default=0.00)
  stop_date = fields.Datetime(compute='_compute_stop_date', store=True)
  display_name = fields.Char(compute='_compute_gantt_display_name')
  no_of_transfer = fields.Integer(compute='_compute_no_of_transfer', default=0,store=True)
  no_of_lines = fields.Integer(compute='_compute_no_of_lines', default=0,store=True)
  
  @api.depends('picking_ids.weight','picking_ids','category_id')
  def _compute_weight(self):
    if len(self.category_id) >=1:
      for record in self:
        record.total_weight = sum(picking.weight for picking in record.picking_ids)
        record.weight = (sum(picking.weight for picking in record.picking_ids)/record.category_id.max_weight)
    else:
      for record in self:
        record.total_weight = 0.00
    
  @api.depends('picking_ids.volume','picking_ids','category_id')
  def _compute_volume(self):
    if len(self.category_id) >=1:
      for record in self:
        record.total_volume = sum(picking.volume for picking in record.picking_ids)
        record.volume = (sum(picking.volume for picking in record.picking_ids)/record.category_id.max_volume)
    else:
      for record in self:
        record.total_volume = 0.00
  
  @api.depends('scheduled_date')
  def _compute_stop_date(self):
    for record in self:
      if record.scheduled_date: 
          record.stop_date = record.scheduled_date + relativedelta(days=7)
      else:
          record.stop_date = False
    
  @api.depends('name')
  def _compute_gantt_display_name(self):
    for record in self:
      record.display_name = record.name+' :'+str(float_round(record.weight,precision_digits=2))+' kg, '+ str(float_round(record.volume,precision_digits=2))+' m³'
      
  @api.depends('picking_ids')
  def _compute_no_of_transfer(self):
    self.no_of_transfer = len(self.picking_ids)
    
  @api.depends('move_ids')
  def _compute_no_of_lines(self):
    self.no_of_lines = len(self.move_ids)
