# -*- coding: utf-8 -*-

from odoo import fields, http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class website_matrix_quick_cart_view(WebsiteSale):
    def get_attribute_value_ids(self, product, list=False):
        attribute_value_ids = []
        visible_attrs = set(l.attribute_id.id
                            for l in product.attribute_line_ids if len(l.value_ids) > 1)
        pricelist_context, pricelist = self._get_pricelist_context()
        if request.website.pricelist_id.id != pricelist.id:
            website_currency_id = request.website.currency_id
            currency_id = pricelist.currency_id
            for p in product.product_variant_ids:
                price = website_currency_id._convert(p.lst_price, currency_id, request.env.user.company_id, fields.Date.today())
                attribute_value_ids.append([p.id, [v.id for v in p.product_template_attribute_value_ids if v.attribute_id.id in visible_attrs], p.price, price])
        else:
            attribute_value_ids = [[p.id, [v.id for v in p.product_template_attribute_value_ids if v.attribute_id.id in visible_attrs], p.price, p.lst_price]
                for p in product.product_variant_ids]

            attribute_value_ids_dict = []
            attribute_value_ids_list = []
            i = 0
            val = 2
            attribute_value_ids_dict.append('')
            for p in product.product_variant_ids:
                for a in p.product_template_attribute_value_ids:
                    if a.attribute_id.name not in attribute_value_ids_dict:
                        attribute_value_ids_dict.append(a.attribute_id.name)
                attribute_value_ids_list.append([p.id])
                attribute_value_ids_list[i].append(p)
                attribute_value_ids_list[i].append(['checkbox'])

                for j in range(0, len(attribute_value_ids_dict) - 0 - 1):
                        attribute_value_ids_list[i][val].append('-')
                for a in p.product_template_attribute_value_ids:
                    pos = attribute_value_ids_dict.index(a.attribute_id.name)
                    attribute_value_ids_list[i][val][pos] = a.name
                i += 1
        if list:
            return {'header': attribute_value_ids_dict, 'value': attribute_value_ids_list}
        return attribute_value_ids

    @http.route(['/shop/matrix/cart'], type='json', auth="public", methods=['POST'], website=True)
    def shop_matrix_cart(self, datas, **kw):
        order = request.website.sale_get_order(force_create=1)
        if order.state != 'draft':
            request.website.sale_reset()
            if kw.get('force_create'):
                order = request.website.sale_get_order(force_create=1)
            else:
                return {}
        value = {}
        for data in datas:
            value = order._cart_update(
                product_id=data['product_id'],
                add_qty=data['qty'],
                product_custom_attribute_values=None,
                no_variant_attribute_values=None
            )

        if not order.cart_quantity:
            request.website.sale_reset()
            return value

        order = request.website.sale_get_order()
        value['cart_quantity'] = order.cart_quantity

        value['website_sale.cart_lines'] = request.env['ir.ui.view']._render_template("website_sale.cart_lines", {
            'website_sale_order': order,
            'date': fields.Date.today(),
            'suggested_products': order._cart_accessories()
        })
        value['website_sale.short_cart_summary'] = request.env['ir.ui.view']._render_template("website_sale.short_cart_summary", {
            'website_sale_order': order,
        })
        return value

    @http.route(['/shop/<model("product.template"):product>'], type='http', auth="public", website=True, sitemap=True)
    def product(self, product, category='', search='', **kwargs):
        r = super(website_matrix_quick_cart_view, self).product(
            product, category, search, **kwargs)
        if category == 13:
            r.qcontext['variants'] = True
        r.qcontext['get_attribute_value_ids'] = self.get_attribute_value_ids
        return r
