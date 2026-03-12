from odoo import models, fields, api

class PropertyMaintenance(models.Model):
    _name = "property.maintenance"
    _description = "Mantenimiento de Propiedad"
    _rec_name = "property_id"

    property_id = fields.Many2one(
        "patrimonial.property",
        string="Propiedad",
        required=True,
        ondelete="cascade"
    )

    fecha = fields.Date(
        string="Fecha",
        required=True,
        default=fields.Date.today
    )

    tipo_mantenimiento = fields.Selection(
        [
            ("preventivo", "Preventivo"),
            ("correctivo", "Correctivo"),
        ],
        string="Tipo de Mantenimiento",
        required=True
    )

    observaciones = fields.Text(string="Observaciones")

    usuario_id = fields.Many2one(
        "res.users",
        string="Registrado por",
        default=lambda self: self.env.user,
        readonly=True
    )

    estado = fields.Selection(
        [
            ("pendiente", "Pendiente"),
            ("completado", "Completado"),
        ],
        string="Estado",
        default="pendiente"
    )
