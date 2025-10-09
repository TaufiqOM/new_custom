{
    "name": "ITCustom Total OM Price",
    "summary": "Add Total OM Price field to sale.blanket.order computed from sec_price",
    "description": "This module adds a new field 'amount_total_sec_price' to sale.blanket.order model, which computes the total based on sec_price * original_uom_qty from sale.blanket.order.line.",
    "author": "Custom",
    "website": "",
    "category": "Sales",
    "version": "1.0",
    "depends": ["sale_blanket_order"],
    "data": [
        "views/sale_blanket_order_views.xml"
    ],
    "installable": True,
    "application": False,
    "auto_install": False
}
