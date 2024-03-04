from traitlets import default
from odoo import api, models,fields
class FleetVehicleModelCategory(models.Model):
  _inherit = "fleet.vehicle.model.category"
  
  max_weight = fields.Float("Max Weight (kg)",default=500)
  max_volume = fields.Float("Max Volume (m³)",default=700)
  
  @api.depends('name')
  def _compute_display_name(self):
    for record in self:
      record.display_name = record.name+' ('+str(record.max_weight)+' kg, '+ str(record.max_volume)+' m³)'