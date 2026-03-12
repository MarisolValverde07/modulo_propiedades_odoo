{
    "name": "Gestión de Propiedades Patrimoniales y Zonas Verdes",
    "summary": "Sistema para la administración digital de bienes patrimoniales y zonas verdes municipales.",
    "description": """
        Módulo desarrollado para la Municipalidad de Pérez Zeledón
        orientado a la gestión y control de propiedades patrimoniales
        y zonas verdes.

        Funcionalidades principales:
        - Registro de expedientes
        - Clasificación por tipo de propiedad
        - Gestión de áreas y destinos
        - Administración de convenios
        - Control de mantenimiento

        Permite centralizar la información y facilitar la
        trazabilidad de los bienes municipales.
    """,
    "author": "Marisol Valverde Retana",
    "category": "Public Administration",
    "version": "19.0.1.0.0",  
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/patrimonial_property_view.xml",
        "views/property_maintenance_view.xml",
        "views/patrimonial_menus.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
