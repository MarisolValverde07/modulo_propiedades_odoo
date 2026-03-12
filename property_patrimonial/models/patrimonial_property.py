from odoo import models, fields

class PatrimonialProperty(models.Model):
    _name = 'patrimonial.property'
    _description = 'Propiedad Patrimonial'

    expediente = fields.Char(string="Expediente", required=True)
    tipo = fields.Selection([
        ('zona_verde', 'Zona Verde'),
        ('inmueble_patrimonial', 'Inmueble Patrimonial')
    ], string="Tipo", required=True)

    distrito = fields.Char(string="Distrito")
    descripcion = fields.Text(string="Descripción")

    #Relación con mantenimientos
    maintenance_ids = fields.One2many(
        'property.maintenance',
        'property_id',
        string="Mantenimientos"
    )

    #Campo contador
    maintenance_count = fields.Integer(
        string="Cantidad de Mantenimientos",
        compute="_compute_maintenance_count"
    )

    def _compute_maintenance_count(self):
        for record in self:
            record.maintenance_count = len(record.maintenance_ids)

    def action_view_maintenances(self):
        return {
            'name': 'Mantenimientos',
            'type': 'ir.actions.act_window',
            'res_model': 'property.maintenance',
            'view_mode': 'list,form',
            'domain': [('property_id', '=', self.id)],
            'context': {'default_property_id': self.id},
        }

