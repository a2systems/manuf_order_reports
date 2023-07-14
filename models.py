from odoo import tools, models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date,datetime

class StockPicking(models.Model):
    _inherit = "stock.picking"

    def _compute_source_data(self):
        for rec in self:
            res_bom_id = None
            res_product_id = None
            if rec.origin:
                manuf_id = self.env['mrp.production'].search([('name','=',rec.origin)])
                if manuf_id:
                    res_bom_id = manuf_id.bom_id.id
                    res_product_id = manuf_id.product_id.id
            rec.source_bom_id = res_bom_id
            rec.source_product_id = res_product_id

    source_bom_id = fields.Many2one('mrp.bom','LdM Origen',compute=_compute_source_data)
    source_product_id = fields.Many2one('product.product','Producto Origen',compute=_compute_source_data)
