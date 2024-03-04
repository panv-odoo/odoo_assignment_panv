{
    'name': "Stock Trasport",
    'version': '1.0',
    'depends': ['base','mail','fleet','stock_picking_batch'],
    'author': "PANV-ODOO",
    'category': 'Stock Transport/Transport',
    'description': """
    This module is for the technical training assesment purpose
    """,
    'data':[
        'views/fleet_vehicle_model_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_picking_batch_views.xml',
        
    ],
    'license': 'LGPL-3',
}
